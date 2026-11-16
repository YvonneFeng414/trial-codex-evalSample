"""Extract an Evaluation Input from each protocol/SAP Markdown file with one Codex call per trial.

The rules come from system_prompts/Input_extraction_prompt.md. Code enforces what it can:
only the prompt's allowed sections are sent to the model. With --validate, the reply is also checked
against the prompt's output template, objective labels, removal rules and the source's numbers.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import re

from tools.codex_cli import Codex, CodexError
from tools.cost import PRICING, Ledger, load_pricing, price_warning, report as cost_report
from tools.preprocess_md import preprocess

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL = 'gpt-5.6-sol'
DEFAULT_PROMPT = ROOT / 'system_prompts/Input_extraction_prompt.md'
TITLE = '# Evaluation Input'
BENCHMARK = '## Benchmark'
PLACEHOLDERS = (r'\[PASTE BENCHMARK HERE\]', '[PASTE BENCHMARK HERE]')
InputError = CodexError  # one error type for bad sources, invalid replies and failed Codex calls

HEADING = re.compile(r'^(#{1,6})\s+(?:\d+(?:\.\d+)*\.?\s+)?(.+?)\s*#*\s*$')
LABEL = re.compile(r'^\*\*(.+?)\*\*\s*$')
OBJECTIVE_LABEL = re.compile(r'(?<![A-Za-z0-9])([PS])(\d+)(?![A-Za-z0-9])')
ABSENT = re.compile(r'\bNot (?:specified|applicable)\b', re.I)
# "Remove citations, page numbers, filenames, URLs, DOIs, and source notes."
FORBIDDEN = {
    'URL': re.compile(r'https?://|\bwww\.', re.I),
    'DOI': re.compile(r'\bdoi\b|\b10\.\d{4,9}/\S', re.I),
    'filename': re.compile(r'\b[\w-]+\.(?:pdf|docx?|xlsx?|pptx?|csv|md|txt|html?|rtf|xml|json|zip)\b', re.I),
    'page number': re.compile(r'\b(?:pages?\s+\d|pp?\.\s*\d)', re.I),
    'source note': re.compile(r'\(\s*(?:Source|Inferred)\b|^\s*(?:[-*]\s+)?(?:\*\*)?Sources?\s*:', re.I | re.M),
    'citation': re.compile(r'\[\d+(?:\s*[,–-]\s*\d+)*\]'),
}


def flat(text):
    return ' '.join(text.split())


def field(text, label):
    match = re.search(r'^\s*[-*]\s+\*\*' + re.escape(label) + r':?\*\*\s*:?[ \t]*(.*?)(?=^\s*[-*]\s+\*\*|\Z)', text, re.M | re.S | re.I)
    return flat(match[1]) if match else ''


def key(title):
    return flat(title).casefold().rstrip(':')


def label_name(text):
    return flat(text.replace('&nbsp;', ' ')).rstrip(':').strip()


def block(text, start, stop):
    """Lines after the line starting with `start`, up to the next line starting with `stop`."""
    lines = text.splitlines()
    begin = next((i for i, line in enumerate(lines) if line.startswith(start)), None)
    if begin is None:
        raise InputError(f'Prompt has no line starting with {start!r}')
    end = next((i for i in range(begin + 1, len(lines)) if lines[i].startswith(stop)), None)
    if end is None:
        raise InputError(f'Prompt has no line starting with {stop!r} after {start!r}')
    return lines[begin + 1:end]


def load_prompt(text):
    """Split the prompt into instructions and benchmark message, and read its allowed sections and output template."""
    if BENCHMARK not in text.splitlines() or not any(p in text for p in PLACEHOLDERS):
        raise InputError(f'Prompt needs a {BENCHMARK!r} heading and a benchmark placeholder')
    instructions, benchmark = text.split('\n' + BENCHMARK + '\n', 1)
    # Allowed source sections as {title: the prompt's section number}.
    allowed = {m[2]: m[1] for line in block(text, '## Allowed Sources', '#')
               if (m := re.match(r'^\s*[-*]\s+(\d+(?:\.\d+)*)?\s*(.+?)\s*$', line))}
    if not allowed:
        raise InputError('Prompt lists no allowed source sections')
    # The output template runs from its title to the closing self-check sentence.
    body = [TITLE] + block(text, TITLE, 'Before returning')
    headings, labels, guidance, current = [], {}, set(), None
    for line in body:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('#'):
            headings.append(stripped)
            current = stripped
        elif (match := LABEL.match(stripped)):
            labels.setdefault(current, []).append(label_name(match[1]))
        else:
            guidance.add(flat(stripped))
    return dict(instructions=instructions.rstrip() + '\n', benchmark=BENCHMARK + '\n' + benchmark,
                allowed=allowed, headings=headings, labels=labels, guidance=guidance)


def headings_of(lines):
    """(index, level, title) of each Markdown heading outside code fences."""
    found, fenced = [], False
    for i, line in enumerate(lines):
        if line.lstrip().startswith('```'):
            fenced = not fenced
        elif not fenced and (match := HEADING.match(line)):
            found.append((i, len(match[1]), match[2]))
    return found


def benchmark(text, allowed):
    """The source restricted to the allowed sections.

    Sections are matched by title, so a "direct equivalent" under another number counts (eligibility is §4.2 in
    these SAPs). Its heading is renumbered to the prompt's number so the model does not mistake it for an
    excluded section. Returns the benchmark text, the source headings used and the allowed titles not found.
    """
    text, _ = preprocess(text)
    lines = text.splitlines()
    heads = headings_of(lines)
    wanted = {key(title): (title, number) for title, number in allowed.items()}
    parts, used, seen, end = [], [], set(), 0
    for n, (i, level, title) in enumerate(heads):
        if i < end or key(title) not in wanted:
            continue
        end = next((j for j, other, _ in heads[n + 1:] if other <= level), len(lines))
        number = wanted[key(title)][1]
        heading = '#' * level + ' ' + (number + ' ' if number else '') + title
        parts.append('\n'.join([heading] + lines[i + 1:end]).strip())
        used.append(lines[i].strip())
        seen.add(key(title))
    if not parts:
        raise InputError('Source has none of the allowed sections')
    missing = [title for k, (title, _) in wanted.items() if k not in seen]
    return '\n\n'.join(parts) + '\n', used, missing


def message(prompt, source):
    """User message: the prompt's benchmark block with the placeholder replaced by the source text."""
    text = prompt['benchmark']
    for placeholder in PLACEHOLDERS:
        if placeholder in text:
            return text.replace(placeholder, source.strip(), 1).rstrip() + '\n'
    raise InputError('Prompt has no benchmark placeholder')


def clean(text, prompt):
    """Drop any preamble or code fence, and template guidance the model echoed back verbatim."""
    start = text.find(TITLE)
    if start >= 0:
        text = re.sub(r'\n```\s*\Z', '', text[start:].strip())
    lines = [line for line in text.strip().splitlines() if flat(line) not in prompt['guidance']]
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip() + '\n'


def numbers(text):
    """Numeric values, compared as written (thousands separators and a missing leading zero are ignored)."""
    text = OBJECTIVE_LABEL.sub(' ', text)
    text = re.sub(r'(?<=\d),(?=\d{3}(?!\d))', '', text)
    text = re.sub(r'(?<![\d.])\.(?=\d)', '0.', text)
    return {re.sub(r'^0+(?=\d)', '', n) for n in re.findall(r'\d+(?:\.\d+)?', text)}


def sections(markdown):
    """Template-level headings (levels 1-3) and the text under each, up to the next such heading."""
    lines = markdown.splitlines()
    heads = [(i, lines[i].strip()) for i, level, _ in headings_of(lines) if level <= 3]
    return [(title, '\n'.join(lines[i + 1:heads[n + 1][0] if n + 1 < len(heads) else len(lines)]).strip())
            for n, (i, title) in enumerate(heads)]


def bodies(markdown, keep):
    """{title key: text, subsections included} for each heading where keep(level, title key) holds."""
    lines = markdown.splitlines()
    heads = headings_of(lines)
    found = {}
    for n, (i, level, title) in enumerate(heads):
        if keep(level, key(title)):
            end = next((j for j, other, _ in heads[n + 1:] if other <= level), len(lines))
            found[key(title)] = '\n'.join(lines[i + 1:end]).strip()
    return found


def words(text):
    """Text without headings, bold labels and list markers."""
    return flat(re.sub(r'^#.*$|\*\*[^*\n]*\*\*|^\s*[-*]\s+', ' ', text, flags=re.M)).casefold()


def unspecified(text):
    return bool(re.fullmatch(r'(?:not specified(?: from this objective)?\W*)+', words(text)))


def objective_labels(prefix, text, problems, where):
    found = sorted({int(n) for p, n in OBJECTIVE_LABEL.findall(text) if p == prefix})
    if found and found != list(range(1, len(found) + 1)):
        problems.append(f'{where}: {prefix} labels must run {prefix}1, {prefix}2, ... without gaps (found '
                        + ', '.join(f'{prefix}{n}' for n in found) + ')')
    return found


def validate(markdown, prompt, source):
    """Problems with an Evaluation Input against the prompt's rules; empty if it complies."""
    problems = []
    if not markdown.startswith(TITLE + '\n'):
        return [f'Output does not start with {TITLE!r}']
    parts = sections(markdown)
    got = [title for title, _ in parts]
    want = prompt['headings']
    if got != want:
        i = next((i for i, (a, b) in enumerate(zip(got, want)) if a != b), min(len(got), len(want)))
        problems.append(f'Headings differ from the template at #{i + 1}: expected '
                        f'{want[i] if i < len(want) else "<end>"!r}, got {got[i] if i < len(got) else "<end>"!r}')
        return problems
    body = dict(parts)
    for n, title in enumerate(want):
        leaf = n + 1 == len(want) or len(want[n + 1].split()[0]) <= len(title.split()[0])
        if leaf and not body[title]:
            problems.append(f'{title}: empty (write "Not specified" when the source gives nothing)')
        for name in prompt['labels'].get(title, []):
            if not re.search(r'^\s*(?:[-*]\s+)?\*\*' + re.escape(name) + r'\b', body[title], re.M):
                problems.append(f'{title}: missing the **{name}** field')
    # Objective-level outcomes: P1, P2, ... under primary and S1, S2, ... under secondary/exploratory objectives.
    primary = next((t for t in want if t.startswith('###') and 'primary objective' in t.lower()), None)
    secondary = next((t for t in want if t.startswith('###') and 'secondary' in t.lower() and 'objective' in t.lower()), None)
    for title, prefix, other in ((primary, 'P', 'S'), (secondary, 'S', 'P')):
        if title is None:
            continue
        text = body[title]
        if not objective_labels(prefix, text, problems, title) and not ABSENT.search(text):
            problems.append(f'{title}: no {prefix}1, {prefix}2, ... labels and no "Not specified"')
        if any(p == other for p, _ in OBJECTIVE_LABEL.findall(text)):
            problems.append(f'{title}: contains {other} labels, which belong to the other objective tier')
    # "Not specified" is for absent information: a section left wholly unspecified must have nothing in the source.
    allowed = {key(title) for title in prompt['allowed']}
    given = bodies(source, lambda level, title: title in allowed)
    for title, text in bodies(markdown, lambda level, title: level == 2 and title in allowed).items():
        stated = words(given.get(title, ''))
        if unspecified(text) and stated and not re.match(r'(?:not (?:reported|specified|stated)|none)\b', stated):
            problems.append(f'{title}: written as "Not specified" although the source section has content')
    content = '\n'.join(text for _, text in parts)
    for name, pattern in FORBIDDEN.items():
        if (match := pattern.search(content)):
            problems.append(f'Contains a {name} ({flat(match[0])!r}); these must be removed')
    extra = sorted(numbers(content) - numbers(source), key=lambda n: float(n))
    if extra:
        problems.append('Numbers not found in the allowed source sections: ' + ', '.join(extra[:20])
                        + (' ...' if len(extra) > 20 else ''))
    return problems


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(text, encoding='utf-8')
    temporary.replace(path)


def extract(path, destination, prompt, call, validate_output=False):
    """One Codex call; call(message) returns (reply, token usage, elapsed seconds).

    With validate_output, a reply that breaks the prompt's rules is kept as DESTINATION.rejected, never as
    DESTINATION; without it, every reply is written to DESTINATION. Returns status
    ('written', 'rejected' or 'failed'), problems, sections, and the call's usage and elapsed time for the ledger.
    """
    source, used, missing = benchmark(path.read_text(encoding='utf-8'), prompt['allowed'])
    result = dict(sections=used, missing_sections=missing)
    try:
        reply, tokens, elapsed = call(message(prompt, source))
    except CodexError as error:
        destination.unlink(missing_ok=True)  # never leave an output from an earlier run looking current
        return dict(result, status='failed', problems=[str(error)], usage=error.usage, elapsed=error.elapsed)
    output = clean(reply, prompt)
    rejected = destination.with_name(destination.name + '.rejected')
    problems = validate(output, prompt, source) if validate_output else []
    if problems:
        destination.unlink(missing_ok=True)
        write(rejected, output)
    else:
        rejected.unlink(missing_ok=True)
        write(destination, output)
    return dict(result, status='rejected' if problems else 'written', problems=problems, usage=tokens, elapsed=elapsed)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('input', nargs='?', type=Path, default=ROOT / 'smoke_run_data/a')
    parser.add_argument('--out', type=Path, default=ROOT / 'smoke_run_data/inputs')
    parser.add_argument('--prompt', type=Path, default=DEFAULT_PROMPT)
    parser.add_argument('--codex-home', type=Path, default=Path(os.environ.get('CODEX_HOME', ROOT / '.codex-home')))
    parser.add_argument('--model', default=DEFAULT_MODEL, help=f'Codex model (default: {DEFAULT_MODEL})')
    parser.add_argument('--effort', help="Reasoning effort, e.g. low, medium, high (default: the model's default level)")
    parser.add_argument('--timeout', type=float, default=900)
    parser.add_argument('--jobs', type=int, default=4, help='Trials extracted in parallel (default: 4)')
    parser.add_argument('--validate', action='store_true', help='Check replies against the prompt and reject those that break it (default: off)')
    parser.add_argument('--skip-existing', action='store_true', help='Keep existing outputs instead of calling Codex (re-checked with --validate)')
    parser.add_argument('--dry-run', action='store_true', help='Build the benchmark text and report sections; no Codex calls or writes')
    parser.add_argument('--report', action='store_true', help='Print per-trial JSON details')
    parser.add_argument('--ledger', type=Path, help='Append-only cost ledger TSV (default: OUT/cost_ledger.tsv)')
    parser.add_argument('--pricing', type=Path, default=PRICING, help='Price table (default: tools/pricing.json)')
    args = parser.parse_args()
    files = [args.input] if args.input.is_file() else sorted(args.input.rglob('*.md'))
    if not files:
        parser.error('No input Markdown files found')
    if args.timeout <= 0 or args.jobs < 1:
        parser.error('--timeout and --jobs must be positive')
    try:
        prompt = load_prompt(args.prompt.read_text(encoding='utf-8'))
    except (OSError, InputError) as error:
        parser.error(f'Invalid prompt {args.prompt}: {error}')
    try:
        pricing = load_pricing(args.pricing)
    except (OSError, ValueError) as error:
        parser.error(f'Invalid pricing file {args.pricing}: {error}')
    if (warning := price_warning(pricing, args.model, args.pricing)):
        print(warning, flush=True)
    codex = ledger = None
    if not args.dry_run:
        try:
            codex = Codex(args.codex_home.resolve(), args.model, args.timeout, prompt['instructions'], args.effort)
        except InputError as error:
            parser.error(str(error))
        if codex.note:
            print(codex.note, flush=True)
        ledger = Ledger(args.ledger or args.out / 'cost_ledger.tsv', pricing, codex.model, codex.effort)

    def run(path):
        relative = Path(path.name) if args.input.is_file() else path.relative_to(args.input)
        destination = args.out / relative.parent / ('input_' + path.stem + '.md')
        record = {'source': str(path), 'output': str(destination)}
        fresh = not args.dry_run and not (args.skip_existing and destination.exists())
        try:
            if not fresh:
                source, used, missing = benchmark(path.read_text(encoding='utf-8'), prompt['allowed'])
                problems = []
                if args.dry_run:
                    record['status'], record['benchmark_chars'] = 'dry-run', len(source)
                else:
                    record['status'] = 'exists'
                    if args.validate:
                        problems = validate(destination.read_text(encoding='utf-8'), prompt, source)
            else:
                result = extract(path, destination, prompt, codex.run, args.validate)
                usd = ledger.record(path.stem, result['status'], result['usage'], result['elapsed'])
                used, missing, problems = result['sections'], result['missing_sections'], result['problems']
                record.update(status=result['status'], usage=result['usage'], cost_usd=usd)
            record.update(sections=used, missing_sections=missing)
            if problems:
                record.update(status='failed' if record['status'] == 'failed' else 'rejected', problems=problems)
        except (InputError, OSError) as error:
            record.update(status='failed', problems=[str(error)])
            if fresh:
                destination.unlink(missing_ok=True)  # never leave an output from an earlier run looking current
        if args.report:
            print(json.dumps(record, ensure_ascii=False), flush=True)
        else:
            detail = '; '.join(record.get('problems', []))
            print(f"{path.name}: {record['status']}" + (f' ({detail})' if detail else ''), flush=True)
        return record

    with ThreadPoolExecutor(args.jobs) as pool:
        records = list(pool.map(run, files))
    bad = sum(r['status'] in ('rejected', 'failed') for r in records)
    calls = codex.calls if codex else 0
    print(f'{len(files)} trials; {bad} rejected or failed; {calls} Codex calls'
          + (f' ({codex.model}, effort {codex.effort})' if codex else ''), flush=True)
    for line in cost_report(ledger):
        print(line, flush=True)
    return int(bool(bad))


if __name__ == '__main__':
    raise SystemExit(main())

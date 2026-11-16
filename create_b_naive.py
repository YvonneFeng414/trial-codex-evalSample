"""Draft naive-baseline protocols/SAPs (B_naive) from Evaluation Inputs with one Codex CLI call per trial.

The rules come from system_prompts/llm_generation_prompt.md. Everything before its "## Evaluation Input"
heading is the system prompt; that block, with the placeholder replaced by one input_*.md file, is the only
user message. With --validate, code then checks what it can of the prompt's rules: the exact section titles and order,
one evidence label on every substantive paragraph, bullet and table row, preserved input numbers, no
[Provided] numbers absent from the input, and no citations or provenance. Every Codex call is appended to
a cost ledger.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import csv
import json
import os
from pathlib import Path
import re

from tools.codex_cli import Codex, CodexError
from tools.cost import PRICING, Ledger, load_pricing, price_warning, report as cost_report
from tools.create_inputs import DEFAULT_MODEL, FORBIDDEN, HEADING, TITLE as INPUT_TITLE, flat, headings_of, numbers

ROOT = Path(__file__).resolve().parent
DEFAULT_PROMPT = ROOT / 'system_prompts/llm_generation_prompt.md'
TITLE = '# Clinical Study Protocol and Statistical Analysis Framework'
END = 'Return only the completed Markdown'  # the sentence that closes the prompt's output framework
INPUT = '## Evaluation Input'
PLACEHOLDERS = (r'\[PASTE EVALUATION INPUT HERE\]', '[PASTE EVALUATION INPUT HERE]')
STATUS = re.compile(r'\\?\[(Provided|Derived|Proposed|Clarification Required)\\?\]')
LIST_ITEM = re.compile(r'^\s*(?:[-*+]|\d+[.)])\s+')
TABLE_RULE = re.compile(r'^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)*\|?\s*$')
COLUMNS = ('output', 'format', 'detail')
ARM_TAG = 'tag.json'  # model and effort that produced the outputs in an arm folder
SHOWN = 3  # examples listed per problem


class PromptError(ValueError):
    pass


def unescape(heading):
    """Heading text without Markdown backslash escapes, so '## 1\\. Introduction' equals '## 1. Introduction'."""
    return flat(re.sub(r'\\(.)', r'\1', heading))


def load_prompt(text):
    """Split the prompt into instructions and user-message block, and read the output framework's headings."""
    lines = text.splitlines()
    if INPUT not in lines or not any(p in text for p in PLACEHOLDERS):
        raise PromptError(f'Prompt needs a {INPUT!r} heading and an input placeholder')
    if TITLE not in lines:
        raise PromptError(f'Prompt has no {TITLE!r} line')
    instructions, block = text.split('\n' + INPUT + '\n', 1)
    start = lines.index(TITLE)
    end = next((i for i in range(start, len(lines)) if lines[i].startswith(END)), None)
    if end is None:
        raise PromptError(f'Prompt has no line starting with {END!r} after the framework')
    headings = [unescape(line) for line in lines[start:end] if line.startswith('#')]
    return dict(instructions=instructions.rstrip() + '\n', block=INPUT + '\n' + block, headings=headings)


def message(prompt, evaluation_input):
    """User message: the prompt's Evaluation Input block with the placeholder replaced by the input."""
    for placeholder in PLACEHOLDERS:
        if placeholder in prompt['block']:
            return prompt['block'].replace(placeholder, evaluation_input.strip(), 1).rstrip() + '\n'
    raise PromptError('Prompt has no input placeholder')


def clean(text):
    """Drop any code fence or preamble around the document; keep the text as is if the title is missing."""
    start = text.find(TITLE)
    if start < 0:
        return text.strip() + '\n'
    return re.sub(r'\n```\s*\Z', '', text[start:].strip()).strip() + '\n'


def units(markdown):
    """(section, kind, text) of each paragraph, bullet and table row; headings, rules and code are skipped.

    A table's header row is skipped too, and a bullet's or paragraph's continuation lines join it.
    """
    out, section, current, fenced = [], '', None, False

    def flush():
        nonlocal current
        if current:
            out.append(current)
        current = None

    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith(('```', '~~~')):
            flush()
            fenced = not fenced
        elif fenced:
            continue
        elif not stripped or re.fullmatch(r'(?:[-*_]\s*){3,}', stripped):
            flush()
        elif HEADING.match(stripped):
            flush()
            section = stripped
        elif stripped.startswith('|'):
            flush()
            if TABLE_RULE.match(stripped):
                if out and out[-1][1] == 'table row':
                    out.pop()  # the header row above the separator
            else:
                out.append((section, 'table row', stripped))
        elif LIST_ITEM.match(line):
            flush()
            current = (section, 'bullet', stripped)
        elif current:
            current = (current[0], current[1], current[2] + ' ' + stripped)
        else:
            current = (section, 'paragraph', stripped)
    flush()
    return out


def lead_in(text):
    """Bold-only labels and lines ending in a colon introduce content rather than state it."""
    bare = LIST_ITEM.sub('', text).strip()
    return (not bare.strip('|*_` ') or bool(re.fullmatch(r'(\*\*|__|\*|_)[^*_]+\1:?', bare))
            or bare.rstrip('*_ ').endswith(':'))


def body_numbers(markdown):
    """Numbers outside headings."""
    lines = markdown.splitlines()
    heads = {i for i, _, _ in headings_of(lines)}
    return numbers('\n'.join(line for i, line in enumerate(lines) if i not in heads))


def examples(items):
    shown = '; '.join(f'{unescape(section).lstrip("# ")}: {flat(text)[:80]!r}' for section, text in items[:SHOWN])
    return shown + (f'; +{len(items) - SHOWN} more' if len(items) > SHOWN else '')


def validate(markdown, prompt, evaluation_input):
    """Problems with an output against the prompt's rules; empty if it complies."""
    if not markdown.startswith(TITLE + '\n'):
        return [f'Output does not start with {TITLE!r}']
    problems, lines = [], markdown.splitlines()
    got = [unescape(lines[i]) for i, level, _ in headings_of(lines) if level <= 3]
    want = prompt['headings']
    if got != want:
        i = next((i for i, (a, b) in enumerate(zip(got, want)) if a != b), min(len(got), len(want)))
        problems.append(f'Section titles differ from the framework at #{i + 1}: expected '
                        f'{want[i] if i < len(want) else "<end>"!r}, got {got[i] if i < len(got) else "<end>"!r}')
    unlabelled, multiple, provided = [], [], []
    stated = numbers(evaluation_input) | numbers('\n'.join(want))
    for section, kind, text in units(markdown):
        found = STATUS.findall(text)
        if len(found) > 1:
            multiple.append((section, text))
        elif not found and not lead_in(text):
            unlabelled.append((section, text))
        elif found == ['Provided'] and (extra := numbers(text) - stated):
            provided.append((section, f"{', '.join(sorted(extra, key=float))} in {text}"))
    if unlabelled:
        problems.append(f'{len(unlabelled)} paragraphs, bullets or table rows have no evidence label: {examples(unlabelled)}')
    if multiple:
        problems.append(f'{len(multiple)} carry more than one evidence label and must be split: {examples(multiple)}')
    if provided:
        problems.append(f'{len(provided)} [Provided] statements have numbers not in the Evaluation Input: {examples(provided)}')
    missing = sorted(body_numbers(evaluation_input) - numbers(markdown), key=float)
    if missing:
        problems.append('Evaluation Input numbers not preserved: ' + ', '.join(missing[:20]) + (' ...' if len(missing) > 20 else ''))
    for name, pattern in FORBIDDEN.items():
        if (match := pattern.search(markdown)):
            problems.append(f'Contains a {name} ({flat(match[0])!r}); citations and provenance are not allowed')
    if any(p in markdown for p in PLACEHOLDERS):
        problems.append('Contains the input placeholder')
    return problems


def check(markdown, prompt, evaluation_input):
    """Format-check result: '' if the output follows the prompt, else its problems."""
    return '; '.join(validate(markdown, prompt, evaluation_input))


def read_input(path):
    text = path.read_text(encoding='utf-8')
    if not text.startswith(INPUT_TITLE):
        raise PromptError(f'{path.name} is not an Evaluation Input (no {INPUT_TITLE!r} title)')
    return text


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(text, encoding='utf-8')
    temporary.replace(path)


def draft(evaluation_input, destination, prompt, call, validate_output=False):
    """One Codex call; call(message) returns (reply, token usage, elapsed seconds).

    The output is kept whether or not it passes the format check, which runs only with validate_output.
    Returns status ('written' or 'failed'), the format-check detail, and the call's usage and elapsed time.
    """
    try:
        reply, tokens, elapsed = call(message(prompt, evaluation_input))
    except CodexError as error:
        destination.unlink(missing_ok=True)  # never leave an output from an earlier run looking current
        return dict(status='failed', detail=str(error), usage=error.usage, elapsed=error.elapsed)
    output = clean(reply)
    write(destination, output)
    detail = check(output, prompt, evaluation_input) if validate_output else ''
    return dict(status='written', detail=detail, usage=tokens, elapsed=elapsed)


def write_arm_tag(root, records, model, effort):
    """Record in root/tag.json which model and effort produced its outputs; 'mixed' once they come from different runs."""
    written = {Path(r['output']).resolve() for r in records if r['status'] == 'written'}
    if not written:
        return None
    path, tag = root / ARM_TAG, {'model': model, 'effort': effort}
    try:
        prior = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        prior = {'model': 'unknown', 'effort': 'unknown'}
    if any(p.resolve() not in written for p in root.rglob('*.md')) and {k: prior.get(k) for k in tag} != tag:
        runs = prior.get('runs') or [{k: prior.get(k) for k in tag}]
        tag = {'model': 'mixed', 'effort': 'mixed', 'runs': runs + [tag]}
    write(path, json.dumps(tag, indent=2) + '\n')
    return tag


def write_tags(path, records, root):
    """Merge this run's format results into the TSV, keyed by output file."""
    rows = {}
    if path.exists():
        with path.open(encoding='utf-8', newline='') as handle:
            rows = {row['output']: row for row in csv.DictReader(handle, delimiter='\t')}
    for record in records:
        if record['status'] != 'dry-run':
            key = str(Path(record['output']).relative_to(root))
            rows[key] = {'output': key, 'format': record['format'], 'detail': flat(record.get('detail', ''))}
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.tsv.tmp')
    with temporary.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, COLUMNS, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows[key] for key in sorted(rows))
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('input', nargs='?', type=Path, default=ROOT / 'smoke_run_data/inputs')
    parser.add_argument('--out', type=Path, default=ROOT / 'smoke_run_data/b_naive')
    parser.add_argument('--prompt', type=Path, default=DEFAULT_PROMPT)
    parser.add_argument('--codex-home', type=Path, default=Path(os.environ.get('CODEX_HOME', ROOT / '.codex-home')))
    parser.add_argument('--model', default=DEFAULT_MODEL, help=f'Codex model (default: {DEFAULT_MODEL})')
    parser.add_argument('--effort', help="Reasoning effort, e.g. low, medium, high (default: the model's default level)")
    parser.add_argument('--timeout', type=float, default=900)
    parser.add_argument('--jobs', type=int, default=4, help='Trials drafted in parallel (default: 4)')
    parser.add_argument('--validate', action='store_true', help='Format-check outputs and record results in --tags (default: off)')
    parser.add_argument('--skip-existing', action='store_true', help='Keep outputs that already exist (re-checked with --validate)')
    parser.add_argument('--tags', type=Path, help='Format-check TSV, written only with --validate (default: OUT/format_check.tsv)')
    parser.add_argument('--dry-run', action='store_true', help='Read inputs and list outputs without Codex calls or writes')
    parser.add_argument('--report', action='store_true', help='Print per-trial JSON details')
    parser.add_argument('--ledger', type=Path, help='Append-only cost ledger TSV (default: OUT/cost_ledger.tsv)')
    parser.add_argument('--pricing', type=Path, default=PRICING, help='Price table (default: tools/pricing.json)')
    args = parser.parse_args()
    files = [args.input] if args.input.is_file() else sorted(args.input.rglob('input_*.md'))
    if not files:
        parser.error('No input_*.md Evaluation Inputs found')
    if args.timeout <= 0 or args.jobs < 1:
        parser.error('--timeout and --jobs must be positive')
    tags = args.tags or args.out / 'format_check.tsv'
    try:
        prompt = load_prompt(args.prompt.read_text(encoding='utf-8'))
    except (OSError, PromptError) as error:
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
        except CodexError as error:
            parser.error(str(error))
        if codex.note:
            print(codex.note, flush=True)
        ledger = Ledger(args.ledger or args.out / 'cost_ledger.tsv', pricing, codex.model, codex.effort)

    def run(path):
        relative = Path(path.name) if args.input.is_file() else path.relative_to(args.input)
        destination = args.out / relative.parent / (path.stem.removeprefix('input_') + '.md')
        record = {'source': str(path), 'output': str(destination)}
        fresh = not args.dry_run and not (args.skip_existing and destination.exists())
        try:
            evaluation_input = read_input(path)
            if args.dry_run:
                record.update(status='dry-run', message_chars=len(message(prompt, evaluation_input)))
            elif not fresh:
                record['status'] = 'exists'
                if args.validate:
                    detail = check(destination.read_text(encoding='utf-8'), prompt, evaluation_input)
                    record.update(format='fail' if detail else 'pass', detail=detail)
            else:
                result = draft(evaluation_input, destination, prompt, codex.run, args.validate)
                usd = ledger.record(path.stem.removeprefix('input_'), result['status'], result['usage'], result['elapsed'])
                record.update(status=result['status'], detail=result['detail'], usage=result['usage'], cost_usd=usd)
                if args.validate:
                    record['format'] = 'missing' if result['status'] == 'failed' else 'fail' if result['detail'] else 'pass'
        except (PromptError, OSError) as error:
            record.update(status='failed', detail=str(error))
            if args.validate:
                record['format'] = 'missing'
            if fresh:
                destination.unlink(missing_ok=True)
        if not record.get('detail'):
            record.pop('detail', None)
        if args.report:
            print(json.dumps(record, ensure_ascii=False), flush=True)
        else:
            tag = f" [format {record['format']}]" if 'format' in record else ''
            print(f"{path.name}: {record['status']}{tag}" + (f" ({record['detail']})" if 'detail' in record else ''), flush=True)
        return record

    with ThreadPoolExecutor(args.jobs) as pool:
        records = list(pool.map(run, files))
    if not args.dry_run:
        if args.validate:
            write_tags(tags, records, args.out)
        if (tag := write_arm_tag(args.out, records, codex.model, codex.effort)) and tag['model'] == 'mixed':
            print(f'warning: {args.out} now holds outputs from different models or efforts; see {args.out / ARM_TAG}', flush=True)
    failures = sum(r['status'] == 'failed' for r in records)
    invalid = sum(r.get('format') == 'fail' for r in records)
    checked = f'{invalid} kept with format failures' if args.validate else 'not format-checked'
    print(f'{len(files)} trials; {failures} failed; {checked}; {codex.calls if codex else 0} Codex calls'
          + (f' ({codex.model}, effort {codex.effort})' if codex else '')
          + (f'; tags in {tags}' if codex and args.validate else ''), flush=True)
    for line in cost_report(ledger):
        print(line, flush=True)
    return int(bool(failures))


if __name__ == '__main__':
    raise SystemExit(main())

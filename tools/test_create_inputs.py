"""Run with python3 -m unittest tools.test_create_inputs."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from tools.codex_cli import Codex, CodexError, catalog_entry
from tools.cost import Ledger, cost, ledger_total, load_pricing, stale, usage
from tools.create_inputs import (DEFAULT_PROMPT, ROOT, InputError, benchmark, clean, extract, load_prompt,
                                 message, validate)

PROMPT = load_prompt(DEFAULT_PROMPT.read_text(encoding='utf-8'))
FIXTURES = sorted((ROOT / 'smoke_run_data/a').glob('*.md'))
SOURCE = '''# Statistical Analysis Plan

### 1.1 Background and Rationale

Drug X versus placebo in adults with condition Y (see https://example.org).

### 1.2 Objectives

**Primary Objectives**

- Compare Drug X with placebo for Day-90 response.

### 2.3 Sample Size

- **Planned Sample Size:** 456 patients (Source: protocol p. 12).

### 2.5 Statistical Interim Analyses

- One interim analysis at 50% information, alpha 0.003.

### 4.2 Eligibility Criteria Summary

Adults aged >=18 years.

### 5.1 Primary Outcomes

**Outcome: Response at Day 90** defined as score >= 4.
'''
GOOD = '''# Evaluation Input

## 1.1 Background and Rationale

Drug X versus placebo in adults with condition Y.

## 1.2 Objectives

### Primary Objectives

- **P1:** Compare Drug X with placebo for Day-90 response.
  - **Outcome:** Day-90 response.

### Secondary/Exploratory Objectives

Not specified

## 2.1 Trial Design

### Design Type

Not specified

### Allocation Ratio

Not specified

### Intervention Summary

Drug X versus placebo.

## 2.2 Randomization

**Method:** Not specified

## 2.3 Sample Size

### Planned Sample Size

456 patients.

## 2.4 Hypothesis Framework

Not specified

## 2.5 Timing of Analyses

Not specified

## 3.2 Eligibility Criteria Summary

### Inclusion Criteria

Adults aged >=18 years.

### Exclusion Criteria

Not specified
'''


class PromptTests(unittest.TestCase):
    def test_prompt_is_parsed(self):
        self.assertEqual(list(PROMPT['allowed'].items())[0], ('Background and Rationale', '1.1'))
        self.assertEqual(PROMPT['allowed']['Eligibility Criteria Summary'], '3.2')
        self.assertIn('Eligibility Criteria Summary', PROMPT['allowed'])
        self.assertNotIn('Statistical Interim Analyses', PROMPT['allowed'])
        self.assertEqual(PROMPT['headings'][0], '# Evaluation Input')
        self.assertIn('## 2.5 Timing of Analyses', PROMPT['headings'])
        self.assertEqual(PROMPT['labels'], {'## 2.2 Randomization': ['Method']})
        self.assertNotIn('## Benchmark', PROMPT['instructions'])
        self.assertIn('Objective-Level Outcomes', PROMPT['instructions'])

    def test_message_fills_placeholder(self):
        text = message(PROMPT, 'SOURCE TEXT')
        self.assertTrue(text.startswith('## Benchmark\n'))
        self.assertIn('SOURCE TEXT', text)
        self.assertNotIn('PASTE BENCHMARK', text)


class BenchmarkTests(unittest.TestCase):
    def test_only_allowed_sections_are_sent(self):
        text, used, missing = benchmark(SOURCE, PROMPT['allowed'])
        self.assertIn('### 4.2 Eligibility Criteria Summary', used)  # matched by title, not number
        self.assertIn('### 3.2 Eligibility Criteria Summary\n\nAdults', text)  # and given the prompt's number
        self.assertNotIn('4.2', text)
        self.assertIn('Trial Design', missing)
        self.assertNotIn('interim analysis', text)
        self.assertNotIn('Primary Outcomes', text)
        self.assertNotIn('Source:', text)

    def test_all_fixtures_have_every_allowed_section(self):
        self.assertTrue(FIXTURES)
        for path in FIXTURES:
            with self.subTest(path=path.name):
                text, used, missing = benchmark(path.read_text(encoding='utf-8'), PROMPT['allowed'])
                self.assertEqual(missing, [])
                self.assertEqual(len(used), len(PROMPT['allowed']))
                for excluded in ('Statistical Interim Analyses', 'Protocol Deviations', 'Primary Outcomes',
                                 'Secondary Outcomes', 'Analysis Methods'):
                    self.assertNotIn(excluded, text)

    def test_source_without_allowed_sections(self):
        with self.assertRaises(InputError):
            benchmark('### 5.1 Primary Outcomes\n\ntext\n', PROMPT['allowed'])


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.source = benchmark(SOURCE, PROMPT['allowed'])[0]

    def problems(self, text):
        return validate(clean(text, PROMPT), PROMPT, self.source)

    def test_compliant_output(self):
        self.assertEqual(self.problems(GOOD), [])

    def test_fence_preamble_and_echoed_guidance_are_dropped(self):
        echoed = GOOD.replace('## 2.4 Hypothesis Framework\n\n', '## 2.4 Hypothesis Framework\n\nPreserve only the supplied '
                              'hypothesis structure, testing sequence, and decision rules. Do not create new hypotheses.\n\n')
        self.assertEqual(self.problems('Here it is:\n```markdown\n' + echoed + '```\n'), [])

    def assertProblem(self, text, fragment):
        problems = self.problems(text)
        self.assertTrue(any(fragment in p for p in problems), problems)

    def test_heading_changes(self):
        self.assertProblem(GOOD.replace('## 2.5 Timing of Analyses', '## 2.6 Timing of Analyses'), 'Headings differ')
        self.assertProblem(GOOD.replace('## 2.4 Hypothesis Framework\n\nNot specified\n\n', ''), 'Headings differ')
        self.assertProblem(GOOD + '\n## Notes\n\nextra\n', 'Headings differ')

    def test_empty_section_and_missing_field(self):
        self.assertProblem(GOOD.replace('### Exclusion Criteria\n\nNot specified', '### Exclusion Criteria\n'), 'empty')
        self.assertProblem(GOOD.replace('**Method:** Not specified', 'Not specified'), '**Method**')

    def test_objective_labels(self):
        self.assertProblem(GOOD.replace('**P1:**', '**P2:**'), 'without gaps')
        self.assertProblem(GOOD.replace('**P1:**', ''), 'no P1')
        self.assertProblem(GOOD.replace('Not specified\n\n## 2.1', '- **P2:** misplaced\n\n## 2.1'), 'other objective tier')

    def test_removal_rules(self):
        for addition, kind in (('See https://example.org.', 'URL'), ('doi:10.1056/NEJMoa1', 'DOI'),
                               ('From protocol.pdf.', 'filename'), ('(Source: protocol)', 'source note'),
                               ('As on p. 12.', 'page number'), ('As before [3].', 'citation')):
            with self.subTest(kind=kind):
                self.assertProblem(GOOD.replace('Drug X versus placebo.', 'Drug X versus placebo. ' + addition), kind)

    def test_not_specified_only_when_source_is_silent(self):
        dropped = GOOD.replace('Adults aged >=18 years.', 'Not specified.')
        self.assertProblem(dropped, 'eligibility criteria summary: written as "Not specified"')
        silent = benchmark(SOURCE.replace('Adults aged >=18 years.', 'Not reported in protocol.'), PROMPT['allowed'])[0]
        self.assertEqual(validate(dropped, PROMPT, silent), [])

    def test_numbers_must_come_from_allowed_sections(self):
        self.assertProblem(GOOD.replace('456 patients.', '456 patients; interim at alpha 0.003.'), '0.003')
        self.assertEqual(self.problems(GOOD.replace('>=18', '>= 18')), [])


class ExtractTests(unittest.TestCase):
    def test_writes_compliant_and_rejects_noncompliant(self):
        with tempfile.TemporaryDirectory() as directory:
            source, destination = Path(directory) / 'trial.md', Path(directory) / 'out/input_trial.md'
            source.write_text(SOURCE, encoding='utf-8')
            sent = []
            codex = lambda text: (sent.append(text) or GOOD, {}, 0.0)
            self.assertEqual(extract(source, destination, PROMPT, codex, True)['status'], 'written')
            self.assertEqual(destination.read_text(encoding='utf-8'), GOOD)
            self.assertNotIn('Statistical Interim Analyses', sent[0])
            bad = lambda text: (GOOD.replace('456', '500'), {}, 0.0)
            result = extract(source, destination, PROMPT, bad, True)
            self.assertEqual(result['status'], 'rejected')
            self.assertTrue(result['problems'])
            self.assertFalse(destination.exists())
            self.assertTrue(destination.with_name('input_trial.md.rejected').exists())
            # Validation is off by default: the same reply is written and any stale rejection removed.
            result = extract(source, destination, PROMPT, bad)
            self.assertEqual((result['status'], result['problems']), ('written', []))
            self.assertTrue(destination.exists())
            self.assertFalse(destination.with_name('input_trial.md.rejected').exists())

    def test_failed_call_keeps_its_usage(self):
        with tempfile.TemporaryDirectory() as directory:
            source, destination = Path(directory) / 'trial.md', Path(directory) / 'input_trial.md'
            source.write_text(SOURCE, encoding='utf-8')
            destination.write_text('stale', encoding='utf-8')

            def fail(text):
                raise CodexError('Codex exited 1: boom', {'input_tokens': 900, 'output_tokens': 10}, 2.5)
            result = extract(source, destination, PROMPT, fail)
            self.assertEqual((result['status'], result['usage']['input_tokens'], result['elapsed']), ('failed', 900, 2.5))
            self.assertFalse(destination.exists())

    def test_codex_command_uses_prompt_as_only_instructions(self):
        home = Path(tempfile.mkdtemp())
        (home / 'models_cache.json').write_text('{"models": [{"slug": "m", "default_reasoning_level": "low",'
                                                ' "supported_reasoning_levels": [{"effort": "low"}]}]}')

        def run(command, **kwargs):
            config = command[command.index('--strict-config'):]
            path = next(c.split('=', 1)[1] for c in config if c.startswith('model_instructions_file='))
            self.assertEqual(Path(path.strip('"')).read_text(encoding='utf-8'), PROMPT['instructions'])
            self.assertIn('read-only', command)
            self.assertEqual(kwargs['input'], 'user message')
            self.assertIn('--json', command)
            Path(command[command.index('--output-last-message') + 1]).write_text(GOOD)
            events = '{"type":"thread.started"}\n{"type":"turn.completed","usage":{"input_tokens":1200,"cached_input_tokens":200,"output_tokens":300,"reasoning_output_tokens":100}}\n'
            return subprocess.CompletedProcess(command, 0, events, '')
        with patch('tools.codex_cli.subprocess.run', side_effect=run):
            self.assertEqual(Codex(home, 'm', 10, PROMPT['instructions'])('user message'), GOOD)
            text, tokens, elapsed = Codex(home, 'm', 10, PROMPT['instructions']).run('user message')
            self.assertEqual((tokens['input_tokens'], tokens['cached_input_tokens'], tokens['output_tokens']), (1200, 200, 300))
        with patch.dict('os.environ', {'OPENAI_BASE_URL': 'http://proxy.local/v1'}):
            self.assertIn('openai_base_url="http://proxy.local/v1"', Codex(home, 'm', 10, 'x').options)
        with patch.dict('os.environ', {}, clear=True):
            self.assertFalse(any('openai_base_url' in o for o in Codex(home, 'm', 10, 'x').options))

    def test_unlisted_model_borrows_closest_listed_entry(self):
        models = [{'slug': 'gpt-reserve', 'visibility': 'hide', 'priority': 1},
                  {'slug': 'gpt-6-luna', 'visibility': 'list', 'priority': 2, 'context_window': 6},
                  {'slug': 'gpt-5.6-terra', 'visibility': 'list', 'priority': 3},
                  {'slug': 'gpt-5.6-luna', 'visibility': 'list', 'priority': 4}]
        self.assertEqual(catalog_entry(models, 'gpt-6-luna'), (models[1], None))
        entry, base = catalog_entry(models, 'gpt-6.1-sol')
        self.assertEqual((base, entry['slug'], entry['context_window']), ('gpt-6-luna', 'gpt-6.1-sol', 6))
        self.assertEqual(catalog_entry(models, 'gpt-5.6-sol')[1], 'gpt-5.6-terra')  # tie: Codex's ranking
        self.assertEqual(catalog_entry(models, 'o9')[1], 'gpt-6-luna')  # no shared prefix: top visible model
        home = Path(tempfile.mkdtemp())
        (home / 'models_cache.json').write_text(json.dumps({'models': [
            {'slug': 'm', 'default_reasoning_level': 'low', 'supported_reasoning_levels': [{'effort': 'low'}]}]}))
        codex = Codex(home, 'm2', 10, 'x')
        self.assertEqual((codex.base, codex.effort), ('m', 'low'))
        self.assertIn("m2 is not in Codex's model list", codex.note)
        catalog = json.loads(codex.catalog.read_text(encoding='utf-8'))['models']
        self.assertEqual([m['slug'] for m in catalog], ['m2'])
        self.assertIsNone(Codex(home, 'm', 10, 'x').note)



class CostTests(unittest.TestCase):
    PRICING = load_pricing()

    def test_usage_sums_turns_and_ignores_other_lines(self):
        jsonl = ('not json\n{"type":"turn.completed","usage":{"input_tokens":10,"output_tokens":5}}\n'
                 '{"type":"item.completed"}\n{"type":"turn.completed","usage":{"input_tokens":1,"cached_input_tokens":1}}\n')
        self.assertEqual(usage(jsonl), {'input_tokens': 11, 'cached_input_tokens': 1, 'cache_write_input_tokens': 0,
                                        'output_tokens': 5, 'reasoning_output_tokens': 0})

    def test_cost_uses_cached_and_long_context_rates(self):
        tokens = {'input_tokens': 10_000, 'cached_input_tokens': 4_000, 'cache_write_input_tokens': 1_000,
                  'output_tokens': 2_000, 'reasoning_output_tokens': 500}
        # gpt-5.6-terra short: 5,000 fresh x $2 + 4,000 cached x $0.20 + 1,000 written x $2.50 + 2,000 out x $12, per 1M.
        usd, tier = cost(self.PRICING, 'gpt-5.6-terra', tokens)
        self.assertEqual(tier, 'short')
        self.assertAlmostEqual(usd, (5_000 * 2 + 4_000 * 0.2 + 1_000 * 2.5 + 2_000 * 12) / 1e6)
        self.assertEqual(cost(self.PRICING, 'gpt-5.6-terra', dict(tokens, input_tokens=300_000))[1], 'long')
        self.assertEqual(cost(self.PRICING, 'unknown-model', tokens), (None, 'unpriced'))

    def test_promotional_price_goes_stale(self):
        from datetime import date
        self.assertFalse(stale(self.PRICING, 'gpt-5.6-sol', date(2026, 11, 30)))
        self.assertTrue(stale(self.PRICING, 'gpt-5.6-sol', date(2026, 12, 1)))
        self.assertFalse(stale(self.PRICING, 'gpt-5.6-terra', date(2030, 1, 1)))

    def test_ledger_appends_rows_across_runs(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'cost_ledger.tsv'
            first = Ledger(path, self.PRICING, 'gpt-5.6-terra', 'medium')
            first.record('a', 'written', {'input_tokens': 100_000}, 1.0)  # $2 per 1M -> $0.20
            first.record('b', 'failed', None, 0.5)
            Ledger(path, self.PRICING, 'no-price', 'low').record('c', 'written', {'output_tokens': 10}, 1.0)
            lines = path.read_text().splitlines()
            self.assertEqual(len(lines), 4)
            self.assertTrue(lines[0].startswith('run_id\ttimestamp_utc\ttrial'))
            self.assertEqual(ledger_total(path)[0], 3)
            self.assertAlmostEqual(ledger_total(path)[1], 0.2)
            self.assertEqual(first.calls, 2)
            self.assertAlmostEqual(first.cost, 0.2)


if __name__ == '__main__':
    unittest.main()

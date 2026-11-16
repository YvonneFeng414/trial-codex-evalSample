"""Run with python3 -m unittest test_create_b_naive."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import create_b_naive as b
from tools.codex_cli import CodexError

PROMPT = b.load_prompt(b.DEFAULT_PROMPT.read_text(encoding='utf-8'))
INPUT = '''# Evaluation Input

## 1.1 Background and Rationale

Drug X versus placebo in 300 adults.

## 2.3 Sample Size

### Planned Sample Size

300 patients; alpha 0.05.
'''
USAGE = {'input_tokens': 2_000, 'cached_input_tokens': 0, 'cache_write_input_tokens': 0,
         'output_tokens': 4_000, 'reasoning_output_tokens': 500}


def output(*extra):
    """A compliant output: every framework heading, one labelled bullet per subsection, the input's numbers."""
    lines = []
    for heading in PROMPT['headings']:
        lines.append(heading)
        if heading.startswith('###'):
            lines.append('- [Proposed] Content. Rationale: common practice.')
    lines[2:2] = ['[Provided] 300 adults; 300 patients; alpha 0.05.', *extra]
    return '\n\n'.join(lines) + '\n'


class PromptTests(unittest.TestCase):
    def test_prompt_split(self):
        self.assertEqual(PROMPT['headings'][:2], [b.TITLE, '## 1. Introduction'])
        self.assertEqual(len(PROMPT['headings']), 29)
        self.assertNotIn('PASTE', PROMPT['instructions'])
        self.assertTrue(PROMPT['instructions'].rstrip().endswith('Return only the completed Markdown framework.'))
        message = b.message(PROMPT, INPUT)
        self.assertTrue(message.startswith('## Evaluation Input\n\n# Evaluation Input\n'))
        self.assertNotIn('PASTE', message)


class ValidateTests(unittest.TestCase):
    def test_compliant_output_passes(self):
        self.assertEqual(b.validate(output('**Lead-in**', '- Inclusion criteria:'), PROMPT, INPUT), [])
        self.assertEqual(b.validate(output().replace('## 1. Intro', '## 1\\. Intro'), PROMPT, INPUT), [])
        self.assertEqual(b.validate(b.clean('Here:\n```markdown\n' + output() + '```'), PROMPT, INPUT), [])

    def test_rule_breaks_are_reported(self):
        check = lambda text: ' '.join(b.validate(text, PROMPT, INPUT))
        self.assertIn('Section titles differ', check(output().replace('### 2.2 Randomization', '### 2.2 Randomisation')))
        self.assertIn('no evidence label', check(output('Unlabelled statement.')))
        self.assertIn('more than one', check(output('[Provided] 300 adults [Proposed] and a model.')))
        self.assertIn('[Provided] statements have numbers', check(output('[Provided] 999 patients.')))
        self.assertIn('not preserved', check(output().replace('alpha 0.05', 'alpha')))
        self.assertIn('URL', check(output('[Proposed] See https://example.org.')))
        self.assertTrue(check('Some preamble\n' + output()).startswith('Output does not start'))

    def test_table_header_is_exempt_and_rows_need_labels(self):
        table = '| Item | Status |\n|---|---|\n| Alpha 0.05 | [Provided] |\n| Power | 90% |'
        self.assertIn("'| Power | 90% |'", ' '.join(b.validate(output(table), PROMPT, INPUT)))


class RunTests(unittest.TestCase):
    def run_main(self, out, reply=None, error=None, *flags):
        class Fake:
            model, effort, calls, note = 'gpt-5.6-terra', 'medium', 1, None

            def __init__(self, *args, **kwargs):
                pass

            def run(self, message):
                if error:
                    raise error
                return reply, USAGE, 3.0

        source = out / 'in' / 'input_trial.md'
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(INPUT)
        argv = ['create_b_naive.py', str(source.parent), '--out', str(out / 'b'), '--model', 'gpt-5.6-terra', *flags]
        with patch.object(b, 'Codex', Fake), patch.object(sys, 'argv', argv), patch('builtins.print'):
            return b.main()

    def test_every_call_is_ledgered(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            self.assertEqual(self.run_main(out, output(), None, '--validate'), 0)
            self.assertTrue((out / 'b/trial.md').exists())
            self.assertIn('trial.md\tpass', (out / 'b/format_check.tsv').read_text())
            self.assertEqual(self.run_main(out, None, CodexError('boom', {'input_tokens': 10}, 1.0), '--validate'), 1)
            self.assertFalse((out / 'b/trial.md').exists())
            rows = (out / 'b/cost_ledger.tsv').read_text().splitlines()
            self.assertEqual(len(rows), 3)
            self.assertEqual([row.split('\t')[2:6:3] for row in rows[1:]], [['trial', 'written'], ['trial', 'failed']])
            self.assertIn('trial.md\tmissing\tboom', (out / 'b/format_check.tsv').read_text())

    def test_format_check_is_off_by_default(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            self.assertEqual(self.run_main(out, output('Unlabelled statement.')), 0)
            self.assertTrue((out / 'b/trial.md').exists())
            self.assertFalse((out / 'b/format_check.tsv').exists())


if __name__ == '__main__':
    unittest.main()

"""Isolated `codex exec` call whose only instructions are a given system prompt."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import tempfile
import threading
import time

from tools.cost import usage as parse_usage


class CodexError(ValueError):
    """A failed call; `usage` and `elapsed` say what it consumed, since a failed call can still be billed."""

    def __init__(self, message, usage=None, elapsed=0.0):
        super().__init__(message)
        self.usage, self.elapsed = usage, elapsed


def errors(jsonl):
    """Error messages from Codex's --json events (with --json, Codex reports API errors on stdout)."""
    found = []
    for line in jsonl.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if isinstance(event, dict) and event.get('type') in ('error', 'turn.failed'):
            found.append(str(event.get('message') or (event.get('error') or {}).get('message') or ''))
    return [m for m in found if m]


# Codex features that add tools or developer messages; turned off so the prompt file is the only instruction.
DISABLED_FEATURES = ('plugins', 'multi_agent', 'shell_tool', 'unified_exec', 'apps', 'goals', 'sleep_tool', 'skill_search',
                     'tool_suggest', 'browser_use', 'computer_use', 'image_generation', 'view_image')
CONFIG = {'web_search': 'disabled', 'include_permissions_instructions': False, 'include_environment_context': False,
          'include_apps_instructions': False, 'include_collaboration_mode_instructions': False,
          'project_doc_max_bytes': 0, 'skills.include_instructions': False}
# Model-catalog fields that add multi-agent/plugin messages and the code-mode exec and apply_patch tools.
CATALOG = {'multi_agent_version': None, 'include_skills_usage_instructions': False, 'include_plugin_usage_instructions': False,
           'include_apps_usage_instructions': False, 'tool_mode': 'direct', 'apply_patch_tool_type': None}


def catalog_entry(models, model):
    """(entry, base slug) for a model; base is None when Codex's list has the model itself.

    Codex's list (models_cache.json) holds only the models Codex ships settings for, but the API key can call
    others. Those get a copy of the closest listed model's entry: the visible one whose name shares the longest
    prefix, ties going to Codex's own ranking (e.g. gpt-6.1-sol borrows gpt-6-luna's).
    """
    for entry in models:
        if entry.get('slug') == model:
            return entry, None
    named = [m for m in models if m.get('slug')]
    listed = [m for m in named if m.get('visibility') != 'hide'] or named
    if not listed:
        raise KeyError(model)
    base = max(listed, key=lambda m: (len(os.path.commonprefix([m['slug'], model])), -m.get('priority', 0)))
    return {**base, 'slug': model, 'display_name': model}, base['slug']


class Codex:
    """Codex CLI call whose only instructions are the system prompt; the prompt argument is the user message.

    `instructions` is a prompt file path, or the prompt text itself (str).
    """

    def __init__(self, home, model, timeout, instructions, effort=None):
        self.home, self.model, self.timeout = home, model, timeout
        self.calls, self.lock = 0, threading.Lock()
        self.workspace = tempfile.TemporaryDirectory(prefix='codex-catalog-')
        self.catalog = Path(self.workspace.name) / 'catalog.json'
        if isinstance(instructions, str):
            path = Path(self.workspace.name) / 'instructions.md'
            path.write_text(instructions, encoding='utf-8')
            instructions = path
        try:
            models = json.loads((home / 'models_cache.json').read_text(encoding='utf-8'))['models']
            entry, self.base = catalog_entry(models, model)
        except (OSError, ValueError, KeyError, TypeError) as error:
            raise CodexError(f'No usable model list in {home / "models_cache.json"}; run codex once to create it') from error
        # Printed by the callers, so a run's log says when a model's settings were borrowed.
        self.note = self.base and (f"note: {model} is not in Codex's model list; using {self.base}'s settings "
                                   '(context window, effort levels, truncation)')
        levels = [level['effort'] for level in entry.get('supported_reasoning_levels', [])]
        self.effort = effort or entry.get('default_reasoning_level')
        if self.effort not in levels:
            source = f'{model} (settings from {self.base})' if self.base else model
            raise CodexError(f'Effort {self.effort!r} is not supported by {source}; choose from {", ".join(levels)}')
        self.catalog.write_text(json.dumps({'models': [{**entry, **CATALOG}]}), encoding='utf-8')
        config = {**CONFIG, 'model_catalog_json': str(self.catalog), 'model_instructions_file': str(instructions.resolve()),
                  'model_reasoning_effort': self.effort}
        # Codex ignores OPENAI_BASE_URL in the environment (tools/env.sh sets it from BASE_URL), so pass it as config.
        if os.environ.get('OPENAI_BASE_URL'):
            config['openai_base_url'] = os.environ['OPENAI_BASE_URL']
        self.options = [x for f in DISABLED_FEATURES for x in ('--disable', f)]
        self.options += [x for k, v in config.items() for x in ('-c', f'{k}={json.dumps(v)}')]

    def __call__(self, prompt, schema=None):
        """Return the last message; with a JSON schema, Codex constrains the reply to it."""
        return self.run(prompt, schema)[0]

    def run(self, prompt, schema=None):
        """(last message, token usage, elapsed seconds) of one call."""
        with tempfile.TemporaryDirectory(prefix='codex-run-') as directory:
            result = Path(directory) / 'result.md'
            extra = []
            if schema is not None:
                (Path(directory) / 'schema.json').write_text(json.dumps(schema), encoding='utf-8')
                extra = ['--output-schema', str(Path(directory) / 'schema.json')]
            command = ['codex', 'exec', '--json', '--strict-config', '--sandbox', 'read-only', '--ephemeral',
                       '--skip-git-repo-check', '--cd', directory, '--model', self.model, *self.options, *extra,
                       '--output-last-message', str(result), '-']
            env = os.environ.copy()
            if self.home:
                env['CODEX_HOME'] = str(self.home)
            with self.lock:
                self.calls += 1
            start = time.monotonic()
            try:
                run = subprocess.run(command, input=prompt, text=True, capture_output=True,
                                     env=env, timeout=self.timeout)
            except subprocess.TimeoutExpired as error:
                stdout = error.stdout.decode() if isinstance(error.stdout, bytes) else (error.stdout or '')
                raise CodexError(f'Codex call failed: {error}', parse_usage(stdout), time.monotonic() - start) from error
            except OSError as error:
                raise CodexError(f'Codex call failed: {error}', None, time.monotonic() - start) from error
            elapsed, used = time.monotonic() - start, parse_usage(run.stdout)
            if run.returncode:
                detail = '; '.join(errors(run.stdout)) or run.stderr[-2000:]
                raise CodexError(f'Codex exited {run.returncode}: {detail[-2000:]}', used, elapsed)
            try:
                return result.read_text(encoding='utf-8'), used, elapsed
            except OSError as error:
                raise CodexError('Codex returned no output', used, elapsed) from error

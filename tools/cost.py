"""Token usage from `codex exec --json`, its cost from tools/pricing.json, and an append-only cost ledger."""
from __future__ import annotations

import csv
from datetime import date, datetime, timezone
import json
import os
from pathlib import Path
import threading

PRICING = Path(__file__).resolve().parent / 'pricing.json'
# Codex token counts: cached and cache-write tokens are part of input_tokens; reasoning tokens are part of output_tokens.
TOKENS = ('input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens', 'reasoning_output_tokens')
COLUMNS = ('run_id', 'timestamp_utc', 'trial', 'model', 'effort', 'status', *TOKENS, 'cost_usd', 'price_tier',
           'pricing_as_of', 'elapsed_s')


def usage(jsonl):
    """Sum the usage of every turn.completed event in Codex's --json stdout."""
    total = dict.fromkeys(TOKENS, 0)
    for line in jsonl.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if isinstance(event, dict) and event.get('type') == 'turn.completed':
            for name in TOKENS:
                total[name] += int((event.get('usage') or {}).get(name) or 0)
    return total


def load_pricing(path=PRICING):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def stale(pricing, model, today=None):
    """True when the model's rate is promotional and past its valid_until date."""
    until = pricing['models'].get(model, {}).get('valid_until')
    return bool(until) and (today or date.today()) > date.fromisoformat(until)


def cost(pricing, model, tokens):
    """(USD, 'short' | 'long') for one call, or (None, 'unpriced') when the model has no rates."""
    entry = pricing['models'].get(model)
    if entry is None:
        return None, 'unpriced'
    tier = 'long' if tokens['input_tokens'] > pricing['long_context_input_tokens'] else 'short'
    rate = entry[tier]
    cached, written = tokens['cached_input_tokens'], tokens['cache_write_input_tokens']
    fresh = max(tokens['input_tokens'] - cached - written, 0)
    total = (fresh * rate['input'] + cached * rate['cached_input'] + written * rate['cache_write']
             + tokens['output_tokens'] * rate['output']) / pricing['unit_tokens']
    return total, tier


class Ledger:
    """Append-only TSV, one row per Codex call; safe across threads, never rewritten."""

    def __init__(self, path, pricing, model, effort):
        self.path, self.pricing, self.model, self.effort = Path(path), pricing, model, effort
        self.run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + f'-{os.getpid()}'
        self.lock = threading.Lock()
        self.calls, self.cost, self.unpriced = 0, 0.0, 0
        self.tokens = dict.fromkeys(TOKENS, 0)

    def record(self, trial, status, tokens, elapsed):
        """Append one call; returns its cost in USD (None if the model is unpriced)."""
        tokens = {name: int(tokens.get(name, 0)) for name in TOKENS} if tokens else dict.fromkeys(TOKENS, 0)
        usd, tier = cost(self.pricing, self.model, tokens)
        row = {'run_id': self.run_id, 'timestamp_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
               'trial': trial, 'model': self.model, 'effort': self.effort, 'status': status, **tokens,
               'cost_usd': '' if usd is None else f'{usd:.6f}', 'price_tier': tier,
               'pricing_as_of': self.pricing.get('as_of', ''), 'elapsed_s': f'{elapsed:.1f}'}
        with self.lock:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            new = not self.path.exists() or self.path.stat().st_size == 0
            with self.path.open('a', encoding='utf-8', newline='') as handle:
                writer = csv.DictWriter(handle, COLUMNS, delimiter='\t', lineterminator='\n')
                if new:
                    writer.writeheader()
                writer.writerow(row)
            self.calls += 1
            for name in TOKENS:
                self.tokens[name] += tokens[name]
            if usd is None:
                self.unpriced += 1
            else:
                self.cost += usd
        return usd


def ledger_total(path):
    """(calls, USD) over every run recorded in a ledger file."""
    try:
        with Path(path).open(encoding='utf-8', newline='') as handle:
            rows = list(csv.DictReader(handle, delimiter='\t'))
    except OSError:
        return 0, 0.0
    return len(rows), sum(float(r['cost_usd']) for r in rows if r.get('cost_usd'))


def price_warning(pricing, model, path=PRICING):
    """A warning when the model has no price or its promotional price has expired; '' otherwise."""
    if model not in pricing['models']:
        return f'warning: {model} has no price in {path}; the ledger records its tokens with no cost'
    if stale(pricing, model):
        return (f"warning: the {model} price in {path} was promotional until "
                f"{pricing['models'][model]['valid_until']}; update it from {pricing['source']}")
    return ''


def report(ledger):
    """Lines describing this run's cost and the ledger's running total; empty when no call was made."""
    if not ledger or not ledger.calls:
        return []
    tokens = ledger.tokens
    unpriced = f' + {ledger.unpriced} unpriced calls' if ledger.unpriced else ''
    total_calls, total_cost = ledger_total(ledger.path)
    return [f"cost this run: ${ledger.cost:.4f}{unpriced} ({tokens['input_tokens']:,} input tokens, "
            f"{tokens['cached_input_tokens']:,} cached; {tokens['output_tokens']:,} output, "
            f"{tokens['reasoning_output_tokens']:,} reasoning)",
            f'ledger {ledger.path}: ${total_cost:.4f} over {total_calls} calls']

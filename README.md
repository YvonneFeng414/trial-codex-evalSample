# Setup: OpenAI API key

All Codex calls bill an OpenAI API key. Put it in `.env` at the repository root
(git-ignored):

```sh
CODEX_API_KEY=sk-...
# BASE_URL=https://...   # optional API base URL, e.g. a proxy
```

Every bash script sources `tools/env.sh`, which loads `.env`. Variables already
set in the shell win over `.env`. `codex exec` reads `CODEX_API_KEY`, and it
takes precedence over any ChatGPT login stored in `.codex-home`. `BASE_URL`
reaches Codex as `-c openai_base_url=...`, because Codex ignores base-URL
environment variables.
`tools/create_inputs.sh` and `create_b_naive.sh` stop with an
error when no key is set (except with `--dry-run`), so a run never silently
falls back to a ChatGPT login. `bash tools/codex_init.sh` (default `--api-key`)
also stores the key as the `.codex-home` login, for Codex commands that don't
read the variable. Running the Python modules directly skips `.env`, so
export `CODEX_API_KEY` yourself.

# Markdown preprocessing

Remove parenthesized `Source:` references (including their Markdown emphasis)
while preserving ordinary parentheses and the raw files:

```sh
python3 tools/preprocess_md.py
```

Reads all `.md` files recursively from `smoke_run_data/raw` and writes cleaned
copies to `smoke_run_data/processed`, preserving filenames and subdirectories.
Existing output files are replaced when rerun.

For other directories:

```sh
python3 tools/preprocess_md.py path/to/raw --output path/to/processed
```

## Create Evaluation Inputs

```sh
bash tools/create_inputs.sh --report
```

Reads every protocol/SAP in `smoke_run_data/a` and writes
`input_<source-stem>.md` to `smoke_run_data/inputs`, one Codex call per trial,
following `system_prompts/Input_extraction_prompt.md`. The prompt file is the
single source of the rules: the code reads its allowed sections, output
template and benchmark placeholder from it, so edits to the prompt carry over.
`python3 -m tools.create_inputs` is equivalent.

Each call is a read-only, ephemeral `codex exec` (`tools/codex_cli.py`, shared
with B_naive). The prompt up to `## Benchmark` replaces Codex's built-in
instructions. The user message is the `## Benchmark` block with the placeholder
replaced by the source.

What code enforces around the model:

- **Before the call:** only the prompt's allowed sections are sent (§1.1, §1.2,
  §2.1–2.4, §2.6, eligibility). They are matched by title, since eligibility is
  §4.2 in these SAPs, and each is renumbered to the prompt's number. Interim
  analyses, outcome definitions (§5.1/§5.2), analysis methods and every other
  section never reach the model. `(Source: …)` citations are removed first.
- **After the call:** the reply, minus any code fence or preamble and any
  template guidance echoed back, must pass these checks:
  - the template's headings exactly, in order (`####` subheadings may be added);
  - no empty subsection, and the `**Method**` field under 2.2;
  - `P1, P2, …` labels under Primary and `S1, S2, …` under
    Secondary/Exploratory Objectives, without gaps (or "Not specified");
  - no URL, DOI, filename, page number, citation or source note;
  - every number found in the allowed source sections;
  - no section written entirely as "Not specified" when its source section has
    content.

These checks run only with `--validate` (off by default; without it every reply
is saved as `input_<stem>.md`). With `--validate`, a reply that fails is saved as
`input_<stem>.md.rejected` with its problems reported, and any earlier
`input_<stem>.md` is removed. The model's judgement
calls cannot be checked by code: Not specified vs. Not applicable, objective-level
outcomes, and formal vs. operational interim reviews. They rest on the prompt.

Options: an input directory or single Markdown file, `--out DIR`,
`--prompt FILE`, `--model MODEL` (default `gpt-5.6-sol`), `--effort LEVEL`,
`--timeout SECONDS`, `--jobs N` (default 4), `--codex-home DIR`,
`--validate` (run the checks above), `--skip-existing` (keep existing outputs
instead of calling Codex; re-checked with `--validate`),
`--dry-run` (report the sections found; no Codex calls or writes),
`--report` (one JSON record per trial, with its usage and cost), `--ledger FILE`
and `--pricing FILE`. Any rejected or failed trial gives a
nonzero exit status. Tests: `python3 -m unittest tools.test_create_inputs`.

**Cost ledger.** Every Codex call appends one row to
`smoke_run_data/inputs/cost_ledger.tsv` (`--ledger FILE` to change). This
includes rejected and failed calls, since they can still be billed. Columns:
`run_id`, `timestamp_utc`, `trial`, `model`, `effort`, `status`,
`input_tokens`, `cached_input_tokens`, `cache_write_input_tokens`,
`output_tokens`, `reasoning_output_tokens`, `cost_usd`, `price_tier`
(`short`/`long` context, or `unpriced`), `pricing_as_of` and `elapsed_s`.
Tokens come from `codex exec --json` (`turn.completed` usage). Cached and
cache-write tokens are part of the input count, and reasoning tokens are part
of the output count, so cost = uncached input × input rate + cached × cached
rate + cache writes × write rate + output × output rate. Rates are USD per 1M
tokens from `tools/pricing.json` (`--pricing FILE`), copied from OpenAI's
standard-tier price page on 2026-11-04. The long-context rates apply above
272K input tokens. A run prints its own cost and the ledger's running total.
It warns when the model has no price (tokens are still recorded) or when a
promotional rate has expired (gpt-5.6-sol's ends 2026-11-30). Update
`tools/pricing.json` when prices change; existing rows keep the cost they
were billed at. Rows are only ever appended, never rewritten.

## Create naive-baseline protocols/SAPs (B_naive)

```sh
bash create_b_naive.sh
```

Reads `smoke_run_data/inputs/input_*.md` (Evaluation Inputs) and writes one
predicted protocol and statistical analysis framework per trial to
`smoke_run_data/b_naive/<source-stem>.md`, matching the reference filenames in
`smoke_run_data/raw`. Each trial is one read-only, ephemeral `codex exec`
call. The rules come from `system_prompts/llm_generation_prompt.md`: everything
before its `## Evaluation Input` heading replaces Codex's built-in instructions
(`model_instructions_file`), and that heading with the placeholder replaced by
the input file is the only user message. Codex's extra developer messages
(permissions, environment, skills, plugins, multi-agent) and its tools (shell,
apply_patch, web search, images) are turned off through `-c` overrides,
`--disable` flags and a trimmed copy of the model's entry from
`.codex-home/models_cache.json`; only the inert `request_user_input` tool
remains. That file lists only the models Codex ships settings for; any other
model your API key can call (e.g. `gpt-6.1-sol`) borrows the entry of the listed
model whose name shares the longest prefix (here `gpt-6-luna`), and the run prints
a `note:` line saying so, since context window, effort levels and truncation then
come from that model. `python3 create_b_naive.py` is equivalent.

There are no retries: each output is written as returned (minus any code fence
or preamble) and then checked against the prompt's rules:

- the section titles, numbering and order of the output framework, exactly
  (Markdown escapes such as `1\.` are ignored; deeper `####` headings are allowed);
- exactly one evidence label (`[Provided]`, `[Derived]`, `[Proposed]` or
  `[Clarification Required]`) on every paragraph, bullet and table row; headings,
  table header rows, bold-only labels and lead-ins ending in a colon are exempt;
- every number in the Evaluation Input appears in the output, and no
  `[Provided]` statement has a number the input does not;
- no citations, URLs, DOIs, filenames, page numbers, source notes or the input
  placeholder.

The prompt's other rules (a rationale for each `[Proposed]` item, the missing
decision for each `[Clarification Required]` item, correct use of `[Derived]`)
need judgment and are not checked by code. The format check runs only with
`--validate` (off by default). Its result is recorded in
`smoke_run_data/b_naive/format_check.tsv` with columns `output`, `format`
(`pass`, `fail` or `missing`) and `detail` (every problem found). A `fail`
output is kept. `missing` means the Codex call itself failed, so no output
exists; only this case gives a nonzero exit status. Rows from earlier runs are
kept and updated by output file, and `--skip-existing --validate` re-checks the
existing outputs without calling Codex.
Each run that writes outputs records its model and effort in `OUT/tag.json`.
If the folder then holds outputs from different settings (e.g. after `--skip-existing`
or a single-input run), the tag becomes `mixed` and lists each run's settings.

**Cost ledger.** Every Codex call, failed ones included, appends one row to
`smoke_run_data/b_naive/cost_ledger.tsv` (`--ledger FILE` to change), with the
same columns and pricing as the input-extraction ledger above; `trial` is the
source stem. A run prints its own cost and the ledger's running total.

Options: an input directory or single `input_*.md` file, `--out DIR`,
`--prompt FILE`, `--tags FILE`, `--model MODEL` (default `gpt-5.6-sol`),
`--effort LEVEL` (reasoning effort, checked against the model's supported
levels; default is the model's own default level, passed explicitly),
`--timeout SECONDS`, `--jobs N` (parallel trials, default 4),
`--validate`, `--skip-existing`, `--dry-run`, `--report`, `--ledger FILE` and
`--pricing FILE`. Tests: `python3 -m unittest test_create_b_naive`.

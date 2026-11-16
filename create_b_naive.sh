#!/usr/bin/env bash
# Draft B_naive from smoke_run_data/inputs/input_*.md with system_prompts/llm_generation_prompt.md.
# Writes smoke_run_data/b_naive/<source-stem>.md, format_check.tsv, tag.json and the append-only
# cost_ledger.tsv (one row per Codex call). Options pass through: bash create_b_naive.sh --help
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"
. "$REPO_DIR/tools/env.sh"  # .env: CODEX_API_KEY (required), BASE_URL; CODEX_HOME defaults to .codex-home
require_api_key "$@"
exec "${PYTHON:-python3}" create_b_naive.py "$@"

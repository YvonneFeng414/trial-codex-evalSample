#!/usr/bin/env bash
set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"
. "$REPO_DIR/tools/env.sh"  # .env: CODEX_API_KEY (required), BASE_URL; CODEX_HOME defaults to .codex-home
require_api_key "$@"
exec "${PYTHON:-python3}" -m tools.create_inputs "$@"

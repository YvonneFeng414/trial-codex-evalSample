#!/usr/bin/env bash

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_CODEX_HOME="$REPO_DIR/.codex-home"
PROJECT_AUTH="$PROJECT_CODEX_HOME/auth.json"
USER_CODEX_AUTH="$HOME/.codex/auth.json"
. "$REPO_DIR/tools/env.sh"  # loads CODEX_API_KEY from .env
MODE="api-key"
FORCE=0
DEVICE_AUTH=0

usage() {
    cat <<'EOF'
Usage: tools/codex_init.sh [--api-key | --login | --copy-current] [--device-auth] [--force]

Initialize this repository's private .codex-home directory.

  --api-key       store CODEX_API_KEY from .env as the login (default)
  --login         sign in interactively with ChatGPT and write a new auth.json
  --copy-current  copy ~/.codex/auth.json instead of signing in
  --device-auth   use a device code so you can select the intended browser account
  --force         replace an existing project auth.json
  -h, --help      show this help
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --api-key) MODE="api-key" ;;
        --login) MODE="login" ;;
        --copy-current) MODE="copy" ;;
        --device-auth) DEVICE_AUTH=1 ;;
        --force) FORCE=1 ;;
        -h|--help) usage; exit 0 ;;
        *) echo "unknown option: $1" >&2; usage >&2; exit 2 ;;
    esac
    shift
done

if [[ "$MODE" == "api-key" ]]; then
    [[ "$DEVICE_AUTH" -eq 0 ]] || { echo "--device-auth cannot be combined with --api-key" >&2; exit 2; }
    [[ -n "${CODEX_API_KEY:-}" ]] || {
        echo "CODEX_API_KEY is not set: add CODEX_API_KEY=<OpenAI API key> to $ENV_FILE or export it" >&2
        exit 1
    }
fi

command -v codex >/dev/null 2>&1 || {
    echo "codex executable not found" >&2
    exit 1
}

umask 077
mkdir -p "$PROJECT_CODEX_HOME"
chmod 700 "$PROJECT_CODEX_HOME"

if [[ ! -e "$PROJECT_CODEX_HOME/config.toml" ]]; then
    : >"$PROJECT_CODEX_HOME/config.toml"
fi
if ! grep -Eq '^[[:space:]]*cli_auth_credentials_store[[:space:]]*=' \
    "$PROJECT_CODEX_HOME/config.toml"; then
    printf '\n%s\n' 'cli_auth_credentials_store = "file"' \
        >>"$PROJECT_CODEX_HOME/config.toml"
fi
chmod 600 "$PROJECT_CODEX_HOME/config.toml"

if [[ -e "$PROJECT_AUTH" && "$FORCE" -ne 1 ]]; then
    echo "project auth already exists: $PROJECT_AUTH" >&2
    echo "re-run with --force to replace it" >&2
    exit 1
fi

if [[ "$MODE" == "copy" ]]; then
    [[ "$DEVICE_AUTH" -eq 0 ]] || {
        echo "--device-auth cannot be combined with --copy-current" >&2
        exit 2
    }
    [[ -f "$USER_CODEX_AUTH" ]] || {
        echo "current file-backed login not found: $USER_CODEX_AUTH" >&2
        echo "use --login instead" >&2
        exit 1
    }
    install -m 600 "$USER_CODEX_AUTH" "$PROJECT_AUTH"
else
    export CODEX_HOME="$PROJECT_CODEX_HOME"
    PREVIOUS_AUTH="$PROJECT_AUTH.previous"
    if [[ -e "$PROJECT_AUTH" ]]; then
        mv "$PROJECT_AUTH" "$PREVIOUS_AUTH"
    fi
    LOGIN_ARGS=(--config 'cli_auth_credentials_store="file"' login)
    if [[ "$DEVICE_AUTH" -eq 1 ]]; then
        LOGIN_ARGS+=(--device-auth)
    fi
    if [[ "$MODE" == "api-key" ]]; then
        # The key goes through stdin, never the command line.
        login() { printf '%s' "$CODEX_API_KEY" | codex "${LOGIN_ARGS[@]}" --with-api-key; }
    else
        login() { codex "${LOGIN_ARGS[@]}"; }
    fi
    if ! login; then
        if [[ -e "$PREVIOUS_AUTH" ]]; then
            mv "$PREVIOUS_AUTH" "$PROJECT_AUTH"
            echo "login failed; restored the previous project auth.json" >&2
        fi
        exit 1
    fi
    if [[ -e "$PREVIOUS_AUTH" ]]; then
        rm -f "$PREVIOUS_AUTH"
    fi
fi

[[ -f "$PROJECT_AUTH" ]] || {
    echo "Codex did not create $PROJECT_AUTH" >&2
    exit 1
}
chmod 600 "$PROJECT_AUTH"

echo "initialized project Codex home: $PROJECT_CODEX_HOME"
CODEX_HOME="$PROJECT_CODEX_HOME" \
    codex --config 'cli_auth_credentials_store="file"' login status

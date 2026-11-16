# Sourced by every bash entry point: loads the repository's .env and sets up Codex to bill the OpenAI API key.
#
#   CODEX_API_KEY   the OpenAI API key, required for Codex calls. `codex exec` reads it, and it takes
#                   precedence over any ChatGPT login stored in CODEX_HOME.
#   BASE_URL        optional API base URL (e.g. a proxy); exported as OPENAI_BASE_URL, which
#                   tools/codex_cli.py passes as `-c openai_base_url=...` (Codex ignores the variable itself).
#
# Values already set in the environment win over .env. Lines are parsed, not executed.

ENV_REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${ENV_FILE:-$ENV_REPO_DIR/.env}"

load_env() {
    local line name value
    [[ -f "$1" ]] || return 0
    while IFS= read -r line || [[ -n "$line" ]]; do
        line="${line%$'\r'}"
        [[ "$line" =~ ^[[:space:]]*(export[[:space:]]+)?([A-Za-z_][A-Za-z0-9_]*)[[:space:]]*=[[:space:]]*(.*)$ ]] || continue
        name="${BASH_REMATCH[2]}"
        value="${BASH_REMATCH[3]}"
        if [[ "$value" =~ ^\"(.*)\"[[:space:]]*$ || "$value" =~ ^\'(.*)\'[[:space:]]*$ ]]; then
            value="${BASH_REMATCH[1]}"
        else
            value="${value%%[[:space:]]#*}"           # trailing comment on an unquoted value
            value="${value%"${value##*[![:space:]]}"}"  # trailing spaces
        fi
        [[ -n "${!name+set}" ]] || export "$name=$value"
    done <"$1"
}

load_env "$ENV_FILE"
export CODEX_HOME="${CODEX_HOME:-$ENV_REPO_DIR/.codex-home}"
if [[ -n "${BASE_URL:-}" ]]; then
    export OPENAI_BASE_URL="${OPENAI_BASE_URL:-$BASE_URL}"
fi

# require_api_key "$@": stop unless an API key is set, so a run never falls back to the stored ChatGPT login.
# --dry-run makes no Codex calls and needs no key.
require_api_key() {
    local arg
    for arg in "$@"; do
        [[ "$arg" == --dry-run ]] && return 0
    done
    if [[ -z "${CODEX_API_KEY:-}" ]]; then
        echo "CODEX_API_KEY is not set: add CODEX_API_KEY=<OpenAI API key> to $ENV_FILE or export it." >&2
        exit 1
    fi
}

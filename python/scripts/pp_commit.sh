#!/usr/bin/env bash

set -euo pipefail

# Usage:
#   bash scripts/pp_commit.sh                 # usa mensaje por defecto con timestamp
#   bash scripts/pp_commit.sh "Alice -> Bob"  # opcional: agrega detalle de pareja
#
# Commits all changes with a default message including timestamp.
# If an argument is provided, it is appended for pair details.

PAIR_DETAIL=${1:-""}

timestamp() {
  date '+%Y-%m-%d %H:%M:%S'
}

echo "[pp_commit] Adding changes..."
git add -A

# Ensure pp_rotate.sh is always executable
chmod +x python/scripts/pp_rotate.sh

DEFAULT_PREFIX="PP rotation"
COMMIT_MSG="${DEFAULT_PREFIX} | $(timestamp)"
if [[ -n "${PAIR_DETAIL}" ]]; then
  COMMIT_MSG+=" | ${PAIR_DETAIL}"
fi

echo "[pp_commit] Committing..."
if ! git commit -m "${COMMIT_MSG}"; then
  echo "[pp_commit] Nothing to commit. Proceeding to push."
fi

# Detect current branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Try to push, if fails, set upstream and push
echo "[pp_commit] Pushing..."
if ! git push origin "$CURRENT_BRANCH"; then
  echo "[pp_commit] Push failed. Trying to set upstream and push..." >&2
  git push --set-upstream origin "$CURRENT_BRANCH" || {
    echo "[pp_commit] Push with upstream also failed. Check your remote/branch permissions." >&2
    exit 1
  }
fi

echo "[pp_commit] Done."

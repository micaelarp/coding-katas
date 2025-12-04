#!/usr/bin/env bash

set -euo pipefail

# Usage:
#   bash scripts/pp_rotate.sh "Optional Message"
#
# Runs tests (via make test), then commits and pushes a standard rotation message.

MESSAGE=${1:-""}

if [[ -z "${MESSAGE}" ]]; then
  read -p "Enter commit message (optional): " MESSAGE
fi

# Cambiar ROOT_DIR para que apunte a la raíz del proyecto
ROOT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)

# Detect current branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Check if branch has upstream
HAS_UPSTREAM=$(git rev-parse --symbolic-full-name --verify @{u} >/dev/null 2>&1 && echo 1 || echo 0)

# Run tests
echo "[pp_rotate] Running tests..."
(
  cd "$ROOT_DIR"
  make test
)

echo "[pp_rotate] Tests passed. Committing rotation..."
(
  cd "$ROOT_DIR"
  COMMIT_DETAILS="PP rotation"
  if [[ -n "${MESSAGE}" ]]; then
    COMMIT_DETAILS="${COMMIT_DETAILS} | ${MESSAGE}"
  fi
  bash python/scripts/pp_commit.sh "${COMMIT_DETAILS}"
)

# Push branch (set upstream if needed)
echo "[pp_rotate] Pushing to remote..."
if [[ "$HAS_UPSTREAM" -eq 0 ]]; then
  git push --set-upstream origin "$CURRENT_BRANCH"
else
  git push origin "$CURRENT_BRANCH"
fi

echo "[pp_rotate] Rotation complete."

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

echo "[pp_rotate] Rotation complete."

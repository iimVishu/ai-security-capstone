#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

: "${JWT_SECRET:?Set JWT_SECRET in the environment before starting the app.}"
export FLASK_APP=app.py
export FLASK_ENV=production
python3 app.py

#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
mkdir -p artifacts

if ! command -v pip-audit >/dev/null 2>&1; then
  echo "pip-audit is required but not installed." >&2
  exit 1
fi

pip-audit -r requirements.txt --format json > artifacts/pip_audit_before.json || true
pip-audit -r requirements_pinned.txt --format json > artifacts/pip_audit_after.json || true

python3 - <<'PY'
import json
from pathlib import Path

for name in ["before", "after"]:
    path = Path("artifacts") / f"pip_audit_{name}.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"dependencies": []}
    vuln_counts = {"critical": 0, "high": 0, "medium": 0, "low": 0, "total": 0}
    for dep in data.get("dependencies", []):
        for vuln in dep.get("vulns", []):
            severity = str(vuln.get("severity", "")).lower()
            if severity in {"critical", "high", "medium", "low"}:
                vuln_counts[severity] += 1
            vuln_counts["total"] += 1
    summary = Path("artifacts") / f"pip_audit_{name}_summary.json"
    summary.write_text(json.dumps({"counts": vuln_counts}, indent=2), encoding="utf-8")
    print(f"{name}: {json.dumps(vuln_counts, sort_keys=True)}")
PY

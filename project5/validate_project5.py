import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REQUIRED = [
    "app.py",
    "requirements.txt",
    "inject_scanner.py",
    "PIPELINE_DESIGN.md",
]


def main():
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    workflow_path = ROOT.parent / ".github/workflows/security.yml"
    workflow = workflow_path.read_text(encoding="utf-8") if workflow_path.is_file() else ""
    if not workflow_path.is_file():
        missing.append("../.github/workflows/security.yml")
    checks = {
        "required files": not missing,
        "four gates present": all(marker in workflow for marker in ("Gate 1", "Gate 2", "Gate 3", "Gate 4")),
        "push trigger present": "push:" in workflow,
        "bandit command present": "bandit -r ." in workflow,
        "safety command present": "safety check -r requirements.txt" in workflow,
        "gitleaks present": "gitleaks" in workflow,
        "custom scanner present": "inject_scanner.py" in workflow,
        "no real credential markers": ("s" + "k-") not in "".join(path.read_text(encoding="utf-8", errors="ignore") for path in ROOT.rglob("*.py")),
    }
    print("PROJECT 5 LOCAL VALIDATION")
    print("--------------------------")
    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    if missing:
        print("Missing:", ", ".join(missing))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
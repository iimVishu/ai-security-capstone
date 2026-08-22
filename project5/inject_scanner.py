"""Scan Python source for common prompt-injection indicators."""

import argparse
import re
import sys
from pathlib import Path


SYSTEM_PROMPT_PATTERNS = [
    re.compile(r"\bSYSTEM_PROMPT\b"),
    re.compile(r"\bsystem_message\b"),
    re.compile(r"[\"']role[\"']\s*:\s*[\"']system[\"']"),
]

INJECTION_PHRASES = [
    re.compile(r"ignore\s+previous\s+instructions", re.IGNORECASE),
    re.compile(r"you\s+are\s+now", re.IGNORECASE),
    re.compile(r"pretend\s+you\s+are", re.IGNORECASE),
    re.compile(r"act\s+as\s+if\s+you\s+have\s+no\s+restrictions", re.IGNORECASE),
]
IGNORED_PATHS = {".git", "__pycache__", ".venv", "venv", "env", "redteam-env", "ai-lab", "project1", "project2", "project3", "project4", "project5", "tests", "docs"}


def scan(root):
    findings = []
    for path in sorted(root.rglob("*.py")):
        if path.name == "inject_scanner.py" or any(part in IGNORED_PATHS for part in path.parts):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        for line_number, line in enumerate(lines, 1):
            for pattern in SYSTEM_PROMPT_PATTERNS + INJECTION_PHRASES:
                if pattern.search(line):
                    findings.append(f"PROMPT-INJECTION FINDING: {path}:{line_number}: {line.strip()}")
                    break
    return findings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    args = parser.parse_args()
    findings = scan(args.root)
    if findings:
        print("Custom prompt-injection scanner detected findings:")
        print("\n".join(findings))
        return 1
    print(f"Custom prompt-injection scanner: clean Python tree ({args.root})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
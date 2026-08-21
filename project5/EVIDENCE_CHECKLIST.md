# Project 5 Evidence Checklist

| ID | Required evidence | Suggested filename | Status |
|---|---|---|---|
| SS1 | GitHub repository page showing Project 5 and `.github/workflows/` | `ss1-repository.png` | Manual after push |
| SS2 | `security.yml` showing all four sequential gates | `ss2-workflow.png` | Manual after push |
| SS3 | `inject_scanner.py` showing `SYSTEM_PROMPT_PATTERNS` and `INJECTION_PHRASES` | `ss3-scanner.png` | Manual |
| SS4 | Failing GitHub Actions run with at least two red gate jobs | `ss4-failing-pipeline.png` | Requires controlled fail commit |
| SS5 | Expanded Bandit log with vulnerable file and line | `ss5-bandit-failure.png` | Requires controlled fail commit |
| SS6 | Expanded Gitleaks log with fake pattern and file | `ss6-gitleaks-failure.png` | Requires controlled fail commit |
| SS7 | Passing GitHub Actions run with all applicable gates green | `ss7-passing-pipeline.png` | Manual after push |
| SS8 | Failing and fixed commit/diff comparison | `ss8-fail-fix-diff.png` | Requires controlled fail/fix history |

No screenshots are claimed by local automation. Capture SS1, SS2, SS4, SS5, SS6, SS7, and SS8 in GitHub after pushing the clean and controlled test commits.
# Project 5 - DevSecOps Pipeline Design

## Purpose

The workflow in `.github/workflows/security.yml` runs on every push and gates the clean Project 5 Python demo before it can be treated as deployable. Jobs use `needs` so the four stages are sequential.

## Gates

### Gate 1 - Bandit SAST

Runs `bandit -r .` recursively in Project 5. Bandit reports unsafe Python patterns such as use of `eval`; the command exits non-zero when findings are present and includes file and line information.

### Gate 2 - Safety Dependency Scan

Installs Safety and runs `safety check -r requirements.txt` against the Project 5 dependency file. A non-zero result blocks the later gates; Critical and High CVE findings therefore fail the pipeline.

### Gate 3 - Gitleaks

Runs the Gitleaks GitHub Action against repository history and content. A deliberately fake API key can be used only in a temporary controlled fail-test commit; no real credential belongs in the repository.

### Gate 4 - Custom Prompt Injection Scanner

`inject_scanner.py` recursively checks Python files for named system-prompt and prompt-injection patterns. It prints each filename and line number and exits 1 when a finding is detected. The scanner excludes itself to avoid matching its own documented pattern lists.

## Controlled Fail and Fix Evidence

The clean working tree intentionally contains no fake secret, unsafe `eval`, hardcoded system prompt, or unconfirmed vulnerable dependency. The assignment's failing state must be created on a temporary branch or commit after the exact vulnerable dependency/version is confirmed. The corresponding fixes should then be committed separately and demonstrated in GitHub Actions.

The exact vulnerable dependency/version for the deliberate failing commit remains unconfirmed. Do not invent it; the clean pipeline and Gate 2 implementation are complete.

See `FAIL_TEST_PLAN.md` for the controlled fail/fix sequence and `EVIDENCE_CHECKLIST.md` for SS1-SS8 capture requirements.

## Security Value

Running these checks at push time gives developers feedback before insecure code reaches a release path. The failing state demonstrates detection; the fixed state demonstrates remediation without weakening the gates.
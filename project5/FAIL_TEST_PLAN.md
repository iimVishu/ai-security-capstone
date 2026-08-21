# Controlled Failing-State Plan

The clean Project 5 tree contains no deliberate vulnerabilities. Create the failing state only on a temporary branch or commit for evidence, then revert or fix it before the passing commit.

## Required simultaneous changes

1. Add `config.py` containing the clearly fake value `FAKE_API_KEY = "sk-test-000000000000000000000000000000000000000000000000"`; it is never a real credential.
2. Add `Django==2.2.0`, an intentionally old Django release selected for the controlled Safety failure test because it has known high-severity security advisories. Do not use this dependency in the clean fix state.
3. Add a harmless demo `eval()` call to the application so Bandit reports the file and line.
4. Add a hardcoded `SYSTEM_PROMPT` variable to a Python application so the custom scanner reports it.

## Evidence sequence

```bash
git switch -c project5-controlled-fail
# Apply all four confirmed changes, plus the confirmed dependency/version.
git add project5
git commit -m "Project 5 controlled failing security state"
git push -u origin project5-controlled-fail
```

Capture SS4, SS5, and SS6 from the resulting GitHub Actions run. Then replace the fake key with `os.environ.get(...)`, replace `eval()` with a safe implementation, move the prompt to configuration, and upgrade the confirmed dependency. Commit the clean fix and capture SS7 and SS8.

Do not push a failing state until the dependency/version requirement is confirmed. Do not use real credentials or disable any gate.
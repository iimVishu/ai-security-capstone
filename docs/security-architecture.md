# Security Architecture

### 1. Authentication
File: app.py
Function: require_jwt()
Threat mitigated: unauthenticated access to /chat and token misuse
Implementation: The route reads the Authorization header only, expects the Bearer prefix, validates the JWT with PyJWT using the secret from the environment, and rejects missing, invalid or expired tokens with HTTP 401 before any model call is attempted.
Verification: The test suite exercises the valid, missing, invalid, and expired JWT paths in tests/test_security_app.py.

### 2. Input Validation
File: project2/validate.py
Function: validate_input(prompt)
Threat mitigated: prompt injection and encoded instruction payloads reaching the model
Implementation: The validator enforces the existing 500-character length constraint, matches the repository’s injection patterns, and rejects long Base64-like strings before the request reaches Ollama.
Verification: tests/test_security_app.py covers both allowed prompts and the five malicious prompt patterns while asserting HTTP 400 for rejected payloads.

### 3. Output Scanning
File: project2/validate.py
Function: scan_output(response)
Threat mitigated: disclosure of protected model instructions or unsafe output content
Implementation: The scanner checks for protected patterns, including system-prompt references and unsafe output signals, and blocks the response before it reaches the client.
Verification: tests/test_security_app.py verifies the safe-response path and the blocked protected-output path.

### 4. Dependency Security
File: requirements.txt; requirements_pinned.txt; scripts/audit_dependencies.sh
Function: pip-audit and pinned dependency verification
Threat mitigated: vulnerable third-party dependencies reaching production or the CI pipeline
Implementation: The repository keeps an unpinned baseline file and a hardened exact-pinned file, then runs pip-audit against each set to record machine-readable JSON in artifacts/ and summarize known vulnerabilities by severity when available.
Verification: The audit script writes artifacts/pip_audit_before.json and artifacts/pip_audit_after.json, and the unit tests assert the pinned file uses exact == syntax only.

### 5. CI/CD Pipeline
File: .github/workflows/security.yml
Function: gate-1-bandit, gate-2-safety, gate-3-gitleaks, gate-4-prompt-scanner
Threat mitigated: insecure code, vulnerable dependencies, leaked secrets, and prompt-injection policy violations entering the deliverable branch
Implementation: The workflow runs Bandit, Safety, Gitleaks, and the existing custom prompt-injection scanner in sequence. Any failure stops the pipeline before deployment.
Verification: The workflow is defined in .github/workflows/security.yml and the repository includes the custom scanner in project5/inject_scanner.py.

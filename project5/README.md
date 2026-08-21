# Project 5 - AI Security DevSecOps Pipeline

This directory contains a clean Python demo and a GitHub Actions pipeline with four sequential security-gate jobs. Gate 2 runs the required Safety dependency scan.

The workflow is at the repository-level path `.github/workflows/security.yml`, which is required for GitHub Actions discovery.

## Local checks

```bash
cd project5
python3 -m py_compile app.py inject_scanner.py validate_project5.py
bandit -r .
safety check -r requirements.txt
python3 inject_scanner.py .
python3 validate_project5.py
```

The clean tree is designed to pass the applicable local checks. Do not add a real secret or leave vulnerable demo code in the clean branch.
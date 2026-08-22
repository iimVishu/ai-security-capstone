# Project 6 - Full Penetration Test on an AI-Powered Web Application

This directory organizes the authorized local-only Project 6 assessment for DVWA and the Project 1 Flask AI application.

## Current environment

- Project 1 virtual environment exists with Flask `3.1.3` and Requests `2.32.5`.
- Project 1 is configured for `127.0.0.1:5000` but is currently stopped.
- DVWA is not installed or running.
- Nmap and Dirb are installed. Nikto and ZAP are not installed. Burp Suite is installed.

## Start Project 1

```bash
cd ~/ai-security-capstone/project1
source venv/bin/activate
python app.py
```

Verify with `curl -I http://127.0.0.1:5000/`.

## DVWA setup

Local package candidates are available for Apache, MariaDB, PHP, DVWA, Nikto, and ZAP. Installation/startup requires privileged system changes and remains pending user review.

## Evidence

Use `code-review.md`, `findings.md`, `pentest-report.md`, and the subdirectories for raw outputs, reports, CVSS records, and screenshots. Do not mark findings confirmed or assign CVSS until manually verified.
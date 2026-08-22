# Project 6 Findings Tracker

| ID | Finding | Target | Tool | Status | Evidence | CVSS |
|---|---|---|---|---|---|---|
| P6-SUS-01 | Direct user prompt flow to local model | Project 1 Flask app | Manual prompt test | NOT CONFIRMED | Pending | Pending confirmation |
| P6-SUS-02 | Hardcoded system prompt | `project1/app.py` | Code review | NOT CONFIRMED | `code-review.md` | Pending confirmation |
| P6-SUS-03 | Missing authentication/authorization | Project 1 Flask app | Manual HTTP test | NOT CONFIRMED | Pending | Pending confirmation |
| P6-SUS-04 | Missing security headers | Project 1 Flask app | Curl/Nikto/ZAP | NOT CONFIRMED | Pending | Pending confirmation |
| P6-SUS-05 | In-memory rate limiting limitations | Project 1 Flask app | Manual HTTP test | NOT CONFIRMED | Pending | Pending confirmation |
| P6-SUS-06 | DVWA SQL injection | Local DVWA | Manual/Burp | NOT CONFIRMED | Pending | Pending confirmation |
| P6-SUS-07 | DVWA reflected XSS | Local DVWA | Manual/Burp | NOT CONFIRMED | Pending | Pending confirmation |
| P6-SCAN-01 | Missing security headers | Project 1 Flask app | Nikto/ZAP | NOT CONFIRMED | `reconnaissance/nikto-flask.txt.txt`, `reports/zap-baseline.html` | Pending manual verification |
| P6-SCAN-02 | Apache server-status exposure | Local Apache | Dirb/Nikto | NOT CONFIRMED | `reconnaissance/dirb-apache.txt`, `reconnaissance/nikto-apache.txt.txt` | Pending manual verification |
| P6-SCAN-03 | DVWA exposed files/paths | Local DVWA | Dirb/Nikto | NOT CONFIRMED | `reconnaissance/dirb-dvwa.txt`, `reconnaissance/nikto-dvwa.txt.txt` | Pending manual verification |
| P6-SCAN-04 | ZAP scanner alerts | Project 1 Flask app | OWASP ZAP baseline | SCANNER FINDING - NOT YET CONFIRMED | `reports/zap-baseline.html` | Pending manual verification |

CVSS 3.1 scores will be added only after manual confirmation and evidence review.
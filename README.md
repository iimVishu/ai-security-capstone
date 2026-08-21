# AI Security Capstone

This repository combines three authorized AI security laboratory projects into one parent repository. The work focuses on testing common risks in LLM applications, adding prompt-injection defenses, and documenting red-team and MITRE ATLAS techniques against a local model.

## Projects

### Project 1 — AI Security Lab

Project 1 is a vulnerable-by-design Flask AI chat application assessed against the OWASP LLM Top 10. The assessment covers prompt injection, insecure output handling, training-data poisoning, model denial of service, supply-chain vulnerabilities, sensitive information disclosure, insecure plugin design, excessive agency, overreliance, and model theft. The documented application uses a local Ollama `llama3.2:3b` model at `http://127.0.0.1:5000`.

### Project 2 — Prompt Injection Defense

Project 2 adds a three-layer defense to a Flask LLM endpoint at `POST /ask`:

1. A 500-character input-length limit.
2. Regex-based prompt-injection detection, including encoded-instruction checks.
3. Output scanning for sensitive information and unsolicited external URLs.

The existing project documentation reports five injection payloads blocked with HTTP 400 and ten legitimate queries used to evaluate false positives.

### Project 3 — AI Red Teaming / PromptBench and MITRE ATLAS

Project 3 contains a local red-team campaign with 20 adversarial prompts across prompt injection, jailbreak, role-play bypass, and encoded-payload categories. It also contains a five-technique MITRE ATLAS mapping covering ML Attack Staging, Exfiltration, Impact, Reconnaissance, and AI Model Access. The ATLAS tests target only the local Ollama generation endpoint at `http://127.0.0.1:11434/api/generate`.

## Technologies and Tools

- Python
- Flask
- Requests
- Ollama with Llama 3.2:3b
- Burp Suite
- OWASP LLM Top 10
- MITRE ATLAS
- Kali Linux

## Repository Structure

```text
ai-security-capstone/
├── project1/
│   ├── app.py
│   ├── lab_data.txt
│   ├── owasp_llm_assessment.md
│   └── requirements.txt
├── project2/
│   ├── app.py
│   ├── README.md
│   ├── requirements.txt
│   └── validate.py
├── project3/
│   ├── atlas_mapping.md
│   ├── atlas_results.json
│   ├── atlas_tests.py
│   ├── redteam.py
│   └── redteam_results.json
├── .gitignore
└── README.md
```

Local Python virtual environments are intentionally excluded from version control. Project evidence files, JSON results, scripts, Markdown documentation, and requirements files remain eligible for tracking.

## Evidence and Results

- Project 1 assessment findings and controls are documented in `project1/owasp_llm_assessment.md`.
- Project 2 test scope and reported HTTP 400 blocking results are documented in `project2/README.md`.
- Project 3 campaign output is stored in `project3/redteam_results.json`.
- Project 3 ATLAS technique mapping and generated test records are stored in `project3/atlas_mapping.md` and `project3/atlas_results.json`.

These files preserve the results produced by the local lab runs; the JSON records should be read together with their recorded outcomes and timestamps.

## Security Focus

The capstone emphasizes authorized, local-only testing; prompt and data isolation; input validation; output handling; rate and resource controls; sensitive-information protection; model access; and repeatable evidence collection. No destructive attacks, denial-of-service activity, credential theft, unauthorized access, or external-system testing is part of this repository.

## Navigation

Start with this README for the capstone overview. Each project directory contains its implementation and the documentation or result files specific to that exercise. Read the project documentation before running a local application or red-team script, and use the included result files as the evidence baseline.
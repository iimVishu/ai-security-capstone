# Project 1 — Vulnerable AI Security Lab

## Overview

This project is the baseline lab for an authorized AI security assessment. It demonstrates how a Flask-based application can interact with a local LLM and how weak design choices can introduce common OWASP LLM Top 10 risks.

The application is intentionally vulnerable by design so that security weaknesses can be discussed, tested, and documented in a controlled training environment. The lab uses a local Ollama model and a small knowledge base that includes a deliberately poisoned record.

## Objective

The goal is to evaluate a local AI application against the OWASP LLM Top 10 and to understand how prompt injection, insecure output handling, data poisoning, rate limiting gaps, and model misuse can affect an LLM-powered system.

## Business and Security Context

AI systems are often treated as decision engines or assistants, but they are still exposed to the same software risks plus AI-specific risks:

- user input is not trusted
- model output can be manipulated
- reference data may be malicious or poisoned
- hidden system instructions can be exposed if not isolated properly
- the model may be misused for harmful or unauthorized actions

This project shows those risks in a lab environment, with an emphasis on secure design and responsible testing.

## Architecture

The app uses:

- Python and Flask for the web layer
- requests for outbound calls to Ollama
- Ollama with Llama 3.2:3b as the model runtime
- local knowledge-base text as a trusted or untrusted content source
- a simple web UI for user prompts

## Key Components

### App entry point

- app.py: Flask application and primary attack surface

### Lab data

- lab_data.txt: contains the knowledge base used by the lab as seed context or reference data

### Assessment documentation

- owasp_llm_assessment.md: detailed review mapping the app to OWASP LLM Top 10 categories

### Requirements

- requirements.txt: Python dependencies for the project

## Main Threats Covered

This project reviews and demonstrates risks from the OWASP LLM Top 10, including:

1. Prompt injection
2. Insecure output handling
3. Training data poisoning
4. Model denial of service
5. Supply chain vulnerabilities
6. Sensitive information disclosure
7. Insecure plugin or tool design
8. Excessive agency
9. Overreliance on AI output
10. Model theft or extraction

## Attack Scenarios Explained

### Prompt injection

An attacker submits instructions that try to override the model’s intended behavior. Examples include requests to ignore previous rules, reveal hidden instructions, or act as an unrestricted assistant.

### Poisoned record

The lab includes a deliberately marked poisoned record that falsely tells the model that policy restrictions no longer apply. This highlights why trust boundaries and validation of data sources matter.

### Sensitive information disclosure

The model is tested for attempts to reveal hidden system prompts, internal rules, or confidential lab data.

### Denial of service

The app includes request-size and rate-limit controls meant to prevent abuse, but the system still serves as a reminder that AI applications need resource safeguards.

### Excessive agency

The app is reviewed for situations where the model may be given too much ability to act without safeguards.

## Application Behavior

The app presents a web form where the user enters a prompt. The prompt is sent to a local Ollama model. The model can answer based on the system instruction and untrusted user input. Because the lab is intentionally designed for security training, the application is used to observe how weak prompt design and unsafe application patterns can create risk.

## Core Security Lessons

This project teaches the following patterns:

- never trust user input
- maintain a strong instruction hierarchy
- treat model output as untrusted
- separate system instructions from user content
- validate data and model context
- enforce rate limits and request-size controls
- apply least privilege and ask for human review for important decisions

## How to Run

From the project directory:

```bash
cd project1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open the local application on:

http://127.0.0.1:5000

Make sure Ollama is running locally and the model is available.

## Files in This Project

- app.py: vulnerable AI chat app
- lab_data.txt: lab knowledge base and poisoned record example
- owasp_llm_assessment.md: detailed OWASP LLM Top 10 assessment
- requirements.txt: dependencies

## Interview Talking Points

When answering interview questions, highlight:

- the difference between traditional web vulnerabilities and AI-specific vulnerabilities
- how prompt injection attacks manipulate instruction hierarchy
- why output sanitization and output handling are critical
- how data poisoning can manipulate a model without code changes
- why rate limiting and request controls remain necessary in AI systems

## Example Interview Questions

- What is the difference between a normal web app and an LLM application from a security perspective?
- Why is prompt injection dangerous even when the model seems harmless?
- How would you secure a system like this in production?
- What is training-data poisoning and why does it matter?
- How would you design trust boundaries between system prompts, user input, and model output?

## Summary

Project 1 is the foundation of the capstone: it turns a simple chatbot into a controlled security lab that exposes real AI risks. It is an ideal starting point for discussing how trust, controls, and governance matter in LLM architecture.

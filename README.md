# AI Security Capstone — Study and Interview Guide

## What this repository is

This is an **authorized, local-only AI security lab**. It follows the lifecycle of securing an LLM application: assess risks, add defenses, red-team the model, test MCP integrations, automate security checks, and prepare a penetration test. It uses Python, Flask, and local Ollama with `llama3.2:3b`.

Use only the included local services and harmless fixtures. Nothing in this repository authorizes testing an external model, API, or system.

## One-minute interview summary

> I built an AI-security capstone around a local Flask and Ollama environment. I assessed an intentionally vulnerable LLM app against the OWASP LLM Top 10, added a three-layer prompt-injection defense, ran a controlled red-team campaign mapped to MITRE ATLAS, tested MCP tool-injection and poisoned-resource risks with harmless local fixtures, added a four-gate DevSecOps pipeline, and prepared a scoped penetration-test methodology. My key principle was that user input, retrieved content, model output, tool arguments, and dependencies are all untrusted boundaries that need layered controls and auditable evidence.

## Core concepts from the basics

| Term | Plain-English meaning | Why it matters here |
|---|---|---|
| LLM | A model that generates text from instructions and context. | It is not an authorization engine. |
| Prompt | Text sent to the model. | It can contain legitimate content or adversarial instructions. |
| System prompt | Higher-priority app instructions. | It helps guide the model but is not a security control on its own. |
| Prompt injection | Untrusted text tries to change intended model behavior. | It is a central risk in Projects 1–4. |
| Resource/RAG content | Text retrieved from a file, database, or MCP resource. | Treat it as data, never as trusted instructions. |
| Tool calling | The model asks the app to invoke a defined function. | Tools can have real-world impact and need authorization. |
| MCP | Model Context Protocol: AI clients discover and use tools, resources, and prompts. | It creates useful capabilities and new trust boundaries. |
| Red teaming | Authorized adversarial testing. | It finds weaknesses before attackers do. |
| SAST | Static application security testing. | It reviews source code for risky patterns. |
| Secret scanning | Detection of credentials in source control. | It prevents common supply-chain exposure. |

### The main security rule

Treat **user input, model output, retrieved documents/resources, tool arguments, and third-party dependencies as untrusted**. Validate at the boundary, enforce least privilege, and log important decisions.

## Architecture

```text
User/tester -> Flask application or test harness -> Local Ollama (llama3.2:3b)
                 | validate input/output                 |
                 v                                       v
            local MCP fixture <-------------------- resource/tool evidence logs

Git push/pull request -> Bandit -> Safety -> Gitleaks -> prompt-injection scanner
```

## Projects at a glance

| Project | Theme | Key interview takeaway |
|---|---|---|
| [Project 1](project1/) | Vulnerable LLM app and OWASP assessment | Secure the app surrounding the model, not only the prompt. |
| [Project 2](project2/) | Prompt-injection defenses | Use defense in depth and understand false-positive/bypass tradeoffs. |
| [Project 3](project3/) | Red teaming and MITRE ATLAS | Adversarial tests must be safe, repeatable, and documented. |
| [Project 4](project4/) | MCP security | Tools and resources create high-impact trust boundaries. |
| [Project 5](project5/) | DevSecOps | Automate security gates before release. |
| [Project 6](project6/) | Pen-test methodology | Scanner output needs manual confirmation before it is a finding. |

## Project 1 — Vulnerable AI Security Lab

**Purpose:** the baseline Flask chat application used to discuss AI security risks.

- [app.py](project1/app.py) listens on `127.0.0.1:5000` and calls `http://127.0.0.1:11434/api/generate` using `llama3.2:3b`.
- It has a 16 KiB request limit and an in-memory, per-IP limit of five requests per 60 seconds.
- [owasp_llm_assessment.md](project1/owasp_llm_assessment.md) maps the app to the OWASP LLM Top 10.
- [lab_data.txt](project1/lab_data.txt) contains local training content, including a deliberately poisoned-record example.

**What to say:** Prompt injection attempts to alter model behavior. Data poisoning affects the context/data a model sees. Insecure output handling trusts generated output too much. A system prompt and basic limits help, but production also needs identity and access control, durable rate limiting, output encoding, structured validation, monitoring, and human approval for consequential actions.

```bash
cd project1
source venv/bin/activate
python app.py
```

Open `http://127.0.0.1:5000/` after starting local Ollama.

## Project 2 — Prompt Injection Defence Layer

**Purpose:** a Flask LLM endpoint with three defensive layers.

1. Reject input longer than 500 characters.
2. Detect known injection phrases and long Base64-looking strings with regex.
3. Scan model output for sensitive-information patterns and external URLs.

[app.py](project2/app.py) provides `POST /ask` on `127.0.0.1:5001`; [validate.py](project2/validate.py) implements `validate_input()` and `scan_output()`.

**What to say:** Regex is a quick first layer, not a complete solution: attackers can paraphrase or split requests, and broad patterns can block valid users. Stronger systems separate instructions from data, use allowlisted/least-privilege tools, validate structured output, require authorization for actions, and test bypasses and false positives.

```bash
cd project2
python app.py
curl -X POST http://127.0.0.1:5001/ask \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"Explain least privilege in one paragraph."}'
```

## Project 3 — AI Red Teaming and MITRE ATLAS

**Purpose:** controlled adversarial prompts against the local model. The categories are prompt injection, jailbreaks, role-play bypasses, and encoded payloads.

- [redteam.py](project3/redteam.py) runs 20 prompts and writes [redteam_results.json](project3/redteam_results.json).
- [atlas_tests.py](project3/atlas_tests.py) runs five defensive tests and writes [atlas_results.json](project3/atlas_results.json).
- [atlas_mapping.md](project3/atlas_mapping.md) documents the framework mapping.

The tests reference `AML.T0005` Create Proxy AI Model, `AML.T0056` Extract LLM System Prompt, `AML.T0031` Erode AI Model Integrity, `AML.T0001` Search Open AI Vulnerability Analysis, and `AML.T0040` AI Model Inference API Access.

**What to say:** A model response is evidence to review, not automatic proof of compromise. Define harmless success criteria, record model/version/prompt/response/timestamp, review impact manually, and convert observations into mitigations. MITRE ATLAS gives security teams a common vocabulary for AI threats.

```bash
cd project3
python redteam.py
python atlas_tests.py
```

These commands update the existing JSON evidence.

## Project 4 — MCP Server Security Assessment

**Purpose:** assess MCP risks with local, harmless fixtures. MCP exposes tools, resources, and prompts; each needs a known owner, constrained schema, provenance, least privilege, and audit logging.

### Attack 1: Tool injection

[attack1_harness.py](project4/attack1_harness.py) supplies an original request that says not to use tools together with untrusted injected context. [test_mcp_server/server.py](project4/test_mcp_server/server.py) exposes only `restricted_demo_tool`, a harmless fixture returning `RESTRICTED_TEST_TOOL_CALLED`. See [attack1_results.json](project4/attack1_results.json) and [attack1_server.log](project4/attack1_server.log).

### Attack 2: Resource poisoning

[attack2_resource.txt](project4/attack2_resource.txt) has a clearly marked hidden untrusted instruction. [attack2_harness.py](project4/attack2_harness.py) gives its content to the local model along with a summary request. [attack2_results.json](project4/attack2_results.json) records whether the benign marker was followed.

### Attack 3: Capability chaining

[attack3_harness.py](project4/attack3_harness.py) and [attack3_fixture_server.py](project4/attack3_fixture_server.py) demonstrate a harmless two-tool chain. The output is stored in `attack3_results.json` and `attack3_server.log`.

**What to say:** Do not let model text directly authorize consequential tools. Confirm intent, allowlist tools, validate arguments server-side, scope credentials, authenticate resource provenance, isolate instructions from content, and log calls. See [MCP_INVENTORY.md](project4/MCP_INVENTORY.md), [risk_assessment.md](project4/risk_assessment.md), and [EVIDENCE_CHECKLIST.md](project4/EVIDENCE_CHECKLIST.md) for the assessment approach.

```bash
cd project4
python3 attack1_harness.py
python3 attack2_harness.py
python3 attack3_harness.py
python3 validate_project4.py
```

The attack harnesses require the configured local Ollama service and update their existing evidence artifacts.

## Project 5 — AI Security DevSecOps Pipeline

**Purpose:** security checks run automatically on GitHub push and pull-request events. The workflow is [security.yml](.github/workflows/security.yml) and uses sequential `needs` dependencies.

1. **Bandit:** Python SAST for risky code patterns.
2. **Safety:** dependency vulnerability scan.
3. **Gitleaks:** checks repository/history for secrets.
4. **Custom scanner:** [inject_scanner.py](project5/inject_scanner.py) flags prompt-injection and system-prompt indicators in Python code.

Read [PIPELINE_DESIGN.md](project5/PIPELINE_DESIGN.md) and [FAIL_TEST_PLAN.md](project5/FAIL_TEST_PLAN.md). The clean branch intentionally contains no real secret or confirmed deliberately vulnerable dependency version.

**What to say:** CI gives early feedback and prevents a failed gate from reaching a release path, but it does not replace threat modeling or review. Explain what each tool detects and misses, why gated jobs are sequential, and why failure demonstrations must be isolated on a temporary branch.

```bash
cd project5
python3 -m py_compile app.py inject_scanner.py validate_project5.py
python3 validate_project5.py
```

## Project 6 — AI Penetration-Test Preparation

**Purpose:** an authorized local methodology and evidence structure for Project 1 and local DVWA.

- [pentest-report.md](project6/pentest-report.md): preliminary scope and methodology.
- [findings.md](project6/findings.md): current entries are unconfirmed or scanner findings, not confirmed vulnerabilities.
- [code-review.md](project6/code-review.md): source-review observations.
- [reconnaissance/](project6/reconnaissance/): Nmap, Dirb, and Nikto outputs.
- [reports/zap-baseline.html](project6/reports/zap-baseline.html): ZAP baseline report.
- [cvss/README.md](project6/cvss/README.md): CVSS evidence approach.

**What to say:** Start with scope and authorization, enumerate services, preserve raw evidence, distinguish an observation from a verified finding, and assign CVSS only after manual confirmation. For AI apps, also examine prompt flow, output handling, access control, rate limits, dependencies, logging, and tool integrations.

## Common interview questions

**What is the difference between traditional injection and prompt injection?** Traditional injection targets an interpreter such as SQL or a shell. Prompt injection targets model behavior using natural-language instructions. Both cross a trust boundary, but LLM defenses must handle ambiguous language and downstream tool use.

**Why is a system prompt not enough?** It guides a probabilistic model; it does not enforce permission checks. Deterministic application code must enforce authorization and least privilege.

**How would you secure MCP tools?** Use explicit approval for consequential actions, per-tool authorization, narrow schemas, server-side validation, allowlists, scoped tokens, rate limits, audit logs, and human approval where needed.

**How do you defend against poisoned resources?** Establish provenance/integrity, label retrieved text as untrusted data, keep it separate from instructions, restrict sources, inspect content, and ensure retrieved text cannot expand tool permissions.

**What are the limits of regex filtering?** It catches known patterns quickly but can be bypassed through paraphrase and may create false positives. It is one layer, never the whole solution.

**Why not give every scanner alert a CVSS score?** Tools can be wrong or lack context. CVSS describes a confirmed vulnerability with known exploitability and impact in scope.

## Interview answer structure (STAR)

- **Situation:** A local LLM app handled untrusted prompts, content, and tool-enabled actions.
- **Task:** Identify risks, demonstrate them safely, and improve the controls.
- **Action:** Assessed OWASP risks, implemented input/output checks, red-teamed the model, mapped tests to ATLAS, exercised local MCP fixtures, and automated CI gates.
- **Result:** Produced repeatable local evidence and concrete mitigations without testing beyond authorization.

## Limitations to state honestly

- This is a lab, not proof that a production system is secure.
- Model behavior can vary by model version, prompt, and runtime.
- Project 2's regex-based control is intentionally simple and requires additional layers in production.
- Project 4's results are from harmless local fixtures; do not generalize them to untested MCP servers.
- Project 6 does not claim confirmed findings until manual reproduction and evidence review.
- Security tools reduce risk but do not eliminate threat modeling, access control, review, monitoring, and human judgment.

## Recommended study order

1. Learn the basic terms and the trust-boundary rule above.
2. Study Project 1 to understand the AI security problem.
3. Study Project 2 for defense in depth and its limits.
4. Study Project 3 for red-team methodology and MITRE ATLAS.
5. Study Project 4 for MCP tool/resource risks and evidence.
6. Study Project 5 for automated gates.
7. Finish with Project 6 for scope, evidence quality, and confirmation discipline.

## Evidence and safety

Preserve JSON, logs, and reports as produced. Do not modify attack logic to manufacture results, do not add real secrets for CI demonstrations, and do not present templates, scanner alerts, or unconfirmed observations as confirmed vulnerabilities.

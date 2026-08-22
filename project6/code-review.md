# Project 6 Code Review

## Scope

Reviewed `/home/clouduser/ai-security-capstone/project1/app.py` and the existing Project 1 dependency file. These are **suspected findings** until manually confirmed through controlled testing.

## Application Surface

| Item | Observation |
|---|---|
| Entry point | `project1/app.py` |
| Framework | Flask |
| Route | `POST /` |
| Expected `/chat` route | Not present in the reviewed source; requires confirmation before ZAP/Burp testing |
| Model backend | Local Ollama at `http://127.0.0.1:11434/api/generate` |
| Authentication | No authentication or authorization logic observed |

## Suspected Findings

| Finding | File/line | Reason | Potential impact | Recommended manual verification |
|---|---|---|---|---|
| User-controlled prompt reaches model directly | `project1/app.py:263-299` | `user_prompt` is accepted from the form and placed directly into the Ollama prompt while a system prompt is supplied separately. | Prompt injection or instruction manipulation may influence model behavior. | Submit harmless instruction-override probes and compare responses with expected system behavior. |
| Embedded system prompt in source | `project1/app.py:32` | `SYSTEM_PROMPT` is hardcoded in application code. | Source disclosure or error/log exposure could reveal internal instructions. | Test only local error/rendering paths and inspect repository exposure; do not request secrets. |
| Missing authentication/authorization | `project1/app.py:228-235` | The route accepts requests without an access-control check. | Any reachable local user may submit prompts and consume model resources. | Verify unauthenticated access locally and document the response without altering data. |
| Missing security headers | `project1/app.py:79-220` | No explicit security-header middleware or response-header configuration was observed. | Browser-facing protections such as CSP or frame restrictions may be absent. | Inspect response headers with `curl -I` after the app starts. |
| In-memory rate limiting | `project1/app.py:17-22,51-74` | Request history is stored in process memory and keyed by client IP. | Limits may reset on restart and may not coordinate across workers. | Make a small number of local requests and observe status behavior; do not flood the service. |

## Negative Review Observations

- No `eval()` or `exec()` usage was observed in Project 1.
- No shell/subprocess execution was observed.
- No SQL query or database access was observed.
- No hardcoded API key, password, token, or private key was observed.
- User content is rendered through `render_template_string`; manual XSS confirmation is still required.
- Dependency files are pinned for Flask and Requests, but require separate dependency scanning.

## Status

All items above remain **NOT CONFIRMED** until evidence from local testing is collected.
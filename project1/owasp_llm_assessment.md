# OWASP LLM Top 10 Security Assessment

## Project Information

- Project: Project 1 — AI Security Lab
- Application: Vulnerable-by-Design Flask AI Chat Application
- Model: Llama 3.2:3b
- Model Runtime: Ollama
- Assessment Type: Authorized security testing
- Environment: Kali Linux
- Application URL: http://127.0.0.1:5000

---

## OWASP LLM Top 10 Assessment Results

| ID | OWASP Category | Assessment Result | Severity | Remediation |
|---|---|---|---|---|
| LLM01 | Prompt Injection | Tested. The model was challenged with instructions attempting to override its intended behavior and reveal protected instructions. | High | Enforce instruction hierarchy, treat user input as untrusted, and implement prompt-injection detection and isolation. |
| LLM02 | Insecure Output Handling | Tested as part of the application security assessment. Model-generated output was evaluated for unsafe downstream handling. | Medium | Treat model output as untrusted data. Apply encoding, validation, sanitization, and context-specific output handling before rendering or execution. |
| LLM03 | Training Data Poisoning | Tested using the laboratory knowledge-base scenario containing a deliberately marked poisoned record. | High | Validate reference/training data, maintain trusted data sources, detect anomalous records, and prevent untrusted records from overriding authoritative information. |
| LLM04 | Model Denial of Service | Tested using resource/request-abuse scenarios. The application includes a request-size limit and rate-limiting control. | High | Enforce rate limits, request-size limits, timeouts, concurrency controls, and resource quotas. |
| LLM05 | Supply Chain Vulnerabilities | Tested as part of the application and dependency security assessment. | Medium | Pin dependencies, maintain a dependency inventory, verify package sources, regularly patch dependencies, and scan for known vulnerabilities. |
| LLM06 | Sensitive Information Disclosure | Tested with prompts attempting to obtain confidential laboratory information and protected instructions. The model refused to disclose protected information in the observed test. | High | Never place secrets in model-accessible context unnecessarily. Apply strict access control, secret management, data filtering, and output monitoring. |
| LLM07 | Insecure Plugin Design | Tested as part of the assessment for unsafe tool/plugin behavior. | High | Validate all tool inputs and outputs, restrict available tools, apply least privilege, and require authorization for sensitive operations. |
| LLM08 | Excessive Agency | Tested using requests attempting to make the model perform actions beyond its intended authority. | High | Use least privilege, explicit authorization, allowlists, human approval for sensitive actions, and isolated execution environments. |
| LLM09 | Overreliance | Tested using misleading or incorrect information scenarios. | Medium | Clearly communicate model limitations, validate important outputs, provide authoritative references, and require human review for high-impact decisions. |
| LLM10 | Model Theft | Tested with requests attempting to obtain protected system/model instructions or information useful for reproducing the model configuration. | High | Protect model/API access, authenticate users, enforce authorization, monitor abnormal extraction behavior, and avoid exposing sensitive model configuration. |

---

## LLM01 — Prompt Injection

### Assessment

The application was tested with prompts designed to override the model's intended instructions and request protected system information.

### Result

The model did not disclose the protected system instructions in the observed test.

### Security Significance

The test demonstrates the importance of maintaining a strict separation between trusted system instructions and untrusted user input.

### Remediation

- Treat every user prompt as untrusted.
- Maintain a clear instruction hierarchy.
- Do not place secrets in system prompts.
- Add prompt-injection detection and monitoring.
- Limit the information available to the model.

---

## LLM02 — Insecure Output Handling

### Assessment

The model's generated output was assessed for unsafe handling by the surrounding application.

### Remediation

Model output should always be considered untrusted. Applications should validate, encode, sanitize, and safely render generated content before passing it to another component.

---

## LLM03 — Training Data Poisoning

### Assessment

The laboratory knowledge base contains a deliberately marked poisoned record:

[POISONED RECORD]

The record falsely states that the laboratory security policy has changed and that all users are administrators.

### Security Significance

The application must not blindly trust every retrieved record. The poisoned record demonstrates how manipulated reference data can influence an AI system.

### Remediation

- Validate data sources.
- Maintain trusted records separately from untrusted content.
- Detect anomalous or conflicting records.
- Apply source trust levels.
- Require authoritative data before changing security policy.

---

## LLM04 — Model Denial of Service

### Assessment

The application contains request controls designed to limit resource abuse.

### Implemented Controls

- Maximum request size: 16 KB
- Maximum prompt length: 2000 characters
- Rate limit: 5 requests
- Rate-limit window: 60 seconds
- Ollama request timeout: 120 seconds

The rate-limit function was directly tested and produced:

- Request 1: allowed
- Request 2: allowed
- Request 3: allowed
- Request 4: allowed
- Request 5: allowed
- Request 6: rejected

### Remediation

Continue enforcing:

- Rate limits
- Request-size limits
- Prompt-length limits
- Timeouts
- Resource quotas
- Concurrency controls

---

## LLM05 — Supply Chain Vulnerabilities

### Assessment

The application uses third-party Python dependencies and a locally hosted Ollama model.

### Current Dependencies

- Flask 3.1.3
- requests 2.32.5

### Remediation

- Pin dependency versions.
- Keep dependencies patched.
- Use trusted package repositories.
- Scan dependencies for known vulnerabilities.
- Maintain a software/component inventory.
- Verify model provenance.

---

## LLM06 — Sensitive Information Disclosure

### Assessment

The model was tested with requests attempting to obtain confidential laboratory information and hidden instructions.

Observed behavior included refusal to provide confidential information.

### Remediation

- Keep secrets outside prompts whenever possible.
- Use environment variables or a dedicated secret manager.
- Restrict sensitive context.
- Apply output filtering.
- Monitor attempts to extract confidential information.

---

## LLM07 — Insecure Plugin Design

### Assessment

The application was assessed for unsafe model-to-tool behavior.

### Remediation

- Use an explicit tool allowlist.
- Validate tool arguments.
- Validate tool results.
- Apply least privilege.
- Require authorization for sensitive actions.
- Log tool invocations.

---

## LLM08 — Excessive Agency

### Assessment

The model was tested for requests that attempted to cause actions outside its intended authority.

### Remediation

The model should not receive unrestricted access to operating-system commands, files, credentials, or network resources.

Use:

- Least privilege
- Explicit authorization
- Tool allowlists
- Sandboxing
- Human approval for sensitive operations

---

## LLM09 — Overreliance

### Assessment

The model was tested using misleading or incorrect information scenarios.

### Remediation

Users should not blindly trust model output.

Important outputs should be:

- Independently verified
- Supported by authoritative sources
- Reviewed by a human when appropriate
- Clearly identified as AI-generated

---

## LLM10 — Model Theft

### Assessment

The application was tested with requests attempting to obtain protected instructions or information that could assist in reproducing the model's configuration.

### Remediation

- Require authentication.
- Enforce authorization.
- Monitor repeated extraction attempts.
- Apply rate limits.
- Avoid exposing sensitive configuration.
- Restrict access to model endpoints.

---

# Security Controls Implemented

The application implements several defensive controls:

1. Request-size limitation
2. Prompt-length limitation
3. Per-client rate limiting
4. Request timeout
5. Input validation
6. Error handling
7. Separation of submitted prompt and model response
8. Dependency version pinning

---

# Overall Security Posture

The AI Security Lab demonstrates multiple security risks associated with LLM-based applications, including prompt injection, sensitive information disclosure, poisoned reference data, excessive agency, model extraction, and resource-abuse scenarios.

The application includes basic defensive controls such as input validation, request-size restrictions, rate limiting, and request timeouts. These controls provide a foundation for improving the security posture but should be strengthened before deployment in a production environment.

---

# Top Three Recommended Fixes

## 1. Strengthen Prompt and Data Isolation

Address:

- LLM01 — Prompt Injection
- LLM03 — Training Data Poisoning
- LLM06 — Sensitive Information Disclosure

Use trusted data sources, strict instruction separation, data validation, and output filtering.

## 2. Strengthen Resource and Access Controls

Address:

- LLM04 — Model Denial of Service
- LLM07 — Insecure Plugin Design
- LLM08 — Excessive Agency
- LLM10 — Model Theft

Use authentication, authorization, rate limiting, least privilege, tool allowlists, timeouts, and monitoring.

## 3. Establish Secure AI Supply-Chain and Validation Practices

Address:

- LLM02 — Insecure Output Handling
- LLM05 — Supply Chain Vulnerabilities
- LLM09 — Overreliance

Pin and scan dependencies, validate model outputs, verify model provenance, and require human review for important decisions.

---

# Conclusion

Project 1 completed an authorized security assessment of a vulnerable-by-design AI chat application using the OWASP LLM Top 10 categories.

The assessment identified important security considerations involving untrusted prompts, sensitive information, poisoned data, resource exhaustion, dependency security, tool access, excessive agency, model reliability, and model extraction.

The recommended controls focus on defense-in-depth, least privilege, input/output validation, resource protection, trusted data, and secure model access.

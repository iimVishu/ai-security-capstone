# Burp Suite Capture

**Status: PENDING MANUAL CAPTURE.** Burp GUI traffic was not captured automatically.

## Scope

Configure Burp only for the authorized local/sample MCP server. Do not include credentials, API keys, tokens, or private keys in exported evidence.

## Evidence procedure

1. Configure the local MCP client/server HTTP traffic to use the Burp proxy.
2. Perform one harmless MCP request.
3. Export the raw request to `evidence/burp_request.txt` and response to `evidence/burp_response.txt`.
4. Record method, URL, headers, body, status, response headers/body, and relevant MCP protocol fields below.

| Field | Value |
|---|---|
| Method | Pending |
| URL | Pending |
| Status | Pending |
| MCP transport/protocol data | Pending |

**MANUAL STEP REQUIRED:** Paste sanitized raw Burp data into the evidence files.
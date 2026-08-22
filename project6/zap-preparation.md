# Burp and ZAP Preparation

The reviewed Project 1 source exposes `POST /`, not `/chat`:

```text
http://127.0.0.1:5000/
POST form field: prompt
```

This must be confirmed at runtime before configuring Burp or ZAP. The application sends the form value as `prompt` to the local Ollama endpoint. No `/chat` route was observed in source.

**MANUAL STEP REQUIRED:** Start Project 1, capture one normal request through Burp/ZAP, and verify the actual route before any active scan. Restrict ZAP scope to `127.0.0.1:5000`.
# Project 2 - Prompt Injection Defence Layer

## Objective

This project implements and tests a three-layer prompt injection defence for a Flask-based LLM application using a locally hosted Ollama/Llama model.

## Defence Layers

1. Input length validation with a 500-character maximum.
2. Regex-based prompt injection detection.
3. Output scanning for sensitive information and unsolicited external URLs.

## Testing

Five prompt injection payloads were tested before and after implementation of the defence layer.

After implementation, all five tested payloads returned HTTP 400 and were blocked.

Ten legitimate queries were also tested to evaluate false-positive behaviour.

## Technologies

- Python
- Flask
- Ollama
- Llama 3.2
- Requests
- Burp Suite

## Endpoint

```text
POST /ask

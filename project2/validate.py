import re

# Layer 1: Maximum input length
MAX_LENGTH = 500

# Layer 2: Prompt-injection blocklist
INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"ignore\s+previous\s+instructions",
    r"you\s+are\s+now",
    r"pretend\s+you\s+are",
    r"act\s+as\s+if",
    r"jailbreak",
    r"system\s+prompt",
    r"reveal\s+(your\s+)?system\s+prompt",
    r"bypass\s+authentication",
    r"do\s+not\s+follow\s+previous",
    r"forget\s+(all\s+)?previous",
]


def validate_input(prompt):
    """
    Layer 1 + Layer 2:
    Validate length and detect common prompt-injection patterns.
    """

    if len(prompt) > MAX_LENGTH:
        return False, "Input exceeds maximum allowed length of 500 characters."

    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            return False, "Prompt injection pattern detected."

    # Detect long Base64-looking strings
    base64_pattern = r"\b[A-Za-z0-9+/]{40,}={0,2}\b"

    if re.search(base64_pattern, prompt):
        return False, "Potentially encoded instruction detected."

    return True, ""


# Layer 3: Output scanner
def scan_output(response):
    """
    Detect sensitive information in model responses.
    """

    sensitive_patterns = [
        r"system\s+prompt",
        r"password\s*[:=]",
        r"api[_-]?key\s*[:=]",
        r"token\s*[:=]",
        r"secret\s*[:=]",
    ]

    for pattern in sensitive_patterns:
        if re.search(pattern, response, re.IGNORECASE):
            return False, "Potentially sensitive information detected in model output."

    # Detect unsolicited external URLs
    url_pattern = r"https?://[^\s]+"

    if re.search(url_pattern, response, re.IGNORECASE):
        return False, "External URL detected in model output."

    return True, ""

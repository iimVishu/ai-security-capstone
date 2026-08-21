import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REQUIRED_FILES = [
    "README.md", "mcp_inventory.json", "MCP_INVENTORY.md", "inventory_mcp.py",
    "mcp_attack_surface.md", "risk_assessment.md", "attack1_tool_injection.md",
    "attack1_results.json", "attack2_resource_poisoning.md", "attack2_results.json",
    "attack3_capability_chaining.md", "attack3_results.json", "burp_capture.md",
    "project4_results.json", "PROJECT4_REPORT.md", "EVIDENCE_CHECKLIST.md",
    "evidence/burp_request.txt", "evidence/burp_response.txt",
]
JSON_FILES = [
    "mcp_inventory.json", "attack1_results.json", "attack2_results.json",
    "attack3_results.json", "project4_results.json",
]
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY-----"),
    re.compile(r"(?i)(api[_-]?key|access[_-]?token|secret[_-]?key)\s*[:=]\s*['\"]?[A-Za-z0-9+/=_-]{16,}"),
]


def read_json(name):
    with (ROOT / name).open(encoding="utf-8") as source:
        return json.load(source)


def main():
    exists = all((ROOT / name).is_file() for name in REQUIRED_FILES)
    valid_json = True
    documents = {}
    try:
        for name in JSON_FILES:
            documents[name] = read_json(name)
    except (OSError, json.JSONDecodeError):
        valid_json = False

    inventory = documents.get("mcp_inventory.json", {})
    inventory_ok = all(key in inventory for key in ("server", "tools", "resources", "prompts"))
    attack_keys = {
        "attack1_results.json": ("attack_prompt", "expected_behavior", "mitigation"),
        "attack2_results.json": ("original_content", "hidden_instruction", "mitigation"),
        "attack3_results.json": ("tool_a", "tool_b", "mitigation"),
    }
    attacks_ok = all(all(key in documents.get(name, {}) for key in keys) for name, keys in attack_keys.items())
    results = documents.get("project4_results.json", {})
    results_ok = all(key in results for key in ("project", "environment", "server", "inventory", "attacks", "burp_capture", "findings", "mitigations", "evidence"))
    report_ok = (ROOT / "PROJECT4_REPORT.md").is_file()
    secret_ok = True
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            text = path.read_text(encoding="utf-8", errors="ignore")
            if any(pattern.search(text) for pattern in SECRET_PATTERNS):
                secret_ok = False
    venv_ok = not any(path.is_dir() and path.name in {".venv", "venv", "env", "node_modules"} for path in ROOT.iterdir())

    print("PROJECT 4 VALIDATION")
    print("--------------------")
    print(f"Project structure: {'PASS' if exists else 'FAIL'}")
    print(f"Inventory: {'PASS' if valid_json and inventory_ok else 'FAIL'}")
    print(f"Tool Injection: {'PASS' if valid_json and attacks_ok else 'FAIL'}")
    print(f"Resource Poisoning: {'PASS' if valid_json and attacks_ok else 'FAIL'}")
    print(f"Capability Chaining: {'PASS' if valid_json and attacks_ok else 'FAIL'}")
    print(f"Results JSON: {'PASS' if valid_json and results_ok else 'FAIL'}")
    print(f"Report: {'PASS' if report_ok else 'FAIL'}")
    print(f"Secret check: {'PASS' if secret_ok and venv_ok else 'FAIL'}")
    return 0 if all((exists, valid_json, inventory_ok, attacks_ok, results_ok, report_ok, secret_ok, venv_ok)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
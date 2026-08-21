import json
import sys
from datetime import datetime, timezone
from pathlib import Path


LOG_FILE = Path(__file__).resolve().parent / "attack3_server.log"
TOOL_1 = "chain_source_tool"
TOOL_2 = "chain_consumer_tool"


def log_event(event):
    with LOG_FILE.open("a", encoding="utf-8") as log:
        log.write(json.dumps({"timestamp": datetime.now(timezone.utc).isoformat(), **event}) + "\n")


def reply(request_id, result=None, error=None):
    message = {"jsonrpc": "2.0", "id": request_id}
    message["error" if error else "result"] = error or result
    sys.stdout.write(json.dumps(message) + "\n")
    sys.stdout.flush()


def main():
    log_event({"event": "server_started", "tools": [TOOL_1, TOOL_2]})
    for line in sys.stdin:
        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            continue
        method = request.get("method")
        request_id = request.get("id")
        if method == "initialize":
            reply(request_id, {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "project4-chain-fixture", "version": "1.0.0"},
            })
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            reply(request_id, {"tools": [
                {"name": TOOL_1, "description": "Harmless source tool for local chain testing.", "inputSchema": {"type": "object", "properties": {"value": {"type": "string"}}, "required": ["value"], "additionalProperties": False}},
                {"name": TOOL_2, "description": "Harmless consumer tool for local chain testing.", "inputSchema": {"type": "object", "properties": {"value": {"type": "string"}}, "required": ["value"], "additionalProperties": False}},
            ]})
        elif method == "tools/call":
            params = request.get("params", {})
            name = params.get("name")
            arguments = params.get("arguments", {})
            value = arguments.get("value")
            if name == TOOL_1 and isinstance(value, str):
                output = f"SOURCE_VALUE::{value}"
            elif name == TOOL_2 and isinstance(value, str):
                output = f"CONSUMED_VALUE::{value}"
            else:
                reply(request_id, error={"code": -32602, "message": "Expected a safe string value for a known chain tool."})
                continue
            log_event({"event": "tool_invoked", "tool": name, "arguments": arguments, "response": output})
            reply(request_id, {"content": [{"type": "text", "text": output}]})
        else:
            reply(request_id, error={"code": -32601, "message": f"Unsupported method: {method}"})


if __name__ == "__main__":
    main()
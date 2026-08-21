import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SERVER = ROOT / "attack3_fixture_server.py"
LOG_FILE = ROOT / "attack3_server.log"
RESULTS = ROOT / "attack3_results.json"
TOOL_1 = "chain_source_tool"
TOOL_2 = "chain_consumer_tool"


def send(process, message):
    process.stdin.write((json.dumps(message) + "\n").encode())
    process.stdin.flush()
    while True:
        response = json.loads(process.stdout.readline().decode())
        if response.get("id") == message.get("id"):
            return response


def text_from(response):
    return response["result"]["content"][0]["text"]


def main():
    LOG_FILE.unlink(missing_ok=True)
    process = subprocess.Popen(["python3", str(SERVER)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    timestamp = datetime.now(timezone.utc).isoformat()
    try:
        send(process, {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
        process.stdin.write(b'{"jsonrpc":"2.0","method":"notifications/initialized"}\n')
        process.stdin.flush()
        listed = send(process, {"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        names = [tool["name"] for tool in listed["result"]["tools"]]
        tool_1_input = {"value": "harmless-chain-test"}
        tool_1_response = text_from(send(process, {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": TOOL_1, "arguments": tool_1_input}}))
        tool_2_input = {"value": tool_1_response}
        tool_2_response = text_from(send(process, {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": TOOL_2, "arguments": tool_2_input}}))
        log_text = LOG_FILE.read_text(encoding="utf-8")
        events = [json.loads(line) for line in log_text.splitlines() if line]
        tool_1_events = [event for event in events if event.get("event") == "tool_invoked" and event.get("tool") == TOOL_1]
        tool_2_events = [event for event in events if event.get("event") == "tool_invoked" and event.get("tool") == TOOL_2]
        passed_value = tool_2_input["value"] == tool_1_response
        success = bool(TOOL_1 in names and TOOL_2 in names and tool_1_events and tool_2_events and passed_value and tool_2_response)
        result = {
            "status": "SUCCESSFUL_CONTROLLED_CAPABILITY_CHAIN" if success else "BLOCKED_OR_UNVERIFIED",
            "tool_1_name": TOOL_1,
            "tool_1_input": tool_1_input,
            "tool_1_response": tool_1_response,
            "tool_2_name": TOOL_2,
            "tool_2_input": tool_2_input,
            "tool_2_response": tool_2_response,
            "chain": f"{TOOL_1} -> actual response -> {TOOL_2}",
            "actual_tool_1_invocation": bool(tool_1_events),
            "actual_tool_2_invocation": bool(tool_2_events),
            "tool_2_input_equals_tool_1_response": passed_value,
            "tool_a": {"name": TOOL_1, "input": tool_1_input, "output": tool_1_response},
            "tool_b": {"name": TOOL_2, "input": tool_2_input, "output": tool_2_response},
            "final_result": "SUCCESSFUL_CONTROLLED_CAPABILITY_CHAIN" if success else "BLOCKED_OR_UNVERIFIED",
            "mitigation": "Validate cross-tool data flow and require authorization at each consequential boundary.",
            "timestamp": timestamp,
            "evidence_location": [str(LOG_FILE.relative_to(ROOT)), str(RESULTS.relative_to(ROOT))],
        }
    except Exception as error:
        result = {"status": "BLOCKED_OR_UNVERIFIED", "error": str(error), "tool_1_name": TOOL_1, "tool_2_name": TOOL_2, "actual_tool_1_invocation": False, "actual_tool_2_invocation": False, "final_result": "BLOCKED_OR_UNVERIFIED", "timestamp": timestamp, "evidence_location": [str(LOG_FILE.relative_to(ROOT)), str(RESULTS.relative_to(ROOT))]}
    finally:
        process.terminate()
        process.wait(timeout=5)
    RESULTS.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
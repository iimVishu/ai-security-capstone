# Attack 3 - Controlled Capability Chaining

## Scope

| Field | Value |
|---|---|
| Fixture | `attack3_fixture_server.py` |
| Tool 1 | `chain_source_tool` |
| Tool 2 | `chain_consumer_tool` |
| Authorization | Local Project 4 lab only |
| Timestamp | `2026-08-21T08:45:37.785245+00:00` |

Both tools are harmless local demonstration tools. They perform no filesystem, shell, network, credential, or destructive operation.

## Actual Two-Step Sequence

### Step 1 - Tool 1

Tool 1 input:

```json
{"value": "harmless-chain-test"}
```

Tool 1 actual response:

```text
SOURCE_VALUE::harmless-chain-test
```

The response above was captured from the actual JSON-RPC tool response.

### Step 2 - Tool 2

Tool 2 input:

```json
{"value": "SOURCE_VALUE::harmless-chain-test"}
```

The harness assigned Tool 2's input from Tool 1's captured response and verified:

```text
tool_2_input == tool_1_response
True
```

Tool 2 actual response:

```text
CONSUMED_VALUE::SOURCE_VALUE::harmless-chain-test
```

The Tool 2 response was returned by the fixture; it was not hard-coded in the harness.

## Result

```text
Tool 1 invoked: True
Tool 2 invoked: True
Tool 2 input equals Tool 1 response: True
Final result: SUCCESSFUL_CONTROLLED_CAPABILITY_CHAIN
```

This demonstrates how two individually harmless capabilities can create a composed data flow. The safe mitigation is to validate cross-tool data flow and apply authorization and scope controls at each consequential boundary.

## Evidence

- Harness: `attack3_harness.py`
- Fixture: `attack3_fixture_server.py`
- Server invocation log: `attack3_server.log`
- Structured result: `attack3_results.json`
- Exact command: `python3 attack3_harness.py`
# Attack 3 - Capability Chaining

**Status: PENDING.** Two suitable low-risk tools cannot be selected until the actual inventory is available. No chain was executed.

## Safe test procedure

Select two observed, non-destructive capabilities. Pass Tool A's harmless output as context or input to Tool B, record both complete exchanges, and explain why the combined permissions create more risk than either tool alone.

**MANUAL STEP REQUIRED:** Use only lab data and tools with no destructive side effects.
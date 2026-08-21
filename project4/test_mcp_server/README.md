# Project 4 Restricted MCP Test Fixture

This is a separate local test fixture. It does not modify or replace `mcp-servers/everything`.

## Tool

The fixture exposes exactly one restricted tool:

```text
restricted_demo_tool
```

It performs no filesystem, shell, network, credential, or system operation. A valid call returns exactly:

```text
RESTRICTED_TEST_TOOL_CALLED
```

The server writes invocation evidence to `project4/attack1_server.log`.

## Run the controlled harness

From `project4/`:

```bash
python3 attack1_harness.py
```

The harness starts this fixture over stdio, gives the local Ollama model the tool definition and controlled prompt, and invokes the fixture only if the model returns an actual tool call. It writes `attack1_results.json` and shuts down the fixture.

## Run the fixture manually

```bash
python3 test_mcp_server/server.py
```

The manual process expects newline-delimited JSON-RPC messages on standard input. Use the harness for repeatable evidence.
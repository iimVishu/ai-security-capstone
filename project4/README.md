# Project 4 - MCP Server Security Assessment and Exploitation

This project is a scaffold for an authorized, local-only MCP security assessment. No sample MCP server or server configuration was present in the workspace when these files were created, so capability discovery and attack execution are marked pending rather than invented.

## Environment Verification

Verified on 2026-08-21:

```text
Node.js v24.19.0
npm 11.16.0
```

## MCP Inspector

The expected Inspector URL is `http://localhost:6274`. See [mcp_inspector_setup.md](mcp_inspector_setup.md) for the launch and verification procedure. The UI and server connection were not claimed as verified because no sample server configuration was available.

## Files

- `inventory_mcp.py` collects an inventory from a supplied JSON-RPC capability snapshot or validates an existing inventory.
- `mcp_inventory.json` is an empty, verified inventory awaiting a real server connection.
- `MCP_INVENTORY.md`, `mcp_attack_surface.md`, and `risk_assessment.md` document the pending state and assessment method.
- `attack*_*.md` and `attack*_results.json` contain safe procedures and unexecuted result records.
- `burp_capture.md` and `evidence/` provide manual capture templates.
- `validate_project4.py` checks structure, JSON, required fields, secret patterns, and virtual-environment exclusion.

## Manual Step Required

Place the authorized sample MCP server and its launch configuration in this directory, then run the Inspector and collect actual capabilities before populating the inventory or executing attacks. Do not record a successful test until the server response is available.
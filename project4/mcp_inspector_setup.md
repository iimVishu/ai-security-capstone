# MCP Inspector Setup

## Verified prerequisites

- Node.js: `v24.19.0`
- npm: `11.16.0`
- Expected Inspector URL: `http://localhost:6274`
- Current Inspector status: **PENDING**
- Current MCP server status: **PENDING**; no sample server command/configuration was present.

## Launch procedure

From this directory, run the required Inspector command:

```bash
npx @modelcontextprotocol/inspector
```

Use the provided sample server command or configuration when prompted. Do not substitute an external or public MCP server.

## Verification commands

```bash
curl -I http://localhost:6274
ss -ltnp | grep ':6274'
```

Record the server name, transport, endpoint, connection status, and capabilities only after they are visible in Inspector or returned by the local protocol exchange.

**MANUAL STEP REQUIRED:** Launch the sample server and Inspector, verify the local UI, and capture the terminal/UI evidence manually.
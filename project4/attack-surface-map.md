# MCP Attack Surface Map

## Assessment Scope

| Field | Value |
|---|---|
| MCP server | `mcp-servers/everything` |
| Evidence source | Current `mcp_inventory.json` and MCP Inspector observations |
| Confirmed tools | None recorded in the current inventory |
| Confirmed resources | None recorded in the current inventory |
| Confirmed prompts | None recorded in the current inventory |
| Assessment status | Pending verification |


## Assessment Scope

| Field | Value |
|---|---|
| MCP server | `mcp-servers/everything` |
| Evidence source | MCP Inspector tool list supplied for this assessment |
| Confirmed tools | 19 |
| Confirmed resources | None; Pending verification |
| Confirmed prompts | None; Pending verification |
| Assessment status | Tool identifiers confirmed; schemas and behavior pending verification |

The names and identifiers below are confirmed Inspector observations. Descriptions, purposes, parameters, input schemas, side effects, resources, prompts, and vulnerabilities are not inferred from the names. Risk ratings are security assessments based only on the apparent capability indicated by each confirmed tool name; they are not observed vulnerabilities or attack results.

## diagrams.net / draw.io Layout

Create one server node and one capability node for each of the 19 tools. Connect each tool node to the server node. Use the risk colors shown below. Keep resources and prompts as separate pending-verification nodes or omit them until observed.

```text
[mcp-servers/everything]
    +--> [Tool: echo | Low | green]
    +--> [Tool: get-env | High | red]
    +--> [Tool: trigger-sampling-request | High | red]
    +--> [Tool: ... | assessment rating | color]
    +--> [Resources: Pending verification]
    +--> [Prompts: Pending verification]
```

Risk colors: **High = red**, **Medium = amber**, **Low = green**.

## Confirmed Tool Nodes

| Type | Tool name | Identifier | Parameters/schema | Risk assessment |
|---|---|---|---|---|
| Tool | Echo Tool | `echo` | Pending verification | Low (green) |
| Tool | Get Annotated Message Tool | `get-annotated-message` | Pending verification | Low (green) |
| Tool | Print Environment Tool | `get-env` | Pending verification | High (red) |
| Tool | Get Resource Links Tool | `get-resource-links` | Pending verification | Medium (amber) |
| Tool | Get Resource Reference Tool | `get-resource-reference` | Pending verification | Medium (amber) |
| Tool | Get Structured Content Tool | `get-structured-content` | Pending verification | Medium (amber) |
| Tool | Get Sum Tool | `get-sum` | Pending verification | Low (green) |
| Tool | Get Tiny Image Tool | `get-tiny-image` | Pending verification | Low (green) |
| Tool | GZip File as Resource Tool | `gzip-file-as-resource` | Pending verification | Medium (amber) |
| Tool | Toggle Simulated Logging | `toggle-simulated-logging` | Pending verification | Medium (amber) |
| Tool | Toggle Subscriber Updates | `toggle-subscriber-updates` | Pending verification | Medium (amber) |
| Tool | Trigger Long-Running Operation Tool | `trigger-long-running-operation` | Pending verification | Medium (amber) |
| Tool | Get Roots List Tool | `get-root-list` | Pending verification | High (red) |
| Tool | Trigger Elicitation Request Tool | `trigger-elicitation-request` | Pending verification | High (red) |
| Tool | Trigger URL Elicitation Tool | `trigger-url-elicitation` | Pending verification | High (red) |
| Tool | Trigger Sampling Request Tool | `trigger-sampling-request` | Pending verification | High (red) |
| Tool | Simulate Resource Query | `simulate-resource-query` | Pending verification | Medium (amber) |
| Tool | Trigger Async Sampling Request Tool | `trigger-async-sampling-request` | Pending verification | High (red) |
| Tool | Trigger Async Elicitation Request Tool | `trigger-async-elicitation-request` | Pending verification | High (red) |

## High and Medium Assessment Notes

These are potential abuse scenarios, not claims that the tools are vulnerable or that an attack succeeded.

| Identifier | Risk assessment | One-line potential abuse scenario | Basis limitation |
|---|---|---|---|
| `get-env` | High (red) | If it returns process environment data, an unauthorized caller could seek sensitive configuration values. | Exact schema and returned data pending verification. |
| `get-resource-links` | Medium (amber) | If it exposes links broadly, an attacker could use returned references to discover or reach unintended resources. | Exact scope and URI handling pending verification. |
| `get-resource-reference` | Medium (amber) | If it resolves caller-controlled references, an attacker could attempt access to an unintended resource. | Exact reference validation pending verification. |
| `get-structured-content` | Medium (amber) | If it accepts untrusted structured content, malformed or instruction-bearing data could cross a trust boundary. | Input schema and consumer behavior pending verification. |
| `gzip-file-as-resource` | Medium (amber) | If it accepts arbitrary paths, an attacker could attempt to package and expose an unintended local file. | Path restrictions and side effects pending verification. |
| `toggle-simulated-logging` | Medium (amber) | If callable without authorization, an attacker could alter diagnostic behavior and reduce assessment visibility. | State scope and authorization pending verification. |
| `toggle-subscriber-updates` | Medium (amber) | If callable without authorization, an attacker could alter update delivery or notification behavior. | State scope and authorization pending verification. |
| `trigger-long-running-operation` | Medium (amber) | If inputs are unbounded, an attacker could consume time or resources with an unnecessarily long lab operation. | Limits and cancellation behavior pending verification. |
| `get-root-list` | High (red) | If it reveals client roots, an unauthorized caller could learn local workspace locations or access boundaries. | Returned fields and access controls pending verification. |
| `trigger-elicitation-request` | High (red) | If it can prompt for sensitive user input, an attacker could socially engineer disclosure through a trusted client surface. | Elicitation contents and consent controls pending verification. |
| `trigger-url-elicitation` | High (red) | If it presents caller-controlled URLs, an attacker could induce navigation to an untrusted destination. | URL validation and user confirmation pending verification. |
| `trigger-sampling-request` | High (red) | If it can request model sampling without clear user authorization, an attacker could influence model use or incur unintended processing. | Sampling scope and approval controls pending verification. |
| `simulate-resource-query` | Medium (amber) | If query inputs are not constrained, an attacker could use simulation results to probe resource-handling behavior. | Query schema and isolation guarantees pending verification. |
| `trigger-async-sampling-request` | High (red) | If asynchronous sampling lacks authorization or limits, an attacker could initiate unreviewed model work. | Job controls and approval behavior pending verification. |
| `trigger-async-elicitation-request` | High (red) | If asynchronous elicitation can request user data without clear consent, an attacker could create delayed social-engineering prompts. | Consent and cancellation behavior pending verification. |

## Low-Risk Assessment Notes

The following are assessment ratings based on the names alone and are not findings:

- `echo` and `get-annotated-message` appear limited to message transformation or retrieval; exact behavior is pending verification.
- `get-sum` appears computational and non-destructive; input limits and behavior are pending verification.
- `get-tiny-image` appears to return a small image payload; data source and output handling are pending verification.

## Pending Verification

- Complete JSON input schemas, required/optional parameters, types, enums, and defaults for all tools.
- Exact descriptions and observed behavior for all tools.
- Resources, resource URIs, MIME types, and prompts; none were confirmed in the supplied list.
- Transport, endpoint, authorization, side effects, and actual tool responses.
- Any exploitability or successful/blocked attack result.

**MANUAL STEP REQUIRED:** Capture the MCP Inspector Tools panel showing the 19 tools and use it as the evidence screenshot for this map. Do not claim an attack succeeded without a recorded request and response.
## Confirmed Capability Nodes

**No capability nodes can be populated yet.** The current `mcp_inventory.json` has empty `tools`, `resources`, and `prompts` arrays. This is an evidence limitation, not a conclusion that the server exposes no capabilities.

## diagrams.net / draw.io Layout

Reproduce the map as an editable diagram with the following structure after capabilities are confirmed:

```text
[mcp-servers/everything]
          |
          +--> [Tool: exact Inspector name]
          |
          +--> [Resource: exact Inspector URI]
          |
          +--> [Prompt: exact Inspector name]
```

Use one node for every observed tool, resource, and prompt. Connect the server node to each capability node. Add connections between capabilities only when the Inspector evidence or recorded protocol exchange demonstrates a relationship.

## Node Format

Each confirmed node must use this structure:

```text
Type: Tool | Resource | Prompt
Name/URI: exact Inspector value
Purpose/description: exact observed description
Parameters/schema: complete observed JSON schema, or "None observed"
Risk: High (red) | Medium (amber) | Low (green)
Reason: evidence-based explanation
Abuse scenario: one line for High or Medium risks
```

Risk colors are presentation labels only: High = red, Medium = amber, Low = green. Do not assign a rating until the capability, inputs, side effects, and access scope are confirmed.

## Pending Verification

- MCP Inspector connection status and transport
- All tool names, purposes, and complete JSON input schemas
- Required and optional parameters, types, enums, and defaults
- Resources, URIs, descriptions, and MIME/content types
- Prompts, descriptions, and arguments
- Evidence-based risk ratings and abuse scenarios
- Any relationships or dependencies between capabilities

## Evidence Requirement

**MANUAL STEP REQUIRED:** Capture the MCP Inspector Tools, Resources, and Prompts panels, then update this map from the observed values. Capture the completed editable diagram in diagrams.net/draw.io as the attack-surface evidence screenshot. No attack is claimed successful by this document.
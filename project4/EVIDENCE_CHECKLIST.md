# Evidence Checklist

| Done | Screenshot/evidence | Required visible content | Recommended filename | Caption |
|---|---|---|---|---|
| [x] | Node/npm verification | Terminal path, `node --version`, `npm --version` | `evidence/01-node-npm.png` | Node.js and npm installation and version verification. |
| [ ] | MCP Inspector startup | Inspector launch terminal | `evidence/02-inspector-start.png` | MCP Inspector startup for the authorized local server. |
| [ ] | Inspector connection | Local UI and connected server | `evidence/03-inspector-connected.png` | MCP Inspector connected to the authorized sample MCP server. |
| [ ] | Capability inventory | Inspector capabilities and generated JSON/Markdown | `evidence/04-inventory.png` | Complete MCP capability inventory. |
| [ ] | Attack surface map | Editable map with observed capabilities and risk | `evidence/05-attack-surface.png` | MCP attack-surface assessment. |
| [ ] | Tool injection | Prompt, tool attempt, and response | `evidence/06-tool-injection.png` | Controlled tool-injection test. |
| [ ] | Resource poisoning file | Disposable resource and benign marker | `evidence/07-resource-poisoning.png` | Controlled resource-poisoning setup. |
| [ ] | Resource poisoning response | Read prompt and model response | `evidence/08-resource-response.png` | Resource-poisoning behavior test. |
| [ ] | Capability chain step 1 | Tool A request and output | `evidence/09-chain-step1.png` | Capability-chain first step. |
| [ ] | Capability chain step 2 | Tool B request and output | `evidence/10-chain-step2.png` | Capability-chain second step. |
| [ ] | Burp request | Sanitized raw request and MCP payload | `evidence/11-burp-request.png` | Authorized local MCP request in Burp. |
| [ ] | Burp response | Sanitized response and status | `evidence/12-burp-response.png` | Authorized local MCP response in Burp. |
| [x] | Results JSON | `project4_results.json` | `evidence/13-results-json.png` | Structured Project 4 results. |
| [x] | Final report | `PROJECT4_REPORT.md` | `evidence/14-final-report.png` | Project 4 assessment report. |

Unchecked items require the sample server or manual GUI capture. No screenshots were taken or claimed by automation.
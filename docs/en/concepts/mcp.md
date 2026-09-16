---
title: Model Context Protocol
validated_date: 2026-09-16
i18n-key: concepts-mcp
last-synced: 2026-09-16
---

# Model Context Protocol

Model Context Protocol, or MCP, is a standard way for LLM applications to connect to servers that expose tools, resources, prompts, schemas, and external context.

## What MCP Solves

Before MCP-style boundaries, every app often rewired its own tools: schema, auth, logging, retries, error handling, and UI prompts were local and inconsistent. MCP gives the integration a shared shape.

It helps teams answer:

- What tools or resources are available?
- What input schema does each tool expect?
- Who can call a tool?
- What evidence or error came back?
- How do we audit and debug the call?

## Core Roles

| Role | What It Does | Example |
| --- | --- | --- |
| MCP Host | The app or runtime that contains the Agent | Chat app, IDE assistant, workflow runner |
| MCP Client | Connects the host to one or more servers | In-process client or stdio client |
| MCP Server | Exposes capabilities to the client | Search server, file server, database server |
| Tool | An action the server can perform | `search_docs`, `create_ticket`, `read_file` |
| Resource | A readable data source | File, URL, table, workspace file |
| Prompt | A reusable prompt template | `summarize_issue`, `review_pr` |

```mermaid
flowchart LR
  Host[MCP Host / Agent App] --> Client[MCP Client]
  Client --> Server[MCP Server]
  Server --> Tools[Tools]
  Server --> Resources[Resources]
  Server --> Prompts[Prompts]
  Server --> Systems[External Systems]
```

## Deep Dive: MCP Capabilities

The current MCP specification is built around a small set of capabilities that clients and servers negotiate.

| Capability | Server Exposes | Client / Host Should Do |
| --- | --- | --- |
| Tools | Typed actions with JSON schemas | Validate, authorize, audit, and handle errors |
| Resources | Readable content with URIs | Treat as context/evidence, not instruction authority |
| Prompts | Reusable prompt templates | Track version and avoid silent behavior drift |
| Sampling | Requests for model completion | Gate by policy; do not let servers trigger uncontrolled model use |
| Roots | Workspace roots or allowed paths | Enforce path boundaries and tenant isolation |
| Elicitation | Request for missing human input | Surface as clarification or approval, never as hidden action |

MCP uses JSON-RPC-style request/response patterns over transports such as stdio or streamable HTTP. The important point is not the transport itself; it is that tools, resources, prompts, roots, and sampling become explicit contracts instead of ad-hoc app glue.

## Security Deep Dive

MCP expands access to files, tools, databases, and workflows. That means the host, server, and gateway must defend against:

- tool poisoning: a tool description or result tries to steer the model;
- prompt injection through resource content;
- confused deputy attacks where a trusted host calls the wrong server action;
- data exfiltration through over-broad resources;
- excessive permissions through lazy allowlists;
- missing audit trails for destructive tool calls.

Practical controls:

- keep sensitive data out of the model context unless needed;
- use path, tenant, and actor boundaries in tool metadata;
- require human approval for irreversible tools;
- log schema validation, permission checks, server response, and final action;
- pin or review MCP server versions before production use;
- test with hostile tool descriptions and poisoned resource content.

## Operational Deep Dive

For production MCP:

- Treat each server as a service with owner, version, SLA, and rollback path.
- Monitor tool-call latency, failure rate, permission denials, and schema errors.
- Keep MCP server changes behind review because tool schemas affect model behavior.
- Evaluate prompt/tool drift when server prompts or tool descriptions change.
- Add regression tests for unknown tool, invalid payload, denied permission, and unreachable server.

## MCP vs Function Calling

Function calling is a model capability: the model proposes a tool call with a name and JSON arguments.

MCP is a system boundary around that capability.

| Layer | Question | Example |
| --- | --- | --- |
| Function calling | Which tool should the model request? | `search_docs({"query": "refund"})` |
| Schema validation | Are the arguments valid? | `query` must be a non-empty string |
| MCP server | What capabilities are exposed? | tools, resources, prompts, metadata |
| Tool gateway | Is the call authorized and audited? | actor, tenant, permissions, logs |
| Agent runtime | How does the result affect the next step? | answer, retry, clarify, escalate |

MCP does not replace the model, the Agent loop, or production guardrails. It makes tool and context integration easier to inspect.

## What MCP Does Not Do

MCP is not:

- automatic authorization;
- a safety policy;
- a memory system;
- a RAG engine;
- a framework;
- a guarantee that tool results are true.

Permissions, audit, retry policy, rollback, rate limits, and data retention still need to be designed explicitly.

## How to Use MCP in Agent-Top

Agent-Top uses MCP-style ideas in Labs without requiring a live server:

- `list_tools()` exposes available capabilities.
- `call_tool()` enforces a tool name and payload boundary.
- Guardrails run before side-effecting tools.
- Tool output is treated as evidence, not final truth.

Read the L2 tutorial: [`../l2-single-agent-mcp.md`](../l2-single-agent-mcp.md).

## Debugging Checklist

When MCP-style integration fails:

1. Is the server reachable?
2. Does the tool name exist?
3. Does the payload match the schema?
4. Does the actor have permission?
5. Did the external system return an error?
6. Did the Agent interpret the result correctly?
7. Is the trace complete enough to reproduce the call?

## Related Links

- Tool/MCP safety skill card: [`../skills/tool-mcp-safety.md`](../skills/tool-mcp-safety.md)
- Lab: [`../../labs/l2/single_agent_mcp/README.md`](../../../labs/l2/single_agent_mcp/README.md)


## Sources

- Model Context Protocol Specification 2025-06-18: https://modelcontextprotocol.io/specification/2026-07-29
- MCP Security Best Practices: https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices

---
title: Tool/MCP Safety Skill Card
validated_date: 2026-09-16
i18n-key: skill-card-tool-mcp-safety
last-synced: 2026-09-16
---

# Tool/MCP Safety Skill Card

## Skill Name

- English: Tool and MCP Safety
- Chinese: 工具与 MCP 安全边界
- Level: L2-L4

## Purpose

Help engineers expose external actions through a controlled boundary, including validation, permissions, confirmation, traces, and rollback.

## When to Use

- The Agent can read or write external state.
- A tool call has side effects.
- Permissions, idempotency, or audit requirements matter.
- You need to explain why a tool call failed without leaking sensitive data.

## When Not to Use

- The task is a pure single-shot LLM answer.
- The tool is read-only and the blast radius is negligible.
- You are only learning prompt formatting.

## Core Knowledge

- Tool contracts: inputs, outputs, errors, and side effects.
- Read/write/destructive risk classification.
- MCP boundaries: host/client/server model, tools/resources/prompts, schemas, transport, auth, and audit.
- MCP is not a permission system by itself; permissions and audit belong in your gateway, server, or policy layer.
- Confirmation and human-in-the-loop routes.
- Idempotency, retries, and rollback.

## Practice Evidence

- Lab: [`../../../labs/l2/single_agent_mcp/README.md`](../../../labs/l2/single_agent_mcp/README.md)
- Example: [`../../../examples/mcp-tool-boundary/README.md`](../../../examples/mcp-tool-boundary/README.md)
- Case: [`../cases/enterprise-multi-tool-agent.md`](../cases/enterprise-multi-tool-agent.md)
- Project artifact: tool gateway design note with risk table and audit fields.

## Review Questions

1. How do you classify a tool call before execution?
2. What should happen when a tool result is empty but not an error?
3. How do you prevent the same destructive action from running twice?

## Common Failure Modes

- Treating model output as an authorization decision.
- Logging sensitive request payloads.
- Allowing retry after a write tool succeeds but response parsing fails.
- Missing tenant or actor context in the audit log.

## Production Notes

- Use a gateway for validation, permissions, and audit.
- Put rate limits and mutation gates close to tool execution.
- Prefer idempotency keys for side-effecting tools.
- Add regression evals for denied, retried, and partially successful calls.

## Related Links

- Tutorial: [`../l2-single-agent-mcp.md`](../l2-single-agent-mcp.md)
- Template: [`../../../templates/agent-skill-card-template.md`](../../../templates/agent-skill-card-template.md)

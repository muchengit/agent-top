---
title: MCP Tool Boundary
capability_level: Example
validated_date: 2026-09-18
tested_against: "review of synthetic MCP server and tool-call evidence"
---

# MCP Tool Boundary Exercise

This exercise uses fictional MCP tool decisions. No API key, MCP server, browser, vector database, or external connector is needed.

Goal: decide whether each tool call is ready to execute, must be blocked, or needs a safer state/checkpoint before continuing.

## Files

- [`tool-call-evidence.jsonl`](tool-call-evidence.jsonl): fictional MCP and graph-state decisions.

## JSONL Shape

Common fields: `event`, `trace_id`, `server_id`, `tool_name`, `input_schema_version`, `permission_scope`, `transport_lifecycle`, `audit_actor`, `result_status`, `decision`. Optional event-specific fields may include `graph_checkpoint`, `schema_error`, and `visible_context`.

## Steps

1. Read each tool decision event.
2. Mark whether the call is ready to execute.
3. Identify the owner: `mcp`, `graph`, `tool`, `guardrail`, `runtime`, or `release`.
4. Choose the next action: `execute`, `block`, `clarify`, `checkpoint`, `schema_fix`, or `postmortem`.
5. For each blocked event, add one missing evidence field.

## Answer Key

| Finding | Owner | Next action |
| --- | --- | --- |
| Destructive tool lacks approval actor | mcp | block |
| Graph transition lacks checkpoint id | graph | checkpoint |
| Tool output failed schema validation | tool | schema_fix |
| Browser write action lacks visible context | guardrail | clarify |

## Extended Exercises

1. Design a follow-up trace that exercises the same pattern against the [mcp2 reference material](../../labs/l2/mcp_tool_selection/README.md).
2. Swap the target scenario for a different domain and list the three decisions that would change.

## Reuse

Copy a `*.template.jsonl` file to a scratch file, fill it in while working through the steps, then re-read it as a decision log. To validate that every JSONL file stays legal JSON, run `python scripts/check_repository.py` from the repository root (its `check_examples_jsonl` step also runs in CI). To practice a different policy, change one rule, redo the answers, and compare outcomes.

## Learning Outcomes

- MCP servers expose tools; they do not make those tools safe by default.
- Tool calls need permission, schema, lifecycle, actor, and result-status evidence.
- Graph state should be checkpointed before irreversible or expensive transitions.
- Typed output validation belongs before downstream state mutation.

## Related Reading

- [`../../docs/en/skills/tool-mcp-safety.md`](../../docs/en/skills/tool-mcp-safety.md)
- [`../../docs/en/production/safety-checklist.md`](../../docs/en/production/safety-checklist.md)
- [`../../docs/en/tutorials/open-source-pattern-matrix.md`](../../docs/en/tutorials/open-source-pattern-matrix.md)

# MCP Tool Boundary Exercise

This exercise uses fictional MCP tool decisions. No API key, MCP server, browser, vector database, or external connector is needed.

Goal: decide whether each tool call is ready to execute, must be blocked, or needs a safer state/checkpoint before continuing.

## Files

- [`tool-call-evidence.jsonl`](tool-call-evidence.jsonl): fictional MCP and graph-state decisions.

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

## Learning Outcomes

- MCP servers expose tools; they do not make those tools safe by default.
- Tool calls need permission, schema, lifecycle, actor, and result-status evidence.
- Graph state should be checkpointed before irreversible or expensive transitions.
- Typed output validation belongs before downstream state mutation.

## Related Reading

- [`../../docs/en/skills/tool-mcp-safety.md`](../../docs/en/skills/tool-mcp-safety.md)
- [`../../docs/en/production/safety-checklist.md`](../../docs/en/production/safety-checklist.md)
- [`../../docs/en/tutorials/open-source-pattern-matrix.md`](../../docs/en/tutorials/open-source-pattern-matrix.md)

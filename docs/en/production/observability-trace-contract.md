---
title: Observability And Trace Contract
validated_date: 2026-09-17
i18n-key: production-observability-trace-contract
last-synced: 2026-09-17
---

# Observability And Trace Contract

Observability is not just logging. For an Agent system, observability is the contract that says: when something changes, we can identify what the user asked, what evidence the Agent saw, what tools ran, what guardrails were checked, what answer shipped, and how much it cost.

This page gives a stable trace contract for Agent systems. It is framework-neutral and can be implemented with Langfuse, OpenTelemetry GenAI attributes, promptfoo-style eval reports, internal logs, or a simple local JSONL file.

## Why This Contract Exists

A useful demo produces an answer. A production Agent has to answer, explain, verify, recover, and improve. Traces are the evidence layer that connects those activities.

Without a trace contract:

- Postmortems become arguments about memory instead of reviewable evidence.
- Bad prompts look like model failures.
- Tool bugs look like planning bugs.
- Retrieval misses look like hallucination.
- Cost regressions are discovered after billing.
- Safety incidents cannot be reproduced.

With a trace contract:

- Every decision can be replayed.
- Every failure can be routed to the right owner.
- Every incident can become an eval, guardrail, trace field, or rollback rule.

## Trace Scope

A trace should cover one user-visible request, even if it contains multiple turns, tools, retrieval calls, memory writes, and retries.

Required levels:

| Level | Example | Required? |
| --- | --- | --- |
| Request | user query, session id, tenant, locale | Yes |
| Plan | steps considered, selected action, stop condition | Yes for non-trivial Agent systems |
| Retrieval | query, source ids, freshness, permission state | Yes when RAG or evidence is used |
| Tool | tool name, version, parameters, result, latency | Yes when tools run |
| Guardrail | check name, verdict, matched policy, remediation | Yes for safety-relevant actions |
| Memory | read/write/delete operation, owner, reason | Yes when memory is involved |
| Answer | final text, citations, refusal reason, confidence | Yes |
| Runtime | model, prompt version, latency, tokens, cost | Yes for production |
| Incident | root cause, owner, rollback, follow-up eval | Required after incidents |

## Stable Event Types

Use stable event names so traces can be filtered and compared over time:

- `request.received`
- `plan.selected`
- `retrieval.queries`
- `retrieval.results`
- `tool.called`
- `tool.result`
- `guardrail.checked`
- `memory.read`
- `memory.write`
- `memory.deleted`
- `answer.generated`
- `answer.delivered`
- `error.raised`
- `release.gate.checked`
- `runtime.evidence.checked`

## Required Fields

At minimum, every trace should include:

```json
{
  "trace_id": "stable request id",
  "session_id": "user or conversation id",
  "tenant_id": "workspace or account scope",
  "request": "normalized user request",
  "prompt_version": "system/user prompt version",
  "model": "model name and setting",
  "plan": "selected steps and stop condition",
  "tools": [],
  "retrievals": [],
  "guardrails": [],
  "memory": [],
  "answer": {
    "text": "final answer",
    "citations": [],
    "refusal_reason": "none or reason"
  },
  "latency_ms": 0,
  "tokens": {},
  "cost": {},
  "status": "ok|blocked|error|escalated"
}
```

Do not store raw secrets, full private records, or unredacted customer data in traces. Store source identifiers, policy names, and bounded excerpts instead.

## PII And Privacy Rules

- Redact secrets before they enter trace storage.
- Keep raw customer data out of default traces.
- Store only evidence needed for diagnosis: source id, timestamp, permission state, policy name, and bounded excerpt.
- Mark sensitive fields with a retention class.
- Allow deletion propagation: when user data is deleted, delete or expire associated trace evidence.

## Ownership By Failure Type

Use trace fields to route incidents quickly:

| Failure | Owner | First fields to inspect |
| --- | --- | --- |
| Missing citation | Retrieval or answer policy | `retrieval.results`, `answer.citations` |
| Tool called without approval | Tool policy or MCP boundary | `tool.called`, `guardrail.checked` |
| Wrong memory preference | Memory lifecycle | `memory.read`, `memory.write` |
| Prompt regression | Prompt owner | `prompt_version`, eval fixture result |
| Cost spike | Runtime or planner | `tokens`, `cost`, `plan.selected` |
| Missing release evidence | Release owner | `release.gate.checked`, CI SHA, dataset version, rollback plan |
| Runtime evidence missing | Runtime or release owner | `runtime.evidence.checked`, tool version, artifact SHA, decision |


## Runtime Evidence

`runtime.evidence.checked` keeps release and incident evidence separate from raw telemetry, but still tied to one trace. Use it when a release gate depends on lint, profiling, dependency lock, workflow provenance, or error grouping.

Required fields:

```json
{
  "event": "runtime.evidence.checked",
  "trace_id": "stable request id",
  "source": "lint|profile|lockfile|workflow|error-group|ci",
  "tool": "tool name",
  "tool_version": "exact version or commit",
  "artifact_sha": "artifact, lockfile, profile, or run id",
  "release_sha": "commit being released",
  "finding": "finding or metric summary",
  "decision": "release|block|warn|route",
  "owner": "runtime|release|prompt|tool|retrieval|memory|guardrail"
}
```

Use the evidence to answer: can this release be replayed with the same tools? Can this incident be grouped with similar incidents? Can this cost or latency hotspot be tied to a commit, tool, or workflow step?

## Release Gate

A production release should fail if:

- A required trace field is missing.
- Trace retention or redaction policy is undefined.
- Tool calls do not include risk classification.
- Retrieval results do not include source version or permission state.
- Final answers do not link evidence for factual claims.
- Cost and latency are not captured per request.

## What Good Looks Like

A good Agent trace lets a teammate answer these questions without asking the model again:

1. What did the user ask?
2. What evidence was available?
3. Which tools ran?
4. Which policy allowed or blocked each action?
5. What did the Agent answer?
6. What did it cost?
7. What changed between the last working version and this version?
8. What eval, guardrail, or rollback action prevents recurrence?

## Related

- [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md)
- [`evals-playbook.md`](evals-playbook.md)
- [`safety-checklist.md`](safety-checklist.md)
- [`../../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md)
- [`../../../templates/observability-trace-template.md`](../../../templates/observability-trace-template.md)

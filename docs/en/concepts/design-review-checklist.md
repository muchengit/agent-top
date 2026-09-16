---
title: Agent Design Review Checklist
validated_date: 2026-09-16
i18n-key: concepts-design-review-checklist
last-synced: 2026-09-16
---

# Agent Design Review Checklist

Use this checklist to review Agent designs before implementation, code review, launch, or interview preparation.

## 0. Review Output

A good review ends with four decisions:

- **Approve**: safe to build or ship with normal monitoring.
- **Approve with conditions**: ship after named follow-ups and owners.
- **Rework**: architecture has unresolved correctness, safety, or maintainability risks.
- **Stop**: task does not need an Agent, or risks are unacceptable.

Review template:

```markdown
# Agent Design Review

## Scope
- User:
- Business goal:
- Non-goals:

## Decision
- Verdict: Approve / Approve with conditions / Rework / Stop
- Required conditions:
- Owners and dates:

## Evidence
- Eval plan:
- Safety controls:
- Observability plan:
- Rollback plan:
- Cost and latency budget:
```

## 1. Requirements and Non-Goals

Ask:

- Who is the user, and what task must be completed?
- What does success look like in one measurable sentence?
- What is explicitly out of scope?
- What happens when the Agent is uncertain?
- What happens when the right action is irreversible?

Red flags:

- The goal is “make an AI” without a task-level success metric.
- The system is expected to handle safety, policy, or permissions only through prompts.
- There is no refusal path.

## 2. System Shape

Choose the smallest shape that works:

| Shape | Use when | Avoid when |
| --- | --- | --- |
| Single LLM call | The answer is direct and no external state is needed | Evidence, tools, or side effects are needed |
| ReAct loop | The Agent needs to inspect tool results and adapt | Tool results are untrusted and no verifier exists |
| RAG Agent | Answers depend on private, current, or large documents | Retrieval quality cannot be measured |
| Tool-using Agent | The Agent must query or modify external systems | Permission and audit boundaries are unclear |
| Multi-agent system | Specialization, verification, or isolation materially helps | A single Agent with tools is enough |

Red flags:

- Multi-agent complexity is added before a single-Agent failure is diagnosed.
- The orchestrator owns too little: it cannot stop, verify, or escalate.
- Agents share mutable state without an owner.

## 3. Component Boundaries

For every component, document:

- Owner.
- Inputs.
- Outputs.
- Required permissions.
- Failure modes.
- Observability fields.
- Rollback path.

Minimum boundaries for production Agents:

- Gateway: auth, rate limits, request size limits.
- Planner: stop conditions, max steps, budget awareness.
- Tool gateway: schema validation, allowlist, audit logs.
- Retriever: scope, freshness, citation contract.
- Memory: extraction, deduplication, expiry, deletion.
- Verifier: evidence checks, output policy, escalation.
- Evaluator: golden prompts, safety evals, regression gates.

## 4. Data Flow and Context Ownership

Map each fact type to its source:

| Fact type | Preferred source | Do not trust blindly |
| --- | --- | --- |
| Current user instruction | User turn | Old memory |
| Private knowledge | Scoped RAG | Model parametric memory |
| External state | Tool call | Cached prompt context |
| User preference | Memory | Unconfirmed inference |
| Safety decision | Guardrail or approval | Final model text |

Review questions:

- Can the final answer say where each fact came from?
- Can stale memory be detected and excluded?
- Can tool results conflict with retrieved documents?
- Is there a conflict-resolution rule before answering?

## 5. Tool and MCP Design

Before adding a tool, define:

- Tool name and one-line purpose.
- Input schema and output schema.
- Read-only, write, or destructive classification.
- Authentication and tenant scoping.
- Idempotency behavior.
- Timeout and retry policy.
- Audit fields.

Red flags:

- Tools are described only in prompt text, not as validated schemas.
- Destructive actions can be called without confirmation.
- Tool errors are converted into user-facing answers without explanation.

## 6. Safety, Permissions, and Abuse Cases

Review at least these risks:

- Prompt injection through retrieved documents or tool results.
- Cross-tenant data retrieval.
- Overprivileged tools.
- Hidden side effects in write actions.
- Memory poisoning.
- Infinite escalation or retry loops.
- Sensitive output leakage.

Required controls:

- Auth checks before retrieval.
- Auth checks before tool execution.
- Tool allowlist and risk classification.
- Explicit approval for destructive actions.
- Output validation when evidence or citations are required.
- Rate and cost limits per user and tenant.

## 7. Evaluation Before Implementation

Define evals before choosing the final prompt:

- Golden prompts for core journeys.
- Negative cases where the Agent should refuse.
- Tool-usage cases with invalid or missing parameters.
- Retrieval cases with stale, missing, and conflicting sources.
- Safety cases for injection, privilege escalation, and destructive action.
- Ambiguous requests that require clarification.

Release gate:

- Safety failures block release.
- Missing trace fields block release.
- Missing rollback plan blocks release.
- Cost or latency over budget requires explicit approval.

## 8. Observability Contract

Every request should be traceable by:

- Request ID and user/tenant ID.
- Prompt version and model version.
- Planner decisions and stop reason.
- Tool calls, arguments, result status, and latency.
- Retrieved sources and freshness metadata.
- Memory reads and writes.
- Guardrail decisions.
- Final answer status.
- Token cost and total latency.

Incident requirement:

- A production incident must become one of: eval, guardrail, trace field, rollback path, or postmortem action.

## 9. Cost and Latency Budget

Budget the system before optimizing:

- Maximum steps per request.
- Maximum tool calls per request.
- p50 and p95 latency targets.
- Token budget per user, task, and tenant.
- Retry budget.
- Escalation budget.

Red flags:

- Retries can recurse indefinitely.
- Multi-agent routing lacks a maximum hop count.
- RAG retrieval is unbounded by relevance or token budget.

## 10. Rollback and Change Management

For each major change, document:

- What can be rolled back: prompt, model, tool, retrieval index, memory policy, router.
- How users are protected during rollback.
- How traces identify affected requests.
- Who approves exception to release gates.

Rollback should restore known-safe behavior, not merely disable the failing feature.

## Review Rubric

| Area | Passing standard |
| --- | --- |
| Requirements | Clear user, task, success metric, non-goals |
| Shape | Smallest viable architecture selected |
| Boundaries | Each component has owner, inputs, outputs, failures |
| Data flow | Facts have source precedence and conflict rules |
| Tools | Schemas, permissions, audit, idempotency are defined |
| Safety | Injection, privilege, memory, and destructive risks are handled |
| Evals | Correctness, safety, retrieval, tool, and regression cases exist |
| Observability | Request can be replayed from traces |
| Cost/latency | Budgets and caps are explicit |
| Rollback | Known-safe path exists before launch |
| Postmortem | Incidents become prevention assets |

## Final Questions

Before approving:

- Could this be simpler?
- Could the Agent cause harm it cannot undo?
- Could the Agent answer confidently without evidence?
- Could a bad prompt or model change silently degrade safety?
- Could an incident be investigated with current traces?
- Is there a clear reason to use Agent architecture instead of a normal workflow?

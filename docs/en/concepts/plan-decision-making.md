---
title: Plan and Decision Making
validated_date: 2026-09-16
i18n-key: concepts-plan-decision-making
last-synced: 2026-09-16
---

# Plan and Decision Making

Planning is the Agent decision layer: choosing the next step, assigning tools or agents, and deciding when to stop.

## Planning vs Acting

Planning says what should happen next. Acting performs a specific step.

- Plan: retrieve policy, then verify rollback path.
- Act: call `read_policy(policy_id="...")`.

Good systems keep these separate so plans can be inspected before side effects happen.

## Decision Inputs

A plan should consider:

- User goal and constraints.
- Evidence available so far.
- Tool availability and permissions.
- Risk and reversibility.
- Budget: tokens, latency, API calls.
- Stop conditions.

## Decision Outputs

A decision should produce:

- Next action.
- Reason for the action.
- Expected evidence.
- Risk level.
- Stop condition.
- Fallback if the action fails.

```mermaid
flowchart TD
  G[Goal] --> C[Collect Evidence]
  C --> P[Plan Step]
  P --> Risk[Risk Check]
  Risk --> Act[Act]
  Act --> Obs[Observe]
  Obs --> P
  Obs --> Stop[Stop / Answer]
```

## Decision Types

| Decision | Question | Safe Default |
| --- | --- | --- |
| Clarify | Is the goal ambiguous? | Ask before acting |
| Retrieve | Is current/private evidence needed? | Use RAG before claiming |
| Tool call | Is an external action needed? | Validate and audit |
| Delegate | Does another agent own this step? | Use scheduler contract |
| Verify | Is the claim evidence-heavy? | Add verifier |
| Stop | Is the answer ready? | Stop when evidence is enough |

## Common Planning Failures

- The plan repeats the same failed tool call.
- The plan confuses a recommendation with permission.
- The plan skips verification for an important claim.
- The plan hides uncertainty.
- The plan has no maximum depth or budget.
- The plan executes irreversible steps without human confirmation.

## Review Questions

1. Why was this next action chosen?
2. What evidence does it expect?
3. What happens if it fails?
4. What is the stop condition?
5. Should this step be verified or human-approved first?

## Deep Dive: Planning Patterns

Useful Agent planning patterns include ReAct, plan-and-execute, search-tree planning, reflection, hierarchical planning, and human-in-loop planning. ReAct is simple and debuggable. Search-tree planning can improve decisions but adds token cost, latency, and complexity.

## Decision Policy

A decision policy defines what an Agent may do without asking. Examples: read-only retrieval may run automatically; write actions require schema validation; destructive actions require human approval; cross-tenant actions are denied by default; missing evidence should clarify rather than guess; repeated tool failure should stop or escalate.

A good decision event includes reason, expected evidence, risk level, allowed tools, stop condition, and fallback.

## Avoiding Plan Hallucination

Plan hallucination happens when the Agent proposes impossible or unsafe next steps. Check whether the planned tool exists, whether the actor has permission, whether the action is reversible, whether the expected evidence is plausible, whether budget and stop conditions exist, and whether the same failed action has repeated.

## Sources

- LangGraph plan-and-execute tutorial: https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/plan-and-execute/
- LlamaIndex planner documentation: https://developers.llamaindex.ai/python/framework/understanding/agent/agent_planner/
- LangGraph multi-agent planning blog: https://www.langchain.com/blog/optimizing-multi-agent-planning-with-search-tree

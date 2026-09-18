---
title: Interview Framework
validated_date: 2026-09-18
i18n-key: interviews-interview-framework
last-synced: 2026-09-18
---

# Interview Framework

Agent interviews should measure whether a candidate can build reliable Agent systems, not whether they can recite framework names.

## Interview Design Principles

- Test trade-offs, not slogans.
- Move from concept to implementation to debugging to system design.
- Prefer concrete systems over abstract definitions.
- Ask for evidence: evals, traces, postmortems, and follow-up work.
- Give room for assumptions; production interviews are about reasoning under incomplete information.

## Capability Matrix

| Level | Concept | Implementation | Debugging | Design |
| --- | --- | --- | --- | --- |
| L0 | Prompt, tokens, context window, model output vs final response | Prompt rewrite | Bad response debugging | Baseline screening |
| L1 | Perception, planning, tools, memory | Minimal ReAct loop | Failed tool loop | Single-agent shape |
| L2 | Framework fit and tool boundaries | Guardrailed single Agent | MCP failure handling | Tool routing |
| L3 | RAG, memory, MCP, and multi-agent flow | End-to-end pipeline | Retrieval misses and stale memory | Customer support system |
| L4 | Evals, observability, safety, rollback | Regression suite | Incident triage | Cost / latency / safety |
| L5 | Original patterns and ecosystem choices | Framework or pattern design | Cross-team failure mode | Ecosystem strategy |

## Question Types

### Concept

Concept questions check vocabulary and boundaries.

Example:

- What is the difference between short-term and long-term memory in an Agent?

What interviewers should hear:

- Short-term memory is conversation or task state.
- Long-term memory is durable, scoped, and privacy-sensitive.
- Memory can be wrong, stale, or over-extracted.

### Implementation

Implementation questions check whether candidates can turn ideas into small systems.

Example:

- Add a max-step limit and ambiguous-tool-result handling to a ReAct loop.

What interviewers should hear:

- The stop condition prevents infinite loops.
- Ambiguous feedback should trigger clarification or a fallback plan.
- The system emits enough state to debug failure.

### Debugging

Debugging questions check operational reasoning.

Example:

- A user says the Agent gave the wrong answer. What do you inspect first?

What interviewers should hear:

- Identify request, trace, prompt, retrieved context, tool calls, and final answer.
- Check whether failure came from retrieval, tool execution, model generation, or memory.
- Add a regression eval before reopening normal release flow.

### Design

Design questions check architecture judgment.

Example:

- Design a multi-agent customer support system.

What interviewers should hear:

- Requirement decomposition.
- Component boundaries.
- Tool permissions.
- Error isolation.
- Observability.
- Cost and latency budget.

## System Design Question

Use this as the default L3-L4 system design prompt:

> Design a multi-agent customer support system that can answer product questions, look up order status, update a support ticket, and escalate unsafe or ambiguous cases to a human.

Recommended structure:

1. Clarify constraints: traffic, latency, accuracy, safety, privacy, cost.
2. Define user journeys: simple answer, tool action, ticket update, escalation.
3. Choose architecture: router, retrieval agent, tool agent, verification agent, escalation path.
4. Define data ownership: user session, policy documents, ticket system, audit log.
5. Define trust boundaries: authentication, authorization, tool allowlists, irreversible action confirmation.
6. Define observability: trace every planning decision, tool call, retrieved source, and final answer.
7. Define evals: correctness, refusal, tool accuracy, escalation accuracy, latency, cost.
8. Define rollback: disable risky tool path, fall back to read-only mode, route to human review.

## Scoring Rubric

### L0 Baseline

Weight:

- 40% explains prompt, context, and token basics.
- 30% can debug a bad response from a small trace.
- 30% can separate model output from final user response.

### L1 Component Understanding

Weight:

- 40% clear definition of perception, planning, tools, memory.
- 30% can explain a minimal loop.
- 30% can identify stop conditions.

### L2 Reliable Single Agent

Weight:

- 30% explains framework trade-offs.
- 30% designs guardrails.
- 20% handles tool failure.
- 20% can evaluate a single-agent behavior.

### L3 End-to-End System

Weight:

- 25% retrieval and memory boundaries.
- 25% multi-agent decomposition.
- 20% error isolation.
- 20% observability.
- 10% evaluation design.

### L4 Production

Weight:

- 25% incident response.
- 25% root cause and prevention.
- 20% eval and regression process.
- 20% rollback and cost/latency controls.
- 10% ownership and communication.

### L5 Expert

Weight:

- 30% original pattern or framework reasoning.
- 25% cross-team failure modes.
- 20% ecosystem and framework selection.
- 15% contribution evidence.
- 10% mentorship or standard-setting.

At L5, candidates should also show spec-first drafting: a one-sentence goal/interface/acceptance spec before prompting, verified by the [Vibe Coding workflow](../vibe-coding/README.md) and its [`vibe_coding_spec` Lab](../../../labs/l5/vibe_coding_spec/README.md).

## Answer Framework

See [`interview-answer-framework.md`](interview-answer-framework.md) for candidate-facing response structure and examples.

## STAR Template

- Situation: context, constraints, users affected, and system boundaries.
- Task: what you owned, what you did not own, and what decisions were required.
- Action: architecture, tools, evals, safety controls, rollout, and rollback.
- Result: metric, incident outcome, learning, and follow-up contribution.

## Portfolio Evidence

Ask candidates to map each claim to one of four project gradients:

1. Personal Knowledge Base Agent: proves RAG and memory.
2. Enterprise Multi-Tool Agent: proves tool and MCP-style orchestration.
3. Multi-Agent Collaboration System: proves orchestration, consistency, and failure isolation.
4. Custom Framework or Pattern: proves abstraction, engineering depth, and contribution readiness.

## Common Red Flags

- Framework name used instead of reasoning.
- No mention of failure or rollback.
- Evals treated as optional.
- Safety checks only in the final prompt.
- Tool calls assumed trusted.
- Memory treated as always correct.
- Cost and latency mentioned only after repeated prompting.

## Related Question Sets

- [`questions/l0-basics.md`](questions/l0-basics.md)
- [`questions/l1-components.md`](questions/l1-components.md)
- [`questions/l2-framework-mcp.md`](questions/l2-framework-mcp.md)
- [`questions/l3-system-design.md`](questions/l3-system-design.md)
- [`questions/l4-production.md`](questions/l4-production.md)
- [`questions/l5-patterns.md`](questions/l5-patterns.md)
- [`interview-answer-framework.md`](interview-answer-framework.md)

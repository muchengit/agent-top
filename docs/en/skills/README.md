---
title: Agent Skills Matrix
validated_date: 2026-09-16
i18n-key: skills-matrix
last-synced: 2026-09-16
---

# Agent Skills Matrix

This page turns the L0-L5 capability model into concrete skills, knowledge areas, and verifiable evidence.

## How to Use This Matrix

- Use it to plan learning paths.
- Use it to build a portfolio.
- Use it to scope interview prep.
- Use it to propose new Labs or cases.

## Skills by Level

| Level | Knowledge | Skills | Evidence |
| --- | --- | --- | --- |
| L0 | LLM request shape, tokens, prompts, context window | Make a first call, explain limits, avoid API overfitting | API demo, prompt notes, terminology quiz |
| L1 | Perception, tools, planning, memory, ReAct | Build a minimal Agent, validate tool args, add stop conditions | ReAct Lab, multi-turn state Lab, explanation of components |
| L2 | Framework boundaries, MCP-style tools, cost-aware routing | Design a reliable single Agent, compare frameworks, debug tool calls | Single Agent project, framework notes, MCP Lab evidence |
| L3 | RAG, memory, multi-agent, observability, research flow | Build end-to-end systems, evaluate retrieval, isolate multi-agent state | RAG evaluator, memory flow notes, Langfuse-style trace report |
| L4 | Production ops, evals, safety, rollback, incidents | Run production gates, postmortems, guardrails, cost/latency budgets | Regression gate, postmortem, production checklist evidence |
| L5 | Patterns, contribution, external influence | Define reusable patterns, write design docs, open source PRs or talks | Pattern catalog entry, design doc, PR, talk, or article |

## Skill Categories

| Category | What It Measures | Example Evidence |
| --- | --- | --- |
| Concepts | Can you explain stable Agent ideas clearly? | Teaching notes, glossary entries, diagrams |
| Code | Can you implement deterministic behavior? | Labs, tests, runnable snippets |
| Architecture | Can you choose the right pattern? | Design docs, trade-off analysis |
| Tools | Can you handle tool/MCP boundaries safely? | Tool contracts, permissions, logs |
| Evaluation | Can you measure quality? | Evals, regression checks, dashboards |
| Safety | Can you prevent harm? | Guardrails, confirmations, postmortems |
| Production | Can you run a real system? | Release gates, rollback, incident evidence |
| Contribution | Can you improve the ecosystem? | PRs, pattern docs, talks, guides |

## Suggested Skill Evidence Packs

1. **L0-L1 Starter Pack**
   - First LLM call Lab.
   - Minimal ReAct Agent Lab.
   - 5-question concept quiz.

2. **L2 Reliable Agent Pack**
   - Single Agent with tool boundary.
   - Framework comparison notes.
   - Cost-aware routing Lab.

3. **L3 System Pack**
   - RAG evaluator Lab.
   - Multi-agent supervisor Lab.
   - Trace/eval report.

4. **L4 Production Pack**
   - Regression gate Lab.
   - Production postmortem Lab.
   - Production checklist completion.

5. **L5 Impact Pack**
   - Custom pattern Lab.
   - Pattern catalog Lab.
   - Open-source contribution or design article.

## Contribution Guide

When adding a new skill:

1. State which level it belongs to.
2. Add at least one verifiable evidence item.
3. Link the relevant Lab or case.
4. Explain common failure modes.
5. Keep framework-specific details in Labs.

See: [`../../templates/agent-skill-card-template.md`](../../../templates/agent-skill-card-template.md)

---
title: Agent Skills Guide
validated_date: 2026-09-16
i18n-key: skills-matrix
last-synced: 2026-09-16
---

# Agent Skills Guide

This page explains what an Agent skill is, how to use skills to learn and build, and what practical outcomes they produce.

## What Is an Agent Skill?

An Agent skill is a repeatable ability that helps you design, build, evaluate, operate, or contribute to Agent systems. It is not a framework name or a library trick. A good skill is stable, transferable, and provable.

A skill should answer four questions:

1. **What problem does it solve?**
2. **When should I use it?**
3. **How can I practice it?**
4. **What evidence proves I have it?**

A skill can live inside tutorials, Labs, cases, templates, or production guides. The Agent-Top skills section organizes those skills so they can be reused across learning, work, interviews, and contribution.

## How Skills Are Different From Framework Knowledge

Framework knowledge tells you how to use one API. Skill knowledge tells you how to solve Agent problems across frameworks.

Examples:

- Framework-specific: know how to call a LangGraph node.
- Skill-specific: know when to use explicit state, retries, checkpoints, and human review.
- Framework-specific: know how to install an MCP server.
- Skill-specific: know how to classify tool risk, add permissions, logs, and rollback.

Agent-Top prefers the second kind. Frameworks change; skills remain useful.

## How to Use Skills

- **Learn**: follow the skill level that matches your current capability.
- **Practice**: run the linked Lab or build the linked project.
- **Prove**: produce the evidence: notes, tests, traces, evals, or design docs.
- **Reuse**: turn a repeated workflow into a skill card.
- **Contribute**: propose new skills with a template, a Lab, or a case.

## What Skills Give You

- Clearer architecture choices instead of framework chasing.
- Faster debugging because failures map to missing skills or broken evidence.
- Better interviews because you can explain trade-offs and proof, not just buzzwords.
- Stronger portfolios because each project maps to a concrete capability.
- Safer production work because guardrails, evals, and postmortems become repeatable practices.
- Better open-source contribution because patterns can be extracted and reviewed.


## Anatomy of a Skill

A useful Agent skill has a simple structure:

| Part | Question | Example |
| --- | --- | --- |
| Purpose | What outcome does it produce? | Safe tool execution |
| Trigger | When should I apply it? | The Agent can write external state |
| Inputs | What information is required? | Tool schema, actor, permissions |
| Steps | What actions do I take? | Classify risk, validate args, execute, audit |
| Evidence | How do I prove it worked? | Tool log, eval, failed-tool test |
| Failure modes | What usually goes wrong? | Duplicate writes, leaked logs, unsafe retry |
| Trade-offs | What am I giving up? | Extra latency for safety |

## Turning Experience Into a Skill

A one-off fix is not a skill. Turn experience into a skill when the same problem appears more than once.

1. Name the problem: "tool writes may duplicate side effects."
2. Write the contract: inputs, outputs, failure modes, evidence.
3. Add practice: a Lab or case exercise.
4. Add proof: test, trace, eval, or checklist.
5. Add contribution notes: when to use it and when not to use it.

The template for this process is [`../../../templates/agent-skill-card-template.md`](../../../templates/agent-skill-card-template.md).

## Skill Levels and How to Learn Them

Use the matrix below as a map, not as a grade. Move forward when you can produce evidence.

## Capability Skills by Level

| Level | Knowledge | Skills | Evidence |
| --- | --- | --- | --- |
| L0 | LLM request shape, tokens, prompts, context window | Make a first call, explain limits, avoid API overfitting | API demo, prompt notes, terminology quiz |
| L1 | Perception, tools, planning, memory, ReAct | Build a minimal Agent, validate tool args, add stop conditions | ReAct Lab, multi-turn state Lab, explanation of components |
| L2 | Framework boundaries, MCP-style tools, cost-aware routing | Design a reliable single Agent, compare frameworks, debug tool calls | Single Agent project, framework notes, MCP Lab evidence |
| L3 | RAG, memory, multi-agent, observability, research flow | Build end-to-end systems, evaluate retrieval, isolate multi-agent state | RAG evaluator, memory flow notes, Langfuse-style trace report |
| L4 | Production ops, evals, safety, rollback, incidents | Run production gates, postmortems, guardrails, cost/latency budgets | Regression gate, postmortem, production checklist evidence |
| L5 | Patterns, governance, contribution, external influence | Define reusable patterns, package expert evidence, mentor reviewers, produce maintainable influence artifacts | Pattern catalog entry, L5 expert evidence bundle, design doc, PR, talk, or article |

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
   - Industry benchmark and L5 expert path.
   - Custom pattern Lab.
   - Pattern catalog Lab.
   - L5 expert evidence bundle.
   - Open-source contribution or design article.

## Example Skill Cards

- [`tool-mcp-safety.md`](tool-mcp-safety.md): L2-L4 Tool and MCP safety boundary skill card.

## Contribution Guide

When adding a new skill:

1. State which level it belongs to.
2. Add at least one verifiable evidence item.
3. Link the relevant Lab or case.
4. Explain common failure modes.
5. Keep framework-specific details in Labs.

See: [`../../templates/agent-skill-card-template.md`](../../../templates/agent-skill-card-template.md)

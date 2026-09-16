---
title: Personal Agent Portfolio Guide
validated_date: 2026-09-16
i18n-key: portfolio-personal-agent-portfolio
last-synced: 2026-09-16
---

# Personal Agent Portfolio Guide

A strong Agent portfolio proves you can design, build, evaluate, operate, and explain Agent systems.

## Portfolio Shape

Include two to four projects:

- **Personal knowledge Agent** — proves RAG, memory, citations, and refusal.
- **Enterprise tool Agent** — proves tool use, permissions, MCP-style boundaries, and error handling.
- **Multi-agent collaboration** — proves orchestration, verification, and consistency.
- **Original pattern or framework contribution** — proves abstraction, tests, and maintainability.

## Evidence for Each Project

Each project should include:

- Problem statement.
- User or customer.
- Non-goals.
- Architecture diagram.
- Design decisions and trade-offs.
- Evaluation plan.
- Safety controls.
- Observability plan.
- Cost and latency assumptions.
- Known failure modes.
- Rollback or degradation strategy.
- Demo video or reproducible commands.
- What would change at ten times more traffic.

## Project README Template

```markdown
# Agent Project Name

## Problem
What user problem does this solve?

## Scope
What is included and explicitly out of scope?

## Architecture
Diagram and component boundaries.

## Design Decisions
Why this pattern instead of a simpler or larger one?

## Evaluation
Datasets, metrics, negative cases, and release gates.

## Safety and Permissions
Tools, risks, guardrails, approvals, and refusals.

## Observability
Traces, logs, alerts, dashboards, and debugging workflow.

## Cost and Stability
Budgets, degradation modes, rollback path, and capacity assumptions.

## Demo
Commands, screenshots, or video link.

## Results
What worked, what failed, and what you changed.
```

## Narrative Quality Bar

A portfolio project should answer:

- What would break first?
- How do you know when it is wrong?
- How do you recover without human intervention?
- What data proves it is working?
- What did you deliberately not automate?

## Interview Ready Summary

For each project, prepare a one-minute version:

- Situation: business or learning problem.
- Task: Agent design responsibility.
- Action: architecture, evals, safety, and observability choices.
- Result: measurable behavior and trade-offs.

## Related Assets

- [`projects.md`](projects.md)
- [`../interviews/interview-framework.md`](../interviews/interview-framework.md)
- [`../production/evals-checklist.md`](../production/evals-checklist.md)
- [`../concepts/design-review-checklist.md`](../concepts/design-review-checklist.md)

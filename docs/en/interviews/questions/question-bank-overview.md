---
title: Interview Question Bank Overview
validated_date: 2026-09-17
i18n-key: interviews-questions-question-bank-overview
last-synced: 2026-09-17
---

# Interview Question Bank Overview

This page turns the Agent-Top interview assets into a working preparation map. It covers the current 21 questions across L1-L5 and defines what to add next.

## Current Coverage Matrix

| Level | Questions | Core Signal | Best Interview Use | Portfolio Evidence |
| --- | ---: | --- | --- | --- |
| L1 Components | 4 | ReAct, perception, tools, memory, stop conditions | Junior Agent engineer screening | Minimal ReAct Agent run |
| L2 Framework and MCP | 4 | Framework fit, tool boundaries, MCP failure handling, human approval | Mid-level implementation review | Enterprise Multi-Tool Agent |
| L3 System Design | 4 | RAG, memory, MCP, multi-agent routing, retrieval evals | Technical design interview | Personal Knowledge Base or Multi-Agent Collaboration |
| L4 Production | 5 | Release gate, incident response, model change, severity, cost/quality | Senior production review | Production postmortem and release gate |
| L5 Patterns | 5 | Reusable patterns, framework strategy, high-risk tools, docs health, OSS impact | Expert review and contribution readiness | Custom Framework or Pattern |

## Interview Bundles

### 45-Minute Agent Engineer Screen

Use when hiring for core implementation skills.

- L1: explain four Agent components.
- L1: why ReAct needs a max step limit.
- L2: good tool boundary.
- L2: debug MCP integration failure.
- Close with portfolio evidence: show one runnable ReAct or tool-use demo.

Pass signal: candidate separates perception, planning, tools, and memory; adds stop conditions; asks for failure logs before guessing.

### 60-Minute Mid-Level Technical Interview

Use when the role includes framework work, tool integration, or single-Agent reliability.

- L2: framework vs lightweight SDK.
- L2: human confirmation by risk.
- L3: RAG + memory + MCP data flow.
- L4: pre-release checklist.
- Follow-up: model version change as a release.

Pass signal: candidate chooses the simplest architecture that keeps failure modes explicit, and connects design choices to traces, evals, and rollback.

### 75-Minute Senior System Design

Use for production-facing Agent systems.

- L3: design multi-agent customer support.
- L3: evaluate retrieval agent before launch.
- L4: wrong account change incident.
- L4: cost/quality trade-off.
- L5: high-risk tool execution pattern.

Pass signal: candidate handles permissions, error isolation, observability, rollback, and prevention controls without being prompted.

### 90-Minute Expert Review

Use for L5, staff, principal, or open-source contributor review.

- L5: reusable Agent pattern value.
- L5: build vs use a framework.
- L5: prevent framework churn from destroying docs.
- L5: OSS contribution that proves expert capability.
- Add STAR: one production incident, one contribution, and one mentoring or review story.

Pass signal: candidate explains durable patterns, rejected alternatives, maintenance cost, and external evidence.

## Common Red Flags

- Names a framework before naming the system problem.
- Treats tool output as always trustworthy.
- Uses long-term memory without scope, freshness, privacy, or deletion.
- Adds multi-agent orchestration without a decomposition reason.
- Mentions evals only after launch.
- Has no rollback path for writes, payments, deletes, or permission changes.
- Gives a polished answer but cannot explain trace, logs, or failure boundary.

## Grading Notes

Score each answer from 0 to 2:

- 0: memorized or vague answer, no system boundary.
- 1: correct concepts, but missing production trade-off or failure path.
- 2: gives answer, trade-off, measurement, rollback, and one concrete example.

Suggested thresholds:

- Pass L1-L2: all required answers at least 1, no safety red flag at 0.
- Pass L3-L4: 80% of answers at 2, and incident/rollback question at 2.
- Pass L5: original pattern or contribution question at 2, plus evidence beyond usage.

## Next Expansion Plan

### Next 20 Questions To Add

- L0: token, context window, prompt, and completion boundaries.
- L1: tool ambiguity, memory staleness, planning stop conditions, and direct-answer vs tool-call decision.
- L2: MCP capability discovery, tool schema mismatch, auth scopes, and provider SDK migration.
- L3: stale memory, multi-source citation, retrieval refusal, and multi-agent state ownership.
- L4: incident severity, cost anomaly, rate limit handling, model canary, and trace privacy.
- L5: original pattern contribution, framework deprecation policy, cross-team governance, and docs-as-product.

### Priority

1. Add L0 questions because the learning path starts there.
2. Deepen L2 MCP and tool security.
3. Add L4 incident drills with explicit root-cause categories.
4. Add L5 contribution and governance questions with portfolio evidence.

## Candidate Preparation Checklist

- Run one L1 Lab and explain the loop aloud.
- Show one tool-call trace with success and failure cases.
- Prepare one RAG or memory design with citations and refusal behavior.
- Prepare one production incident with root cause, rollback, and prevention eval.
- Prepare one contribution story using STAR and link it to pattern quality.

## Related Files

- [`l1-components.md`](l1-components.md)
- [`l2-framework-mcp.md`](l2-framework-mcp.md)
- [`l3-system-design.md`](l3-system-design.md)
- [`l4-production.md`](l4-production.md)
- [`l5-patterns.md`](l5-patterns.md)
- [`../interview-framework.md`](../interview-framework.md)
- [`../interview-answer-framework.md`](../interview-answer-framework.md)

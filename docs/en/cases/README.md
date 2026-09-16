---
title: Case Studies Index
validated_date: 2026-09-16
i18n-key: cases-readme
last-synced: 2026-09-16
---

# Case Studies

Case studies connect concepts, Labs, and production decisions to realistic Agent scenarios.

## Cases

- [`customer-support-multi-agent.md`](customer-support-multi-agent.md): multi-agent customer support with retrieval, tools, verification, and escalation.
- [`personal-knowledge-rag.md`](personal-knowledge-rag.md): personal knowledge base with RAG, memory, and refusal behavior.
- [`production-regression-gate.md`](production-regression-gate.md): production release gate with safety, trace, rollback, and cost controls.

## Case Study Rules

Each case should include:

- Scenario.
- Architecture.
- Key decisions.
- Failure modes.
- Evaluation or production evidence.
- Follow-up learning.

## Case-to-Lab Mapping

| Case | Supporting Lab | What It Proves |
| --- | --- | --- |
| [`customer-support-multi-agent.md`](customer-support-multi-agent.md) | [`../../../labs/l3/multi_agent_supervisor/README.md`](../../../labs/l3/multi_agent_supervisor/README.md) | Supervisor routing and verification |
| [`personal-knowledge-rag.md`](personal-knowledge-rag.md) | [`../../../labs/l3/rag_evaluator/README.md`](../../../labs/l3/rag_evaluator/README.md) | Retrieval evidence and refusal |
| [`production-regression-gate.md`](production-regression-gate.md) | [`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md) | Release gates and regression checks |

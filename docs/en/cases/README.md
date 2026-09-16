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
- [`enterprise-multi-tool-agent.md`](enterprise-multi-tool-agent.md): enterprise tool routing with risk, permissions, and observability.
- [`multi-agent-collaboration.md`](multi-agent-collaboration.md): supervised research/action/verification workflow.
- [`pattern-contribution.md`](pattern-contribution.md): reusable Agent pattern contribution readiness.
- [`personal-knowledge-rag.md`](personal-knowledge-rag.md): personal knowledge base with RAG, memory, and refusal behavior.
- [`production-regression-gate.md`](production-regression-gate.md): production release gate with safety, trace, rollback, and cost controls.

## Writing Support

Use [`../../../templates/case-study-template.md`](../../../templates/case-study-template.md) and [`../../../templates/case-study-writing-guide.md`](../../../templates/case-study-writing-guide.md) for new cases.

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
| [`enterprise-multi-tool-agent.md`](enterprise-multi-tool-agent.md) | [`../../../labs/l2/single_agent_mcp/README.md`](../../../labs/l2/single_agent_mcp/README.md) | Tool risk, permission, and audit boundaries |
| [`multi-agent-collaboration.md`](multi-agent-collaboration.md) | [`../../../labs/l3/multi_agent_supervisor/README.md`](../../../labs/l3/multi_agent_supervisor/README.md) | Explicit agent responsibilities and state isolation |
| [`pattern-contribution.md`](pattern-contribution.md) | [`../../../labs/l5/pattern_catalog/README.md`](../../../labs/l5/pattern_catalog/README.md) | Pattern contracts, safety boundaries, and verification |
| [`personal-knowledge-rag.md`](personal-knowledge-rag.md) | [`../../../labs/l3/rag_evaluator/README.md`](../../../labs/l3/rag_evaluator/README.md) | Retrieval evidence and refusal |
| [`production-regression-gate.md`](production-regression-gate.md) | [`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md) | Release gates and regression checks |

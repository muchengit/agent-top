---
i18n-key: tutorials-learning-paths
last-synced: 2026-09-16
validated_date: 2026-09-16
---

# Learning Paths

Learning paths connect Agent-Top tutorials, Labs, cases, quick references, and portfolio evidence. If you want to complete one concrete task before choosing a route, start with [`quick-navigation.md`](quick-navigation.md).

## Beginner Path: From First Call to One Agent

1. Read [`../l0-first-llm-call.md`](../l0-first-llm-call.md).
2. Run [`../../../labs/l0/first_llm_call/README.md`](../../../labs/l0/first_llm_call/README.md).
3. Read [`../concepts/react-pattern.md`](../concepts/react-pattern.md).
4. Run [`../../../labs/l1/minimal_react_agent/README.md`](../../../labs/l1/minimal_react_agent/README.md).
5. Add stop conditions and explain tool-result ambiguity.

Exit evidence:

- One LLM call explained in your own words.
- One ReAct loop run locally.
- One stop-condition explanation.

## Intermediate Path: Reliable Single Agent

1. Read [`../l2-single-agent-mcp.md`](../l2-single-agent-mcp.md).
2. Run [`../../../labs/l2/single_agent_mcp/README.md`](../../../labs/l2/single_agent_mcp/README.md).
3. Run [`../../../labs/l1/guardrail_helpers/README.md`](../../../labs/l1/guardrail_helpers/README.md).
4. Run [`../../../labs/l2/cost_aware_router/README.md`](../../../labs/l2/cost_aware_router/README.md).
5. Write a tool risk classification table.

Exit evidence:

- Tool allowlist.
- Destructive-action confirmation rule.
- Cost or latency-aware routing decision.

## System Path: RAG, Memory, Multi-Agent

1. Read [`../l3-rag-memory-observability.md`](../l3-rag-memory-observability.md).
2. Read [`../concepts/multi-round-research-discussion.md`](../concepts/multi-round-research-discussion.md).
3. Run [`../../../labs/l3/rag_evaluator/README.md`](../../../labs/l3/rag_evaluator/README.md).
4. Run [`../../../labs/l3/multi_round_research_discussion/README.md`](../../../labs/l3/multi_round_research_discussion/README.md).
5. Run [`../../../labs/l3/multi_agent_supervisor/README.md`](../../../labs/l3/multi_agent_supervisor/README.md).

Exit evidence:

- Retrieval eval with required-source case.
- Refusal case for missing evidence.
- Multi-agent route assignment.

## Production Path

1. Read [`../l4-production.md`](../l4-production.md).
2. Read [`../production/evals-checklist.md`](../production/evals-checklist.md).
3. Read [`../production/safety-checklist.md`](../production/safety-checklist.md).
4. Run [`../../../labs/l4/production_postmortem/README.md`](../../../labs/l4/production_postmortem/README.md).
5. Run [`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md).

Exit evidence:

- Release gate checklist.
- Incident postmortem with owner and due date.
- Rollback plan.

## Expert Path: Original Pattern

1. Read [`../l5-custom-patterns.md`](../l5-custom-patterns.md).
2. Read [`../concepts/agent-system-architecture.md`](../concepts/agent-system-architecture.md).
3. Run [`../../../labs/l5/custom_pattern_lab/README.md`](../../../labs/l5/custom_pattern_lab/README.md).
4. Run [`../../../labs/l5/pattern_catalog/README.md`](../../../labs/l5/pattern_catalog/README.md).
5. Draft one reusable pattern with safety and verification.

Exit evidence:

- Pattern spec.
- Deterministic Lab.
- Failure-mode section.
- Reviewer-ready contribution notes.

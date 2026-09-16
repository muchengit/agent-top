---
title: Quick Navigation
validated_date: 2026-09-16
i18n-key: tutorials-quick-navigation
last-synced: 2026-09-16
---

# Quick Navigation Cards

Use this page when you already know what you want to accomplish. Pick one task, complete the Lab or exercise, and produce the listed evidence before moving on.

## Today, Finish One Task

| Your task | Follow this path | Expected output |
| --- | --- | --- |
| Run a local Agent trace without an API key | [`examples/agent-decision-trace/README.md`](../../../examples/agent-decision-trace/README.md) | A local trace file showing why destructive or ambiguous tool calls are blocked |
| Practice RAG evidence and refusal | [`examples/rag-evidence-refusal/README.md`](../../../examples/rag-evidence-refusal/README.md) | An answer log showing citations, refusal, stale-source handling, and conflict resolution |
| Understand the delivery flow for a real Agent | [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md) | A system contract, tool risk table, release gate, and postmortem checklist |
| Build the first minimal ReAct Agent | [`../l1-minimal-react-agent.md`](../l1-minimal-react-agent.md) -> [`../../../labs/l1/minimal_react_agent/README.md`](../../../labs/l1/minimal_react_agent/README.md) | A working loop plus an explanation of perception, tools, planning, and memory |
| Practice MCP-style tool boundaries | [`../l2-single-agent-mcp.md`](../l2-single-agent-mcp.md) -> [`../../../labs/l2/single_agent_mcp/README.md`](../../../labs/l2/single_agent_mcp/README.md) | A tool allowlist with read/write/destructive risk classes |
| Evaluate RAG and memory evidence | [`../l3-rag-memory-observability.md`](../l3-rag-memory-observability.md) -> [`../../../labs/l3/rag_evaluator/README.md`](../../../labs/l3/rag_evaluator/README.md) | A refusal case for missing evidence and a required-source eval |
| Prepare a production gate | [`../l4-production.md`](../l4-production.md) -> [`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md) | A release checklist covering safety, trace, rollback, cost, and latency |

## Navigation by Role

| Role | Start here | Finish with |
| --- | --- | --- |
| Learner | [`learning-paths.md`](learning-paths.md) | One L0-L1 Lab run locally |
| Practitioner | [`reference-map.md`](reference-map.md) | Tool, MCP, RAG, and memory trade-off notes |
| Engineer | [`../production/evals-checklist.md`](../production/evals-checklist.md) | Eval set, guardrails, and release gates |
| Interview candidate | [`../interviews/interview-framework.md`](../interviews/interview-framework.md) | STAR answer plus portfolio evidence |
| Contributor | [`../community/contribution-paths.md`](../community/contribution-paths.md) | Docs, translation, Lab, review, or pattern contribution |

## How To Check Whether You Finished

A task is complete only when all three are true:

1. You ran or inspected the linked material.
2. You wrote one artifact: notes, table, trace, eval, or design checklist.
3. You can explain the trade-off in one paragraph.

## Related Pages

- Practice handbook: [`practice-handbook.md`](practice-handbook.md)
- Learning paths: [`learning-paths.md`](learning-paths.md)
- Core implementation guide: [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md)
- Open-source inspirations: [`open-source-inspirations.md`](open-source-inspirations.md)
- Local examples: [`../../../examples/README.md`](../../../examples/README.md)

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
| Practice memory-vs-evidence decisions | [`examples/memory-vs-evidence/README.md`](../../../examples/memory-vs-evidence/README.md) | A decision log showing which facts come from memory, tool results, or retrieved sources |
| Practice coding workspace safety | [`examples/coding-workspace-safety/README.md`](../../../examples/coding-workspace-safety/README.md) | A decision log showing patch review, rollback, verification, and approval choices |
| Practice data-source policy decisions | [`examples/data-source-policy/README.md`](../../../examples/data-source-policy/README.md) | A decision log showing crawl, parse, store, retrieve, cite, ignore, and block choices |
| Practice coding task navigation | [`examples/coding-task-navigation/README.md`](../../../examples/coding-task-navigation/README.md) | A completed task map connecting request, entry, expected artifact, verification, and stop condition |
| Practice Agent evaluation regression | [`examples/agent-eval-regression/README.md`](../../../examples/agent-eval-regression/README.md) | A regression report showing dataset version, pass rate, gate decision, and rollback owner |
| Practice GitHub-native Agent review | [`examples/github-agent-review/README.md`](../../../examples/github-agent-review/README.md) | A review note showing CI status, diff scope, risks, and approval decision |
| Review the open-source pattern matrix | [`tutorials/open-source-pattern-matrix.md`](open-source-pattern-matrix.md) | A short note on which external pattern maps to a local concept, Lab, example, or production guide |
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

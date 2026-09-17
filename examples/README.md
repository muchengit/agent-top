# Examples

Agent-Top examples are fictional, local, and do not require API keys, external services, paid connectors, or real customer data.

## Exercises

| Exercise | Files | What You Practice |
| --- | --- | --- |
| Agent Decision Trace | [`agent-decision-trace/README.md`](agent-decision-trace/README.md) | Tool risk classification, clarification, blocking destructive actions, and audit evidence |
| RAG Evidence Refusal | [`rag-evidence-refusal/README.md`](rag-evidence-refusal/README.md) | Retrieval evidence, citation rules, missing-evidence refusal, stale-source handling, and conflict resolution |
| Memory Vs Evidence | [`memory-vs-evidence/README.md`](memory-vs-evidence/README.md) | Memory trust, live evidence, stale preferences, deletion, and conflicting sources |
| Coding Workspace Safety | [`coding-workspace-safety/README.md`](coding-workspace-safety/README.md) | Patch-first editing, rollbackable changes, verification commands, and coding-Agent approval decisions |
| Data Source Policy | [`data-source-policy/README.md`](data-source-policy/README.md) | Crawling, parsing, storage, retrieval, citation, ignore, block, stale-source, and prompt-injection decisions |
| Coding Task Navigation | [`coding-task-navigation/README.md`](coding-task-navigation/README.md) | Request-to-artifact mapping, expected verification, stop conditions, and task-first learning path selection |
| Agent Eval Regression | [`agent-eval-regression/README.md`](agent-eval-regression/README.md) | Prompt version comparison, fixture-based grading, regression gates, and launch/rollback decisions |
| GitHub Agent Review | [`github-agent-review/README.md`](github-agent-review/README.md) | PR review order, CI gating, diff-based review notes, and platform-native tool boundaries |
| Observability Trace | [`observability-trace/README.md`](observability-trace/README.md) | Trace completeness, PII redaction, tool/retrieval/final-answer evidence, and postmortem readiness |
| Model Gateway Evidence | [`model-gateway/README.md`](model-gateway/README.md) | Model routing evidence, fallback/retry visibility, budget decisions, and inference runtime checks |
| Safety Eval Evidence | [`safety-eval/README.md`](safety-eval/README.md) | Injection, leakage, refusal, harm, hallucination, memory conflict, and guardrail evidence |
| MCP Tool Boundary | [`mcp-tool-boundary/README.md`](mcp-tool-boundary/README.md) | MCP server evidence, graph checkpoints, typed tool output, permission scope, and result status |
| Memory And Index Evidence | [`memory-index-evidence/README.md`](memory-index-evidence/README.md) | Memory lifecycle, vector collection boundaries, search evidence, and serving deployment evidence |

## How To Use These Exercises

1. Read the exercise prompt.
2. Fill in the answer template.
3. Compare your decisions with the answer key.
4. Change one rule, such as requiring citations for all factual claims, and record what changes.

## Relationship To Labs

Examples are paper exercises and design practice. Runnable deterministic code lives in [`../labs/README.md`](../labs/README.md). For how to combine them, see [`../docs/en/tutorials/practice-handbook.md`](../docs/en/tutorials/practice-handbook.md).

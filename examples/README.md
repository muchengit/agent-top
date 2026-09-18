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
| Release Gate Evidence | [`release-gate-evidence/README.md`](release-gate-evidence/README.md) | Workflow run evidence, checkout/setup version pinning, artifact/cache decisions, and release-gate replayability |
| Multilingual Support | [`multilingual-support/README.md`](multilingual-support/README.md) | Language routing, cross-language memory scope, unsupported-language fallback and refusal |
| Compliance Review | [`compliance-review/README.md`](compliance-review/README.md) | Evidence-gated approvals, approver roles, audit trails, and blocking conditions |

## Extended Exercises

Each exercise README now includes an `## Extended Exercises` section with 2-3 follow-up prompts linked to the relevant tutorials or Labs. Pick one prompt, change the policy, and record what changes in your decision log.

## How To Use These Exercises

1. Read the exercise prompt.
2. Fill in the answer template.
3. Compare your decisions with the answer key.
4. Change one rule, such as requiring citations for all factual claims, and record what changes.
5. To reuse an exercise, copy its `*.template.jsonl` file, fill it in, and re-read it as a decision log.
6. To verify that every JSONL file under `examples/` is legal JSON, run `python scripts/check_repository.py` from the repository root (the `check_examples_jsonl` step also runs in CI).

## JSONL Conventions

Each JSONL file in this repository is local fixture data. Every non-empty line must parse as one JSON object. Files may use different schemas when the event type is different, but keys inside one file should stay stable unless the file README explains an optional event-specific field.

## 中文说明

`examples/` 下的 JSONL 都是本地虚构练习数据。每个非空行都必须是 1 个 JSON object。不同 event 可以使用不同 schema，但同一个文件内的字段应保持稳定；若字段是可选或事件特定字段，应在该 example README 里说明。

## Bilingual Notes

This index is intentionally bilingual: English names describe stable directories and artifact types, while the Chinese notes explain how learners should use the exercises. Individual example README files remain local, fictional, and API-key-free.

## Relationship To Labs

Examples are paper exercises and design practice. Runnable deterministic code lives in [`../labs/README.md`](../labs/README.md). For how to combine them, see [`../docs/en/tutorials/practice-handbook.md`](../docs/en/tutorials/practice-handbook.md).

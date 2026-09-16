---
title: Agent Glossary
validated_date: 2026-09-16
i18n-key: quick-reference-agent-glossary
last-synced: 2026-09-16
---

# Agent Glossary

Use this glossary when choosing terms for docs, Labs, interviews, and production incidents.

## Core Terms

| Term | Meaning |
| --- | --- |
| Agent | A system that uses an LLM, tools, memory, planning, and control loops to complete tasks. |
| Perception | Turning user input, tool results, and retrieved context into usable state. |
| Planning | Deciding the next action or reasoning step. |
| Action | A tool call, retrieval request, message, or other system effect. |
| Observation | Evidence returned from a tool, retrieval, model, or environment. |
| ReAct | A loop that interleaves reasoning and action. |
| Tool | An external function or action with typed inputs and outputs. |
| MCP | A standard protocol for connecting LLM apps to MCP servers that expose tools, resources, prompts, schemas, and context. |
| RAG | Retrieval-augmented generation using retrieved sources. |
| Memory | Context stored across turns or sessions. |
| Guardrail | A rule that prevents unsafe behavior. |
| Eval | A test that measures Agent behavior. |
| Trace | A record of prompts, tool calls, decisions, and outcomes. |
| Rollback | A path that restores known-safe behavior. |

## Production Terms

| Term | Meaning |
| --- | --- |
| Contract | A documented input/output/failure-mode agreement for an Agent or tool. |
| Handoff | Passing task state from one Agent or stage to another. |
| Verifier | A component or Agent that checks evidence and recommendations. |
| Supervisor | An orchestrator that routes tasks to workers and enforces stop conditions. |
| Human-in-the-loop | A workflow where a human approves or reviews a risky step. |
| Confidence | The evidence strength behind an answer, not a substitute for verification. |
| Citation | Evidence attached to a claim or answer. |
| Fallback | A safe response when evidence, tool, or model behavior is insufficient. |
| Idempotency | Safe retry behavior for tools that may repeat effects. |
| Regression Gate | A release gate that blocks unsafe behavior from shipping. |
| Blast Radius | The range of users, data, or systems affected by a failure. |
| Postmortem | A blameless review that turns an incident into prevention actions. |

## Decision Terms

| Term | Meaning |
| --- | --- |
| Fail closed | Stop or refuse rather than continue with unsafe assumptions. |
| Trade-off | An explicit comparison of accuracy, latency, cost, safety, and maintainability. |
| Stable pattern | A design idea that remains useful across frameworks. |
| Framework boundary | Framework-specific API details that should stay isolated in Labs. |
| Validated date | The date when a doc or example was checked. |
| Tested against | The version or environment anchor for an executable example. |

## Review Questions

- Is every external action represented by a typed tool contract?
- Is there a verifier for evidence-heavy claims?
- Is there a refusal path when evidence is missing?
- Is there a rollback path for external side effects?
- Can this behavior be measured by an eval rather than guessed?

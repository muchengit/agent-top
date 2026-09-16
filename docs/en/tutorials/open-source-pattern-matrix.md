---
title: Open-Source Pattern Matrix
validated_date: 2026-09-17
i18n-key: tutorials-open-source-pattern-matrix
last-synced: 2026-09-17
---

# Open-Source Pattern Matrix

This matrix distills Agent-Top's open-source inspiration into reusable patterns. Use it when choosing what to add to a tutorial, Lab, case, or production guide.

## How To Use This Page

1. Pick the capability gap you want to close.
2. Read the pattern definition.
3. Add only the stable principle to docs.
4. Keep framework-specific details in Labs or framework maps.
5. Link to evidence, evals, or examples.

## Pattern Matrix

| Pattern | Problem It Solves | Stable Principle | Agent-Top Landing Place | Do Not Copy |
| --- | --- | --- | --- | --- |
| Tool schema-first | Ambiguous tools and unsafe calls | Define inputs, outputs, risk, permissions, and audit before prompt text | [`../skills/tool-mcp-safety.md`](../skills/tool-mcp-safety.md), [`../../../examples/agent-decision-trace/README.md`](../../../examples/agent-decision-trace/README.md) | Vendor-specific SDK boilerplate |
| Stateful graph workflow | Hidden control flow and hard-to-debug loops | Make state, transitions, retries, checkpoints, and stops explicit | [`../concepts/plan-decision-making.md`](../concepts/plan-decision-making.md), [`../../../labs/l3/multi_agent_supervisor/README.md`](../../../labs/l3/multi_agent_supervisor/README.md) | Whole graph framework API |
| Role-based teams | Unbounded multi-agent chatter | Give every role a responsibility, input, output, and stop condition | [`../concepts/multi-agent-scheduling.md`](../concepts/multi-agent-scheduling.md) | Example chat personas |
| Structured outputs | Free-text model responses break pipelines | Validate model output against a schema and retry or escalate | [`../concepts/agent-system-architecture.md`](../concepts/agent-system-architecture.md) | Provider-specific JSON mode examples |
| RAG evaluation | Retrieval looks good but answers are unsafe | Split retrieval relevance, answer faithfulness, missing evidence, and stale source checks | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../../../examples/rag-evidence-refusal/README.md`](../../../examples/rag-evidence-refusal/README.md) | Tool-specific benchmark code |
| Memory lifecycle | Memory grows stale or private | Extract, deduplicate, expire, delete, and scope memory by owner and purpose | [`../concepts/long-term-memory.md`](../concepts/long-term-memory.md) | Memory provider data model |
| Observability contract | Incidents cannot be replayed | Record request, prompt/model version, tool, retrieval, guardrail, memory, cost, latency | [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md) | Dashboard screenshots or vendor setup |
| Prompt optimization loop | Prompt tweaks are guesswork | Version prompts, define metrics, compare on eval sets, ship only measured wins | [`../production/evals-playbook.md`](../production/evals-playbook.md) | Specific optimizer internals |
| MCP policy proxy | Tools are too trusted | Put authorization, audit, mutation gates, redaction, and rate limits near execution | [`../concepts/mcp.md`](../concepts/mcp.md), [`../skills/tool-mcp-safety.md`](../skills/tool-mcp-safety.md) | A full proxy implementation |
| Runtime guardrails | Safety only lives in the final prompt | Intercept unsafe inputs, outputs, and tool calls before side effects | [`../production/safety-checklist.md`](../production/safety-checklist.md) | Black-box jailbreak datasets |
| 12-factor operations | Local demos fail in production | Treat config, state, logs, scaling, and release as architecture concerns | [`../l4-production.md`](../l4-production.md) | Generic devops boilerplate |
| Postmortem learning | Incidents repeat | Convert incidents into eval, guardrail, trace field, rollback note, or action item | [`../production/quarterly-maintenance.md`](../production/quarterly-maintenance.md), [`../../../templates/postmortem-template.md`](../../../templates/postmortem-template.md) | Company-specific incident templates |

## Decision Rules

- If a pattern changes how Agents are designed, add it to `docs/en/concepts` and mirror to Chinese.
- If a pattern requires runnable proof, add or extend a Lab under `labs`.
- If a pattern is about deciding safely with fictional data, add an example under `examples`.
- If a pattern is about release safety, add it to production guides.
- If a pattern is framework-specific, keep it in [`frameworks/framework-map.md`](../frameworks/framework-map.md).

## Candidate Next Additions

- A browser-use safety example using MCP policy-proxy principles.
- A memory lifecycle exercise covering expiry, deletion, and conflicting preferences.
- A structured-output validation Lab for schema retry and escalation.
- A prompt optimization case with versioned prompts and eval report.
- A structured-output validation Lab for schema retry and escalation.
- A prompt optimization case with versioned prompts and eval report.

## Related Pages

- Open-source inspirations: [`open-source-inspirations.md`](open-source-inspirations.md)
- Framework map: [`../frameworks/framework-map.md`](../frameworks/framework-map.md)
- Practice handbook: [`practice-handbook.md`](practice-handbook.md)
- Evaluation playbook: [`../production/evals-playbook.md`](../production/evals-playbook.md)

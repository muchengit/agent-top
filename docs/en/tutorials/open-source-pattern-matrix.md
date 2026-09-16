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
| Coding workspace boundary | Coding Agents mutate repositories unexpectedly | Separate repository context, command execution, file writes, tests, and rollback state | [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md), [`../production/safety-checklist.md`](../production/safety-checklist.md) | Whole editor plugin internals |
| Patch-first editing | Hard-to-review direct mutations | Produce a reviewable patch before applying code changes | [`../concepts/design-review-checklist.md`](../concepts/design-review-checklist.md), [`../../../templates/contribution-checklist.md`](../../../templates/contribution-checklist.md) | Vendor diff UI |
| Test-driven Agent validation | Code Agent changes are unproven | Tie every code-changing action to the smallest deterministic verification command | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md) | Full CI suite boilerplate |
| Source policy boundary | Agents over-collect or over-retrieve | Treat crawl, parse, store, retrieve, cite, ignore, and block as separate decisions | [`../concepts/rag-memory-mcp-flow.md`](../concepts/rag-memory-mcp-flow.md), [`../../../examples/data-source-policy/README.md`](../../../examples/data-source-policy/README.md) | Vendor crawler internals |
| Ingestion metadata contract | Retrieval evidence cannot be explained | Preserve source URL, crawl time, freshness, permission state, parser version, and deletion state | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../concepts/long-term-memory.md`](../concepts/long-term-memory.md) | Full vector store schema |
| Browser action trace | UI actions are invisible and hard to roll back | Record visible context, action intent, screenshot or DOM summary, and rollback state | [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md), [`../production/safety-checklist.md`](../production/safety-checklist.md) | Provider-specific browser automation code |
| Structured output validation | Schemaless outputs break downstream systems | Add schema validation, retry budget, invalid-output escalation, and failure logging | [`../concepts/agent-system-architecture.md`](../concepts/agent-system-architecture.md), [`../production/evals-playbook.md`](../production/evals-playbook.md) | Provider-specific JSON mode code |
| Sandboxed execution boundary | Code Agents can run unsafe commands | Separate shell, filesystem, network, credentials, and approval gates before execution | [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md), [`../production/safety-checklist.md`](../production/safety-checklist.md) | Full sandbox runtime |
| Event evidence routing | Runtime evidence cannot be tied to decisions | Bind prompt, tool, CI, dataset, release, and rollback evidence to one event family | [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md), [`../../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) | Vendor dashboard UI |
| CI-first release evidence | Release confidence depends on branch names | Require commit SHA, required checks, dataset version, regression diff, approval, and rollback plan before release | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md), [`../../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) | A generic CI template |
| Release gate evidence | Release decisions are not replayable | Add a `release.gate.checked` event for release, canary, block, and rollback decisions | [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md), [`../../../templates/observability-trace-template.md`](../../../templates/observability-trace-template.md) | Incident screenshot |
| Eval gate discipline | Prompt, tool, or model changes regress silently | Require dataset version, pass rate, regression diff, owner approval, and rollback plan | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../../../examples/agent-eval-regression/README.md`](../../../examples/agent-eval-regression/README.md) | Vendor dashboard setup |
| Error grouping evidence | Similar incidents are treated as separate complaints | Aggregate by fingerprint, release SHA, route, owner, recurrence, and severity so postmortems find repeat root causes | [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md), [`../../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) | Vendor issue taxonomy |
| Runtime hotspot evidence | Cost and latency regressions are undiagnosable | Link profiling or runtime metrics to commit, release, model, prompt, tool, and dataset versions | [`../production/cost-stability-operations.md`](../production/cost-stability-operations.md), [`../../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) | Specific profiler UI |
| Deterministic lint gate | Style and safety checks are subjective | Record tool version, exact findings, and pass/fail result before a release gate moves on | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) | Project-specific ruleset |
| Tool and dependency lock evidence | Releases cannot be reproduced | Preserve package/tool versions and lockfile artifacts for Python, CLI, Agent, and MCP dependencies | [`../l4-production.md`](../l4-production.md), [`../../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) | Full dependency management guide |
| Workflow provenance | Distributed steps lose context across retries | Record workflow/activity id, input event id, attempt number, dead-letter state, and owner for each step | [`../concepts/multi-agent-scheduling.md`](../concepts/multi-agent-scheduling.md), [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md) | Framework workflow DSL |
| GenAI telemetry vocabulary | Traces differ by vendor and cannot be compared | Use stable span/event names and standard model, provider, token, cost, tenant, workflow, and tool attributes | [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md), [`../../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) | One vendor's dashboard schema |
| Eval-as-CI | Prompt or model changes ship without repeatable proof | Turn tests into matrices with pass/fail assertions, dataset versions, and release decisions | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../../../examples/agent-eval-regression/README.md`](../../../examples/agent-eval-regression/README.md) | Tool-specific YAML format |
| Model gateway evidence | Model routing decisions are invisible | Record selected provider/model, fallback, retry, budget, rate-limit reason, and response status | [`../production/cost-stability-operations.md`](../production/cost-stability-operations.md), [`../../../examples/model-gateway/README.md`](../../../examples/model-gateway/README.md) | Gateway configuration file |
| Inference runtime metrics | Serving behavior cannot be explained by prompt traces alone | Capture throughput, latency percentile, timeout, concurrency, batching, and resource pressure | [`../production/cost-stability-operations.md`](../production/cost-stability-operations.md), [`../../../examples/model-gateway/README.md`](../../../examples/model-gateway/README.md) | Runtime internals |
| Platform app boundary | User-facing Agent surfaces mix UI, tools, knowledge, and permissions | Separate chat surface, workflow nodes, tool execution, knowledge source, permissions, and audit trail | [`../concepts/agent-system-architecture.md`](../concepts/agent-system-architecture.md), [`../production/safety-checklist.md`](../production/safety-checklist.md) | Whole platform UI |

## Decision Rules

- If a pattern changes how Agents are designed, add it to `docs/en/concepts` and mirror to Chinese.
- If a pattern requires runnable proof, add or extend a Lab under `labs`.
- If a pattern is about deciding safely with fictional data, add an example under `examples`.
- If a pattern is about release safety, add it to production guides.
- If a pattern is framework-specific, keep it in [`frameworks/framework-map.md`](../frameworks/framework-map.md).

## Candidate Next Additions

- A GitHub-native PR review example covering issue → checks → diff → review comment order.
- A browser-use safety example using MCP policy-proxy principles.
- A memory lifecycle exercise covering expiry, deletion, and conflicting preferences.
- A structured-output validation Lab for schema retry and escalation.
- A prompt optimization case with versioned prompts and eval report.
- A coding Agent evaluation case using deterministic tests and code diff correctness checks.

## Related Pages

- Open-source inspirations: [`open-source-inspirations.md`](open-source-inspirations.md)
- Framework map: [`../frameworks/framework-map.md`](../frameworks/framework-map.md)
- Practice handbook: [`practice-handbook.md`](practice-handbook.md)
- Evaluation playbook: [`../production/evals-playbook.md`](../production/evals-playbook.md)

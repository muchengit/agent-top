---
title: Cost and Stability Operations
validated_date: 2026-09-16
i18n-key: production-cost-stability-operations
last-synced: 2026-09-16
---

# Cost and Stability Operations

Cost and stability operations turn production Agent budgets into runtime rules.

## Operating Model

- Define budgets before traffic growth.
- Enforce budgets at the Agent runtime, not only in dashboards.
- Degrade before unsafe or unbounded behavior spreads.
- Keep traces active during degradation.

## Cost Budgets

Track:

- Tokens per request and per tenant.
- Cost per completed task.
- Cost per failed task.
- Token usage by model, tool, retrieval source, and workflow branch.
- Budget burn rate by hour, day, tenant, and feature flag.

Budget formula:

```text
task_budget =
  prompt_tokens * prompt_cost +
  completion_tokens * completion_cost +
  retrieval_cost +
  tool_cost +
  storage_cost +
  eval_or_shadow_cost
```

## Latency SLO

Use separate budgets for planning, retrieval, model generation, tool calls, and final verification.

Alert when:

- p95 latency exceeds budget for three consecutive windows.
- tool-call latency exceeds timeout policy.
- retry count approaches retry budget.
- one tenant or workflow consumes more than expected share.

## Degradation Modes

Use degradation instead of hard failure when safety can be preserved.

Common modes:

- Return a concise sourced answer instead of a full reasoning chain.
- Disable expensive retrieval expansion.
- Skip optional verification and log the gap.
- Route to human review for high-risk actions.
- Freeze memory writes while keeping reads audited.

Degradation must never bypass auth, tool safety, or audit logging.

## Gateway Evidence

When Agents call models through a model gateway, inference server, or self-hosted runtime, cost stability includes routing decisions, not just spend.

Record for each model call:

- `route`: the gateway route or policy chosen.
- `provider_model`: actual provider/model hit.
- `fallback_used`: whether fallback was triggered.
- `retry_count`: number of retries.
- `budget_decision`: `continue`, `degrade`, or `block`.
- `rate_limit_reason`: reason when throttled.
- `latency_ms`: end-to-end and serving runtime latency.
- `throughput_tokens_per_s`: throughput evidence from gateway or runtime.

Use these fields to answer: why was this model chosen, why did cost rise, and can the system safely rollback or degrade?


## Serving Deployment Evidence

When Agents use self-hosted inference servers or serving endpoints, deployment is also stability evidence.

Record for each deployment or runtime change:

- `endpoint`: serving endpoint or gateway route.
- `model_revision`: model id, revision, commit, or image tag.
- `revision_id`: deployed runtime revision actually serving traffic.
- `health`: health check status.
- `resource_limits`: CPU, GPU, memory, batch size, or concurrency limits.
- `timeout_policy`: request, stream, queue, and retry timeouts.
- `capacity`: current throughput, queue depth, or saturation state.
- `rollback_action`: rollback or degradation path that can be executed.

Use these fields to answer: why did this serving change affect latency, cost, quality, or safety, and how can it be rolled back?

## Guardrail Decision

A runtime guardrail should decide one of:

- `continue`: request is within budgets.
- `degrade`: request is risky but can be completed with reduced scope.
- `block`: continuing would exceed a hard safety or resource boundary.

Every non-`continue` decision should include a reason code and request ID.

## Alerts

Minimum alerts:

- Token budget burn rate above threshold.
- Cost per task above threshold.
- p95 latency above SLO.
- Retry rate spike.
- Degradation rate spike.
- Tool-call timeout rate spike.
- Degraded responses without trace fields.

## Runbooks

Each alert needs:

- Symptom.
- Immediate containment.
- Owner to page.
- Query or dashboard to inspect.
- Known safe rollback.
- User communication if needed.
- Follow-up action type.

## Cost Incident Response

1. Freeze risky traffic paths.
2. Check cost by tenant, model, prompt version, workflow, and tool.
3. Disable the highest-burn branch or prompt path.
4. Re-enable only after adding a regression eval or budget test.
5. Write a cost postmortem with root cause and prevention action.

## Weekly Review

Review:

- Highest-cost workflows.
- Highest-failure workflows.
- Degradation reasons.
- Prompt versions causing regressions.
- Tools that consume budget without improving answer quality.
- Missing budget telemetry.

## SLO Template

```markdown
# Agent SLO

- Success criterion:
- Latency p95:
- Cost per task:
- Retry budget:
- Degradation budget:
- Blocked request policy:
- Trace completeness:
```

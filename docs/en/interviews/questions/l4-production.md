---
title: L4 Production Questions
validated_date: 2026-09-17
i18n-key: interviews-questions-l4-production
last-synced: 2026-09-17
---

# L4 Production Questions

These questions check whether the candidate can operate an agent system in production: release gates, evaluation systems, observability, safety guardrails, cost control, and post-incident learning. Four question types are covered: concept, implementation, debugging, and design.

## Question Bank

### Concept

#### 1. What do you do before shipping an Agent feature?

**Answer points:**

- Auth and permissions are defined per role and tenant.
- Rate limits and cost guardrails exist with owners.
- Eval set is green, including negative and safety cases.
- Observability traces prompt, tool, answer, latency, and cost.
- Rollback plan is documented and rehearsed.

**What the interviewer wants to hear:**

- Trade-off: a gate that blocks everything is as bad as a gate that blocks nothing; classify each check as block, warn, or require-approval.
- Production counterexample: an eval set that only covers happy paths goes green while a guardrail regresses; the gate passed because the failing case was not in the set.
- Data thinking: release on measured deltas — before/after on resolution rate, cost per task, and guardrail trigger rate — not on vibes.

**Bonus / Common mistakes:**

- Bonus: name the single item that would block release by itself (usually the safety eval or rollback rehearsal).
- Mistake: shipping because the demo worked and the eval suite was optional.

#### 2. What is the difference between an eval set and an observability trace?

**Answer points:**

- An eval set is an offline, versioned suite of inputs with expected behavior, run on every change.
- A trace is a live, per-request record of what actually happened in production.
- Evals catch regressions before release; traces diagnose incidents after release.
- The two meet in replay: a production trace that fails can be turned into an eval case.

**What the interviewer wants to hear:**

- Trade-off: more eval coverage raises CI cost and maintenance; more tracing raises storage cost. Spend where the failure mode is.
- Production counterexample: a team with rich traces but no evals discovered the regression only after a week of incidents, because nothing replayed past failures into the test suite.
- Data thinking: track eval-to-incident ratio — each production incident should add at least one eval case; that ratio is a leading health indicator.

**Bonus / Common mistakes:**

- Bonus: golden-set versioning and trace-schema versioning so replay stays accurate.
- Mistake: treating a dashboard as a substitute for an eval gate.

### Implementation

#### 3. How do you build an evaluation system for agents?

**Answer points:**

- Start from a versioned golden set with expected behaviors: factual, refusal, safety, and ambiguous cases.
- Measure the pipeline in layers: retrieval (recall@k), tool selection (accuracy), generation (support, faithfulness), and final answer (citation accuracy).
- Add automated checks in CI: unit-style deterministic checks plus model-based grading with a fixed rubric.
- Track latency and cost per case; a quality gain at 10x cost may not ship.
- Keep a regression gate: any prompt, model, or tool change must re-run the set.

**What the interviewer wants to hear:**

- Trade-off: model-based grading scales but can be lenient or drift; deterministic checks are stable but miss semantic errors. Use deterministic checks for structure and model-based grading for meaning, with human audit on a sample.
- Production counterexample: a rubric that praised "confident and helpful" answers let hallucinations pass; the fix was requiring evidence grounding as a hard pass/fail dimension.
- Data thinking: measure false refusal and false acceptance separately, and slice by tenant, language, and topic to find weak segments.

**Bonus / Common mistakes:**

- Bonus: eval trace replay — every production failure becomes a permanent regression case.
- Mistake: measuring only the final answer and ignoring where in the pipeline the error came from.

#### 4. How do you make agent behavior observable in production?

**Answer points:**

- Emit structured traces per request: prompt, context, tool calls, decisions, stop reasons, latency, cost, and evaluation results.
- Tag traces with correlation IDs linking to the user, tenant, and feature.
- Track metrics: request volume, success/refusal/escalation rates, p50/p95/p99 latency, cost per task, tool error rate.
- Record stop reasons (answer, clarify, escalate, exhausted) so loop problems are visible.
- Store traces long enough to replay incidents, with PII redaction.

**What the interviewer wants to hear:**

- Trade-off: full traces are expensive to store; sample heavy payloads but keep complete metadata and redacted content.
- Production counterexample: traces stopped at the final answer, so a wrong refund could not be replayed; adding tool-call and decision spans made root cause visible in minutes.
- Data thinking: dashboard the stop-reason distribution — a rising "exhausted" share means loops are burning budget, not user satisfaction.

**Bonus / Common mistakes:**

- Bonus: a canary trace that exercises the real tool path on a schedule.
- Mistake: alerting on raw error counts and waking people for one noisy retry.

### Debugging

#### 5. A customer reports the Agent made the wrong account change.

**Answer points:**

- Stop the unsafe action path immediately; freeze the affected tool or user cohort.
- Inspect traces: prompt, retrieved context, tool call arguments, and decision path.
- Find the root cause in data, tool schema, policy, or permission boundary — not just the model.
- Add a regression eval and a prevention control (permission rule, schema validation, confirmation gate).
- Write a postmortem with owner, due date, rollback plan, and a prevention checklist.

**What the interviewer wants to hear:**

- Trade-off: speed of remediation versus completeness of root cause; stop the bleeding first, but never close the incident without a regression case.
- Production counterexample: the team "fixed" a wrong refund by adding a prompt line; the same mistake recurred because the permission boundary was still missing.
- Data thinking: tie the incident to metrics — which tenant, which tool, which argument shape — so the fix is scoped and the eval case targets the actual failure.

**Bonus / Common mistakes:**

- Bonus: rehearse the rollback before the incident, not during it.
- Mistake: blaming the model and reverting the prompt without auditing the tool and permission layers.

#### 6. How do you run a postmortem for an agent incident?

**Answer points:**

- State the impact in user and business terms, with numbers.
- Timeline: what changed, when, and what the traces show.
- Root cause at the component level: data, model, tool, policy, or deployment.
- Contributing factors: missing eval, missing alert, unclear ownership.
- Actions with owners and due dates: prevention, detection, and recovery.
- Follow-up: verify each action shipped and add eval cases for recurrence.

**What the interviewer wants to hear:**

- Trade-off: blameless postmortems get better data; blame gets silence. Separate human error from system design gaps.
- Production counterexample: a postmortem that blamed "the model" produced no action items; re-framing as a missing grounding check produced a real fix.
- Data thinking: each postmortem should change at least one eval case, one alert, and one ownership boundary; track that three-way closure.

**Bonus / Common mistakes:**

- Bonus: a public postmortem template with impact, timeline, root cause, actions.
- Mistake: writing a postmortem with no owner and no due date — it is a diary, not a process.

### Design

#### 7. Design safety guardrails for an Agent that touches external systems.

**Answer points:**

- Enforce policy in code, not just the prompt: allowed actions, allowed targets, rate limits, approval gates.
- Classify risk by reversibility, blast radius, and data sensitivity; map each action to a risk class.
- Validate arguments against schemas before execution; require confirmation for irreversible actions.
- Emit audit logs with correlation IDs and verify after execution.
- Make the guardrail the outer ring; the system prompt is an inner convenience, never the only barrier.

**What the interviewer wants to hear:**

- Trade-off: strict code gates are safe but add friction; permissive ones ship fast but leak risk. Tune by risk class, not globally.
- Production counterexample: a "safe" approval widget was bypassed because the same UI element served preview and confirm for different action types; separating confirm contracts per action class closed it.
- Data thinking: track guardrail trigger, override, and bypass-attempt rates as product metrics, not just security metrics.

**Bonus / Common mistakes:**

- Bonus: idempotency keys on every mutating tool, plus post-execution verification.
- Mistake: relying on a refusal prompt for actions with irreversible consequences.

#### 8. How do you balance cost and quality in a production Agent?

**Answer points:**

- Route by difficulty: a small model for routing and common cases, a larger model for complex reasoning.
- Cache stable retrieval and template answers; invalidate by freshness policy.
- Set per-request budgets: max steps, max tokens, wall-clock deadline, max tool calls.
- Monitor cost per task and per tenant; alert on anomalies.
- Optimize the loop before adding models: fewer redundant tool calls and better stop conditions often beat a bigger model.

**What the interviewer wants to hear:**

- Trade-off: a bigger model improves quality but multiplies cost and latency; measure the quality delta on the eval set before switching.
- Production counterexample: a team doubled the model size and the eval score barely moved, because the bottleneck was retrieval quality, not reasoning.
- Data thinking: plot quality against cost per task; the frontier decides whether to spend more tokens or fix the pipeline.

**Bonus / Common mistakes:**

- Bonus: shadow traffic with cost tracking before any model switch.
- Mistake: optimizing token cost while ignoring latency and support burden — the cheapest answer that fails is not cheap.

## Follow-Up Bank

- Which item would block release by itself?
- What does a good incident root-cause look like in an agent system?
- How do you decide between blocking and warning gates?
- When do you cache a tool result and when do you call it live?
- How do you prove a regression fix actually prevents recurrence?

## Common Red Flags

- No eval set at all, or an eval set that never changes.
- Treating the dashboard as the eval gate.
- Safety enforced only in the prompt.
- No rollback plan, or a rollback plan never rehearsed.
- Postmortems without owners or action items.

## Portfolio Evidence

For L4, acceptable evidence is:

- An eval report with a versioned golden set and a regression gate in CI.
- An incident postmortem with impact, timeline, root cause, and verified actions.
- A production runbook covering rollback, degraded modes, and on-call procedures.
- A cost report showing per-task cost, latency, and quality trade-off decisions.

---
title: Production Checklist
validated_date: 2026-09-17
i18n-key: quick-reference-production-checklist
last-synced: 2026-09-17
---

# Production Checklist

Use this checklist before release, during incidents, and after postmortems. It is the fast lookup layer over the detailed production guides; each section points to the supporting document that explains the why.

## Purpose And Scope

This page is the operational gate for shipping and operating an Agent system. It applies to releases, incident response, and follow-up actions. It assumes you have already read the production guides; use it as the executable summary during the actual release and incident.

Supporting guides:

- [`../production/evals-checklist.md`](../production/evals-checklist.md): release-gate evals.
- [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md): required trace fields.
- [`../production/safety-checklist.md`](../production/safety-checklist.md): auth, tool, and memory controls.
- [`../production/quarterly-maintenance.md`](../production/quarterly-maintenance.md): freshness and deprecation.
- [`../production/cost-stability-operations.md`](../production/cost-stability-operations.md): budgets and guardrails.

## Before Release

- [ ] Auth and permissions are defined.
- [ ] Tool allowlist and risk classification exist.
- [ ] Destructive actions require confirmation.
- [ ] Safety evals pass.
- [ ] Golden prompts pass.
- [ ] Trace fields are present.
- [ ] Rollback plan is documented.
- [ ] Cost and latency budgets are set.
- [ ] Incident owner is named.
- [ ] PII handling and data retention are documented.
- [ ] Rate limits and retry budgets are defined.
- [ ] Model/provider failure fallback is tested.
- [ ] Regression gate blocks safety and eval failures.
- [ ] Human escalation path is documented.

## During Incident

- [ ] Disable risky action path.
- [ ] Freeze writes if needed.
- [ ] Inspect traces.
- [ ] Identify root cause.
- [ ] Add regression eval.
- [ ] Document postmortem.
- [ ] Notify stakeholders with blast radius.
- [ ] Capture before/after evidence from traces and logs.
- [ ] Confirm rollback or mitigation is effective.

## After Incident

- [ ] Fix owner and due date assigned.
- [ ] Rollback tested.
- [ ] Evals updated.
- [ ] Documentation updated.
- [ ] Follow-up monitored.
- [ ] Preventive guardrail added.
- [ ] Action items linked from postmortem.

## Run The Gate

Before release, run the deterministic regression gate and the repository checks:

```bash
python -m unittest labs.l4.regression_gate.test_lab
python scripts/check_repository.py
```

Expected output ends with `OK` for the test and `Repository checks passed` for the script.

## Severity And Response Times

| Severity | Example | Response Target | First Action |
| --- | --- | --- | --- |
| S0 | Data loss, unsafe tool execution | 15 min | Disable risky path, freeze writes |
| S1 | Wrong answer at scale, cost runaway | 60 min | Inspect traces, identify root cause |
| S2 | Localized incorrect behavior | Next business day | Add regression eval |
| S3 | Cosmetic or doc issue | Next quarterly review | File issue with owner |

## Roles And Responsibilities

| Role | Release | Incident |
| --- | --- | --- |
| Release manager | Runs the gate, signs the release | Coordinates mitigation and rollback |
| Incident responder | — | Owns the timeline and root cause |
| Eval owner | Runs and records evals | Adds regression cases |
| On-call engineer | Verifies budgets and fallbacks | Executes the runbook |
| Security reviewer | Approves destructive-action policy | Verifies guardrail verdicts in traces |

## Common Failures And Handling

| Failure | Symptom | Handling |
| --- | --- | --- |
| Safety eval fails at the gate | `regression_gate` test fails | Block release, fix the guardrail, rerun the suite |
| Missing trace field | Postmortem cannot be reproduced | Backfill the field in the contract and redeploy |
| Cost runaway | Bill spikes after a prompt change | Enable cost guardrails, roll back the prompt, add a budget alert |
| Fallback not tested | Provider outage takes the Agent down | Add a fallback test to the pre-release gate |
| Escalation path missing | Incident owner cannot be found | Name the owner before release and document the path |

## Worked Example

Pre-release run for `2026-09-17`:

```bash
python -m unittest labs.l4.regression_gate.test_lab
```

Result: `OK`. Repository checks pass. Release approved for canary with the incident owner named and the rollback plan recorded in the release ticket.

## Postmortem Template

Use [`../../../templates/postmortem-template.md`](../../../templates/postmortem-template.md) and link every action item back to the postmortem:

| Action | Owner | Due | Type |
| --- | --- | --- | --- |
| Add stale-source guardrail | eval owner | 2026-09-24 | Prevention |
| Backfill trace field | trace owner | 2026-09-24 | Prevention |
| Update golden prompts | eval owner | 2026-09-20 | Fix |

## Post-Release Follow-Up

Within one business day after a release, confirm:

- [ ] Release notes and version anchor updated (`validated_date`, `tested_against`).
- [ ] Traces for the canary window reviewed for required fields.
- [ ] Budget usage compared with the plan; any overage has an owner.
- [ ] Evals re-run on the shipped model/prompt versions.
- [ ] Rollback trigger conditions documented for the on-call engineer.
- [ ] Stakeholder update sent with measured blast radius and mitigation status.

## Canary And Rollback Decision Matrix

| Condition | Decision |
| --- | --- |
| All blocking evals pass, traces complete, budgets in range | Ship full rollout |
| Non-blocking eval failures only, bounded risk | Canary at 10%, re-evaluate after 24 h |
| Safety eval failure or missing trace field | Block, do not release |
| Latency/cost exceeds threshold | Roll back to previous prompt/model version |
| Tool behavior change affects destructive actions | Roll back and re-run tool usage evals |
| Fallback path exercised and verified | Keep rollout, document verification |

## Key Metrics

| Metric | Checkpoint | Alarm Level |
| --- | --- | --- |
| Safety eval pass rate | Release gate | 100% required |
| Golden pass rate | Release gate | No regressions |
| Trace completeness | Canary window | 100% |
| p95 latency | Release gate + canary | Budget |
| Cost per task | Release gate + canary | Budget |
| Rollback time | Drill, quarterly | ≤ 15 min |
| Error rate | Canary window | Above baseline x2 |

## Approval And Escalation Path

- [ ] On-call engineer holds the rollback trigger and the documented runbook.
- [ ] Destructive-action approvals use a named approver, not the Agent itself.
- [ ] Budget overrides require a written exception with expiry and monitoring plan.
- [ ] S0 incidents escalate to the release manager and security reviewer within 15 min.
- [ ] Every override is linked to a postmortem or a dated risk decision.

## Verification Commands

Run these commands and record their output in the release ticket:

```bash
# 1. Regression gate (deterministic, no API keys)
python -m unittest labs.l4.regression_gate.test_lab

# 2. Cost and stability guardrails
python -m unittest labs.l4.cost_and_stability_guardrails.test_lab

# 3. Full Lab suite for large changes
python -m unittest discover -s labs -p "test_*.py"

# 4. Repository checks (links, frontmatter, bilingual pairs)
python scripts/check_repository.py
```

Record expected results:

| Command | Pass condition |
| --- | --- |
| `regression_gate` test | Ends with `OK` |
| `cost_and_stability_guardrails` test | Ends with `OK` |
| Full Lab suite | All tests pass |
| `check_repository.py` | Prints `Repository checks passed` |

## Definition Of Done

A release is done when all of the following hold:

- [ ] Release gate passed on the exact shipped model/prompt versions.
- [ ] Trace schema validated against the canary window.
- [ ] Budget report signed off by the release manager.
- [ ] Rollback plan exercised in the last quarterly drill.
- [ ] Incident owner, escalation path, and stakeholder list recorded.
- [ ] Evals and checklists updated, and the documentation links are current.
- [ ] No unresolved S0/S1 items in the post-release review.

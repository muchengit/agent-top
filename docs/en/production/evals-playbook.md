---
title: Agent Evaluation And Regression Playbook
validated_date: 2026-09-17
i18n-key: production-evals-playbook
last-synced: 2026-09-17
---

# Agent Evaluation And Regression Playbook

Use this playbook to turn a change into a measurable release decision.

## When To Use

Use it before changing prompts, models, tools, retrieval, memory, routing, guardrails, or production release logic.

## 1. Define The Change Surface

List what changed and what could break.

| Change | Risk Area | Eval Needed | Owner |
| --- | --- | --- | --- |
| Prompt | answer quality, refusal, citations | golden prompts + safety |  |
| Model | format drift, latency, cost | golden prompts + latency/cost |  |
| Tool schema | invalid args, denied tools | tool usage |  |
| Retrieval | missing/stale sources | citation and refusal |  |
| Memory | stale preferences | conflict and expiry |  |
| Router | wrong specialist | route decision |  |
| Guardrail | false block/miss | safety and usability |  |

## 2. Build A Minimal Eval Matrix

Every Agent change needs at least these rows:

| Eval Class | Example Case | Expected Result | Blocking? |
| --- | --- | --- | --- |
| Golden path | Core user task | Answer with required evidence | Yes |
| Missing evidence | Source not retrieved | Refuse or ask clarification | Yes |
| Stale source | Old policy source | Do not answer from stale source | Yes |
| Tool failure | Tool timeout/error | Safe fallback or escalation | Yes |
| Destructive action | Delete/refund/request | Require approval before execution | Yes |
| Prompt injection | Retrieved doc tries to change policy | Ignore injected instruction | Yes |
| Ambiguous request | Missing user identity/intent | Clarify | No |
| Cost/latency | Long tool loop | Respect budget or degrade | Yes if over gate |

## 3. Write Cases

Each eval case should include:

- `id`: stable name.
- `input`: user request.
- `context`: sources, memory, tool availability.
- `expected_action`: answer, clarify, refuse, tool, escalate.
- `expected_evidence`: source IDs, tool result, or trace fields.
- `blocking`: whether failure blocks release.

## 4. Run And Record

Use the L4 regression gate Lab as the deterministic baseline:

```bash
python -m unittest labs.l4.regression_gate.test_lab
```

Record:

- Total cases.
- Pass/fail by class.
- Blocking failures.
- Cost and latency budget status.
- Rollback availability.
- Trace completeness.

## 5. Release Decision

Ship only when all blocking gates pass.

| Decision | Use When |
| --- | --- |
| Ship | No blocking failures; budgets pass; rollback ready |
| Canary | Non-blocking issues exist but risk is bounded |
| Block | Any critical safety, destructive action, missing trace, or missing rollback issue |
| Rollback | Production evidence shows unacceptable regression |

## 6. Failure Action

Every failure must become one of:

- A new eval case.
- A guardrail change.
- A trace field.
- A rollback note.
- A product decision.
- A postmortem action item.

## Eval-as-CI

Treat evaluation as a CI gate, not a post-release audit:

- Bind every prompt/model/tool/retrieval change to a dataset version.
- Require pass/fail rules for every blocking case.
- Record the release decision as Ship, Canary, Block, or Rollback.
- Convert every failure into an eval case, guardrail, trace field, rollback note, or postmortem action.

Minimum report fields:

```text
dataset_version:
matrix_version:
blocking_failures:
cost_status:
latency_status:
trace_completeness:
decision:
follow_up_owner:
```

## Experiment Evidence

Treat experiment tracking as evidence, not only as a dashboard:

- Bind every prompt/model/tool/dataset change to a run id.
- Record parameters, metrics, artifacts, owner, and decision for every run.
- State the baseline and candidate for every comparison.
- Decide Ship, Canary, Block, or Rollback from replayable experiment evidence.

Minimum experiment fields:

```text
run_id:
baseline_run_id:
candidate_run_id:
parameters:
metrics:
artifacts:
owner:
decision:
```

## GitHub Actions Evidence

Use CI workflow evidence to make release decisions replayable:

- Pin every action used in the gate, or record why the ref is intentionally moving.
- Bind the release decision to the exact commit SHA, workflow run id, and evaluated matrix version.
- Record the Python or runtime setup version used by the workflow.
- Store artifact identity with the decision: artifact name, artifact SHA, and download/provenance owner.
- Store cache identity with the decision: cache key, cache hit/miss, and owner responsible for invalidation.
- For every Block, Canary, Rollback, or Request Evidence decision, record owner and next action.

Minimum release-gate fields:

```text
workflow_run_id:
commit_sha:
action_ref:
setup_version:
artifact_sha:
cache_key:
decision:
owner:
rollback:
```

See [`../../../examples/release-gate-evidence/README.md`](../../../examples/release-gate-evidence/README.md) for a fictional evidence exercise with answer key.

## 7. Report Template

Use [`../../../templates/eval-report-template.md`](../../../templates/eval-report-template.md) for a copyable report. Example structure:

```markdown
# Eval Report

- Change:
- Date:
- Owner:
- Eval matrix version:

## Results
- Cases passed:
- Cases failed:
- Blocking failures:
- Safety failures:
- Tool failures:
- Retrieval failures:
- Cost status:
- Latency status:
- Trace completeness:
- Rollback ready:

## Decision
Ship / canary / block / rollback

## Follow-Up
- Owner:
- Due date:
- Regression case added:
```

## Related Pages

- Eval checklist: [`evals-checklist.md`](evals-checklist.md)
- Production checklist: [`../quick-reference/production-checklist.md`](../quick-reference/production-checklist.md)
- Regression gate Lab: [`../../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md)

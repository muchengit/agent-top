---
title: Good First L5 Candidates
validated_date: 2026-09-17
i18n-key: community-good-first-l5-candidates
last-synced: 2026-09-17
---

# Good First L5 Candidates

These are candidate packages for contributors preparing their first L5 evidence bundle. They are intentionally scoped so reviewers can evaluate pattern quality, governance evidence, and influence artifacts without reading private systems.

## Pattern Contribution: Evidence-Gated Memory Write

Problem: agents often write preferences into memory too early or overwrite stronger evidence.

Deliverables:

- Pattern contract with inputs, outputs, safety checks, verification, and rollback.
- Deterministic Lab or example showing source preference, uncertainty threshold, and write refusal.
- Eval report with conflict cases, stale-preference cases, and successful memory-write cases.
- Design review with rejected alternatives: prompt-only memory, vector recall as truth, and unrestricted memory writes.

Suggested labels: `good-first-L5`, `original-pattern`, `eval-evidence`, `safety-review`.

## Pattern Contribution: Tool Risk Preflight

Problem: tool calls can cross read/write/destructive boundaries without clear confirmation.

Deliverables:

- Risk classification contract for read, write, destructive, and external-state-changing tools.
- Preflight checklist and rollback hint template.
- Example trace showing block, approve-with-conditions, and approved execution.
- Review notes for maintainers covering destructive-action policy and audit fields.

Suggested labels: `good-first-L5`, `original-pattern`, `safety-review`, `eval-evidence`.

## Governance Contribution: SIG Charter for Evals and Regression

Problem: eval quality becomes scattered unless evaluation work has ownership.

Deliverables:

- Lightweight charter for an Evaluations SIG or working group.
- Backlog and decision-log template.
- Monthly health update template covering eval coverage, blocker count, review latency, and release instability.
- Contributor guide showing how learners can submit reviewed eval evidence.

Suggested labels: `good-first-L5`, `release-governance`, `sig-candidate`, `external-impact`.

## Ambassador Contribution: Workshop on Evidence Bundles

Problem: learners know the words `agent`, `eval`, and `trace`, but cannot package proof.

Deliverables:

- 30-minute workshop outline.
- One worked example using the L5 evidence template.
- Audience checklist and facilitator notes.
- Link to follow-up issue or contribution path.

Suggested labels: `good-first-L5`, `external-impact`, `original-pattern`.

## Reviewer Contribution: L5 Evidence Review Pack

Problem: maintainers lack a consistent review checklist for expert-level claims.

Deliverables:

- Reviewer guide mapping rubric dimensions to concrete evidence.
- Comments examples for approve, approve-with-conditions, rework, and stop.
- Checklist for detecting overclaimed L5 readiness.
- Bilingual review notes.

Suggested labels: `good-first-L5`, `safety-review`, `release-governance`, `external-impact`.

## How To Use This Page

1. Pick one candidate package.
2. Create an issue or PR using the relevant L5 labels.
3. Link the L5 expert evidence template.
4. Include at least one failure path and one rejected alternative.
5. Ask for reviewer feedback before expanding the work.


---
title: Maintainer Rotation
validated_date: 2026-09-17
i18n-key: community-maintainer-rotation
last-synced: 2026-09-17
---

# Maintainer Rotation

## Goal and Value

Maintainer rotation prevents burnout, keeps the bus factor low, and keeps review standards consistent when the busiest people step away. Rotating ownership quarterly means every active module has at least two people who understand it, and no single person becomes the invisible dependency of the project.

The rotation is also a training path: a reviewer who backs up a module for one quarter is ready to lead it the next quarter.

## Roles and Definitions

- **Module**: a reviewable area of the repo, such as `docs/en/community`, `docs/zh`, `templates`, `labs/l1`, CI configuration, or the production checklists under `docs/en/production`.
- **Module lead**: the person responsible for routing review, chasing stale content, and reporting status.
- **Backup maintainer**: the person who covers for the lead and reviews the same module without leading it.
- **Rotation maintainer**: the lead for the current quarter, tracked in a pinned issue.
- **On-call window**: the two weeks before the handoff when the outgoing lead must close or reassign open items.

## Rotation Cadence

- One quarter per term: January-March, April-June, July-September, October-December.
- Handoff happens in the last week of the term; new terms start on the first working day.
- Each active module needs at least two maintainers or backups.
- The same person must not author and review the same module in the same month.

Quarter boundaries for 2026:

| Term | Handoff week | New term starts |
| --- | --- | --- |
| Q1 (Jan-Mar) | Mar 23-27 | Apr 1 |
| Q2 (Apr-Jun) | Jun 22-26 | Jul 1 |
| Q3 (Jul-Sep) | Sep 21-25 | Oct 1 |
| Q4 (Oct-Dec) | Dec 21-25 | Jan 1 (2027) |

## Maintainer Eligibility

A maintainer candidate should have, in the last two quarters:

- Reviewed at least six PRs across at least two modules.
- Kept local checks green before merging (`python scripts/check_repository.py`).
- Filed or fixed at least one stale or broken-content issue.
- Participated in one translation sync or review.
- No unresolved blocking review complaints.

Backup maintainers should meet half of these requirements and be approved by the current lead.

## Rotation Inputs

- Recent merged contributions per module.
- Review capacity: open PR count per reviewer.
- Translation sync load: pages whose `last-synced` is older than 14 days.
- CI and release readiness: red builds, failing tests, pending release notes.
- Burnout signals: review latency above 7 days, missed handoffs, reduced activity.
- Roadmap changes announced in [`agent-top-roadmap.md`](../../../agent-top-roadmap.md).

## Quarterly Handoff Checklist

1. Review active module ownership and update the pinned rotation issue.
2. Identify a backup maintainer for each module.
3. Update roadmap status in [`agent-top-roadmap.md`](../../../agent-top-roadmap.md).
4. Flag stale or abandoned modules with `sync-required` or `deprecated`.
5. Publish a short handoff note in Discussions or Issues.

## Handoff Procedure (Week-by-Week)

**Week 1 of the last month of the term** (e.g., Sep 1-5):

- Lead opens a handoff issue with the checklist above.
- Lead lists open PRs, blocked reviews, and translation debt.

**Week 2 (Sep 8-12):**

- Each module lead names their backup for the next term.
- New leads confirm willingness in the issue.

**Week 3 (Sep 15-19):**

- Outgoing leads hand over context: review style notes, open decisions, known risks.
- New leads shadow at least one review.

**Week 4 (Sep 22-26):**

- Outgoing lead closes or reassigns all open items older than 30 days.
- Core team approves the new rotation table.
- Handoff note is published.

## Duties During the Term

- Route every PR to the right review route (`reviewer-review` vs `maintainer-review`).
- Triage `translation-needed` and `sync-required` labels weekly.
- Keep `templates` and community docs consistent with [`labels.md`](labels.md).
- Block merging when version anchors (`tested_against`) are missing for framework-sensitive content.
- Coordinate translation review with the language reviewer.

## Judgment Criteria for a Successful Handoff

A handoff is complete when:

- Every module has a named lead and backup in the pinned issue.
- No open review has been waiting longer than 7 days.
- Translation debt is under 14 days per page.
- CI is green and `python scripts/check_repository.py` passes.
- The handoff note is published and linked from the community index.

## Common Issues and Handling

- **Only one person knows a module**: extend the backup window by one quarter before rotating.
- **Lead goes silent**: the backup takes over after two missed weekly check-ins.
- **Conflicting review standards**: new lead documents differences in the handoff note.
- **Too many modules for the team**: merge small modules and route through one lead.
- **Rotation causes review backlog**: keep the outgoing lead as reviewer for one month.

## Measurable Metrics

- Number of modules with two named owners (target: all active modules).
- Median review time per module (target: under 4 days).
- Share of reviews done by the lead vs backups (backup share should rise each quarter).
- Translation `last-synced` drift at quarter end.
- Handoff note published on time (target: 100%).
- Burnout flags raised per quarter (target: zero ignored).

## FAQ

- **What if a quarter starts without a backup?** Do not rotate; keep the lead and raise a hiring request.
- **Can a lead serve two terms in a row?** Only if no backup is ready; otherwise no.
- **Where is the rotation tracked?** In a pinned issue, updated each week.
- **Who approves the table?** The core team, during the handoff week.

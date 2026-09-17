---
title: Contributor of the Month
validated_date: 2026-09-17
i18n-key: community-contributor-of-the-month
last-synced: 2026-09-17
---

# Contributor of the Month

## Goal and Value

The Contributor of the Month program recognizes contributors who shipped meaningful, reviewable, and reproducible work during a calendar month. It exists to reward steady contributions over one-off activity and to make the community's review load sustainable by highlighting people whose work reduces maintenance burden.

A good award is not a popularity contest. It is a decision supported by evidence: merged PRs, review comments, translation sync commits, CI fixes, and unblocking help that other contributors can verify.

## Eligibility

Any contributor qualifies if, during the month, they met at least one of:

- Merged a tutorial, article, Lab, interview question, or case study.
- Merged a complete or partial translation that kept `i18n-key` and updated `last-synced`.
- Reviewed PRs with substantive, non-approval-only feedback.
- Fixed CI, templates, version anchors, or contribution workflows.
- Helped unblock other contributors in issues, Discussions, or Community Labs.
- Kept quality standards high through examples, checklists, and review feedback.

Inactive months do not disqualify anyone. A contributor can win again, but the previous win should not be the deciding factor.

## Nomination Window and Timeline

Use the following fixed schedule. Times are in Asia/Shanghai.

| Deadline | Action | Owner |
| --- | --- | --- |
| Day 25 of the month | Open the nomination issue | Maintainer on rotation |
| Day 26-28 | Collect evidence and comments | Contributors, reviewers |
| Day 29 | Core team confirms the winner | Core team |
| Day 30/31 | Publish the report and badge | Maintainer on rotation |
| First week of next month | Announce in showcase and release notes | Core team |

If a month ends on a weekend or a public holiday, move the deadline to the next working day and say so in the nomination issue.

## Roles

- **Nominator**: any maintainer or contributor who opens or adds evidence to the nomination issue.
- **Evidence collector**: the rotation maintainer, who links each candidate claim to a PR or comment.
- **Confirmer**: the core team, who checks the rules and confirms the winner.
- **Announcer**: the rotation maintainer, who publishes the report.

One person can play several roles, but the confirmer must not be the winner.

## Selection Criteria and Scoring

Score each candidate on a 10-point scale per dimension:

| Dimension | What counts as evidence | Weight |
| --- | --- | --- |
| Documentation quality | Merged docs with valid links, updated `validated_date` | 25% |
| Lab runnability | Labs with code, tests, and passing local checks | 25% |
| Translation or review quality | Sync commits, `last-synced` updates, review feedback | 20% |
| Helping newcomers | Replies that unblock, onboarding reviews, mentoring | 15% |
| Maintenance burden reduction | CI fixes, template updates, stale content flags | 15% |

A candidate needs at least 7.5 average to be considered. If no candidate reaches the bar, the award is skipped for the month; do not lower the bar.

## Selection Process

1. Rotation maintainer opens the nomination issue on day 25 with the candidate list from merged PRs.
2. Each candidate gets one top-level comment with linked evidence.
3. Reviewers and contributors add supporting or objecting comments until day 28.
4. Core team reviews the scoring table, applies the fairness rules, and confirms the winner on day 29.
5. Rotation maintainer fills in [`../../templates/monthly-contributor-report.md`](../../../templates/monthly-contributor-report.md) and publishes it in the community index.
6. The winner receives the badge and benefits described below.

## Benefits

- Badge in the next community showcase.
- One month of reduced review overhead for low-risk `docs-only` PRs.
- Priority visibility in release notes or roadmap reviews.
- Option to host one Community Lab session (use [`../../templates/community-lab-template.md`](../../../templates/community-lab-template.md)).

The reduced-review benefit applies only to `docs-only` PRs and does not skip the `maintainer-review` route.

## Templates and Tools

- Report template: [`../../templates/monthly-contributor-report.md`](../../../templates/monthly-contributor-report.md)
- Evidence checklist: [`../../templates/contribution-checklist.md`](../../../templates/contribution-checklist.md)
- Lab notes: [`../../templates/community-lab-template.md`](../../../templates/community-lab-template.md)
- Contribution paths: [`contribution-paths.md`](contribution-paths.md)
- Label reference: [`labels.md`](labels.md)

Fill in the report template directly. Do not copy it into a new location unless the copy is tracked.

## Fairness Rules

- The same person must not be both author and second reviewer of the same PR in the same month.
- Nominations must be evidence-linked; unsupported claims are dropped.
- Contributions must be reviewable, revertible, and reproducible.
- No self-nomination only; a second person must second the nomination.
- If the winner is also the rotation maintainer, the core team announces instead.

## Common Issues and Handling

- **Low evidence quality**: ask the collector to link PR numbers; if still thin, skip the award.
- **Tie between candidates**: compare review and newcomer-help scores first, then maintenance reduction.
- **Winner is on leave**: award stands; announcement waits until the winner can reply.
- **Duplicate awards to the same person**: allowed but require stronger evidence than the previous win.
- **Disputed nomination**: core team rechecks the scoring table in a public issue within 3 days.

## Measurable Metrics

Track these monthly and compare quarter over quarter:

- Number of nominations per month.
- Percentage of nominations with at least one linked PR.
- Winner's merged PR count and review comment count.
- Time from nomination issue to published report (target under 7 days).
- Share of winners from translation-only contributions (should not be zero).
- Number of months skipped (target under 2 per year).

## FAQ

- **Can a maintainer win?** Yes, but not in the same month they confirm the award.
- **Does a single big PR count?** It counts, but steady multi-PR contributions are preferred.
- **Can I nominate myself?** Yes, if a second contributor seconds it.
- **What if the month has no winner?** Skip and publish a short note explaining why.

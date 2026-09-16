---
title: Community Rhythm
validated_date: 2026-09-16
i18n-key: community-community-rhythm
last-synced: 2026-09-16
---

# Community Rhythm

Agent-Top keeps community work predictable so contributors know what to expect and maintainers can rotate ownership without burnout.

## Regular Events

- Biweekly tutorial release.
- Monthly interview question drop.
- Quarterly roadmap review.
- Biweekly paper or tutorial reading.
- Monthly showcase.
- Quarterly hackathon.
- Biweekly Agent Community Lab sessions for tutorial walkthroughs, interview practice, and article digests.

## Event Output Contract

Every event should produce one concrete artifact:

| Event | Required Artifact | Useful Labels |
| --- | --- | --- |
| Tutorial release | New or updated tutorial plus validation | `docs-only`, `lab`, `maintainer-review` if architecture changes |
| Interview drop | Questions, answer key, rubric note | `interview` |
| Roadmap review | Status update and next priority | `maintainer-review` |
| Reading session | Summary note, adopted pattern, or follow-up issue | `good first issue` |
| Showcase | Project link, trade-off summary, lesson learned | `production`, `lab` |
| Hackathon | Working repo, notes, or reusable pattern candidate | `lab`, `maintainer-review` |

## Event Guide

- Agent Community Lab sessions are lightweight group sessions with one host, one topic, and one artifact.
- Use the host script and notes template before each session.
- Keep the agenda small: 15 minutes context, 30 minutes practice, 15 minutes review and follow-up.

## Operating Rules

- Keep each event small enough for volunteer ownership.
- Rotate leads quarterly.
- Avoid stacking authoring and review on the same person.
- Publish outputs in the main docs tree unless they are optional attachments.
- Community Lab sessions should produce notes, a PR, a docs patch, or a follow-up issue.
- If a session discovers a stale example, open `sync-required` instead of silently editing around it.

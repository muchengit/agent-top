---
title: GitHub Labels
validated_date: 2026-09-16
i18n-key: community-labels
last-synced: 2026-09-16
---

# GitHub Labels

Labels help contributors find the right task and help maintainers route reviews without overloading the team.

## Label Guide

| Label | Meaning | Use For | Review Route |
| --- | --- | --- | --- |
| `good first issue` | Beginner-friendly contribution. | Scoped docs fixes, small Lab improvements, terminology cleanup | Reviewer |
| `docs-only` | Documentation-only change. | Markdown edits that do not change Lab behavior | Reviewer plus language check if ZH changes |
| `translation-needed` | Translation task available for claim. | EN source exists but ZH mirror needs work | Language reviewer plus owner if content is sensitive |
| `sync-required` | EN/ZH content is out of sync. | `last-synced` drift or missing paired content | Maintainer when stale or conflicting |
| `deprecated` | Content should point to a replacement. | Outdated examples or replaced guidance | Maintainer review for replacement path |
| `breaking-change` | Framework or SDK change may affect examples. | Version anchors, Lab behavior, or framework examples | Maintainer review |
| `maintainer-review` | Architecture or safety review required. | Production, security, tool risk, or multi-agent topology changes | Maintainer |
| `lab` | Runnable Lab content. | Code, tests, README for Labs | Reviewer plus test evidence |
| `interview` | Interview question or rubric content. | Questions, answer keys, scoring rubrics | Content reviewer |
| `production` | Production, safety, eval, or postmortem content. | Release gates, incidents, rollback, observability | Maintainer or production reviewer |

## Usage Rules

- Use one primary topic label plus route labels.
- Prefer `good first issue` only when the task can be completed and reviewed independently.
- Use `translation-needed` only when the EN source is stable enough to translate.
- Use `sync-required` when EN and ZH diverge after a source update.
- Use `maintainer-review` for architecture, security, production, or breaking changes.
- Do not use `deprecated` without a replacement link or next-step guidance.

## Label Hygiene

- Avoid stacking labels just to get attention.
- Remove stale labels before closing an issue or PR.
- If a PR changes multiple areas, mention the main review route in the description.
- If a translation is blocked by an unstable EN source, comment with the blocker before claiming.

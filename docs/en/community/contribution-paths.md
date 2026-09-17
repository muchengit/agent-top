---
title: Contribution Paths
validated_date: 2026-09-16
i18n-key: community-contribution-paths
last-synced: 2026-09-16
---

# Contribution Paths

Agent-Top has four main contribution paths.

## 1. Writing

Write new tutorials, concepts, or Labs.

Good writing contribution:

- Has a clear goal.
- Links to relevant labs or templates.
- Includes expected outputs.
- Explains trade-offs.
- Passes repository checks.

## 2. Translation

Translate English source content into Chinese.

Translation contribution:

- Uses the same `i18n-key`.
- Updates `last-synced`.
- Keeps technical terms consistent with the glossary.
- Leaves `translation-needed` closed only after review.

## 3. Review

Review content for correctness, clarity, and maintainability.

Review contribution should check:

- Accuracy.
- Broken links.
- Version anchors.
- Bilingual sync.
- Lab runnability.
- Trade-off explanations.

## 4. Maintenance

Maintain framework maps, CI, templates, and release hygiene.

## 5. L5 Expert Evidence

Submit evidence packages for L5 contributions: original patterns, architecture review, eval/trace/risk/release evidence, external influence artifacts, and mentoring/review proof. Use [`good-first-L5-candidates.md`](good-first-L5-candidates.md) for candidate L5 packages when preparing an issue or PR.

Maintenance contribution:

- Keeps CI green.
- Handles stale or breaking-change content.
- Rotates reviewers.
- Prevents documentation sprawl.

## Labels

Start with:

- `good first issue`
- `docs-only`
- `translation-needed`
- `sync-required`
- `lab`
- `good-first-L5`
- `original-pattern`
- `external-impact`

## Community Lab Sessions

Community Lab sessions are a contribution path when they produce docs, Labs, translations, review notes, or follow-up issues. Use `docs-only` for writing-only patches and `lab` for runnable examples.

## Review Policy

Same person should not be author and both reviewers in the same month. Core contributors can use Contributor of the Month review exemption when workload allows.

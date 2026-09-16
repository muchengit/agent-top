---
title: Translation Workflow
validated_date: 2026-09-16
---

# Translation Workflow

## Principle

English is the primary source. Chinese translation is a first-class contribution path, not an afterthought.

## Steps

1. Add or update English source in `docs/en/`.
2. Mark the issue with `translation-needed`.
3. Contributor claims the translation task and records ownership in the issue.
4. Create or update the matching file in `docs/zh/`.
5. Keep `i18n-key` aligned between EN and ZH files.
6. Update `last-synced` to the translation completion date.
7. Run repository checks.
8. Open a PR and request content + language review.

## Quality Bar

- No meaning drift from the English source.
- Technical terms follow `docs/community/glossary.md`.
- `translation-needed` remains until the ZH PR is merged.
- `sync-required` is opened when EN changes after ZH without matching translation.

## SLA

Each chapter should receive ZH coverage within 3 days of claim.

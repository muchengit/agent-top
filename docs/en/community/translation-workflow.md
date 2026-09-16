---
title: Translation Workflow
validated_date: 2026-09-16
i18n-key: community-translation-workflow
last-synced: 2026-09-16
---

# Translation Workflow

English content under `docs/en` is the primary source. Chinese content under `docs/zh` must stay synchronized through explicit metadata.

## Required Metadata

Both EN and ZH files need:

```yaml
i18n-key: stable-key
last-synced: YYYY-MM-DD
```

## Workflow

1. English source changes.
2. Add or update `i18n-key`.
3. Open or assign `translation-needed`.
4. Translation contributor updates the ZH file.
5. Reviewer checks meaning, terminology, and links.
6. Maintainer checks `last-synced`.
7. If sync lags, CI or review should add `sync-required`.

## SLA

- Each chapter should reach Chinese within 3 working days when actively claimed.
- Translation sync rate should be within 14 days overall.
- Broken or outdated Chinese content should not stay silent; mark and route it.

## Glossary Use

Use the glossary for stable terms. Prefer consistency over local phrasing when the term appears in tutorials, interviews, and Labs.

## Common Issues

- English changed but `last-synced` was not updated.
- Chinese link target uses an old filename.
- Transliteration changes the meaning of MCP, RAG, or ReAct.
- Framework names are translated when they should remain brand names.

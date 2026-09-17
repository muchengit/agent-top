---
title: Translation Workflow
validated_date: 2026-09-17
i18n-key: community-translation-workflow
last-synced: 2026-09-17
---

# Translation Workflow

English content under `docs/en` is the primary source. Chinese content under `docs/zh` must stay synchronized through explicit metadata. This document explains how translation tasks are claimed, how sync is tracked, and how CI catches lag.

## Goal and Value

Translation keeps the bilingual promise of the project: every concept page exists in both English and Chinese, with the same meaning, terminology, and runnable examples. A translation is not a free rewrite; it is a mirror that must remain reviewable and revertible.

## Roles

- **Source author**: the person who changes the English page.
- **Claimer**: the contributor who commits to translating one page.
- **Translator**: usually the same as the claimer; does the actual edit.
- **Language reviewer**: checks meaning, terminology, and natural Chinese.
- **Maintainer**: checks metadata (`i18n-key`, `last-synced`) and merges.

One person may combine roles, but the maintainer who merges should not be the only author of the same translation.

## The Metadata Mechanism

Every bilingual page carries the same two fields in frontmatter:

```yaml
i18n-key: stable-key
last-synced: YYYY-MM-DD
```

- `i18n-key` is a stable identifier shared by the EN and ZH pair. It must be byte-identical in both files. The repository check fails when an EN key has no ZH pair.
- `last-synced` records the date when the ZH page was last brought in line with the accepted EN source. It is updated by the translator or the language reviewer, never by the source author alone.

Example pairing:

| Language | File | i18n-key |
| --- | --- | --- |
| English | `docs/en/community/translation-workflow.md` | `community-translation-workflow` |
| Chinese | `docs/zh/community/翻译流程.md` | `community-translation-workflow` |

## How `translation-needed` Claiming Works

1. The source author opens an issue with label `translation-needed` and links the EN page.
2. A contributor comments `I'll take this` plus a target date. That reserves the task for 7 days.
3. The claimer updates the ZH page and opens a PR that references the issue.
4. The language reviewer approves meaning and terminology; the maintainer checks `last-synced`.
5. Only after merge does anyone remove `translation-needed`. If the PR is closed without merge, the label stays.

If a claimer misses the 7-day reservation, the task is released and may be re-claimed by someone else. Claimers should not hold more than two translations at once.

## Step-by-Step Workflow

1. English source changes and is merged.
2. The changelog or PR description lists which pages changed.
3. A maintainer adds `translation-needed` to the related issue.
4. A contributor claims the page and checks the glossary.
5. The translator updates the ZH file, including links and metadata.
6. The reviewer checks meaning, terminology, and links.
7. The maintainer verifies `last-synced` and merges.
8. If sync lags, CI or review adds `sync-required` and the page is routed.

## SLA

- Actively claimed translations must reach Chinese within 3 working days.
- Overall sync rate must stay within 14 days from source change to merged ZH page.
- Broken or outdated Chinese content must not stay silent: mark it `sync-required` and route it.

## Tools and Templates

- Glossary for stable terms: [`glossary.md`](glossary.md)
- Chinese glossary mirror: [`../../zh/community/术语表.md`](../../zh/community/术语表.md)
- Label rules: [`labels.md`](labels.md)
- Bilingual checklist: [`../../templates/contribution-checklist.md`](../../../templates/contribution-checklist.md)
- Writing guide for case studies: [`../../templates/case-study-writing-guide.md`](../../../templates/case-study-writing-guide.md)

## How CI Detects Lag

The repository gate `python scripts/check_repository.py` runs these checks:

- **Pair check**: every `i18n-key` present in `docs/en` must also exist in `docs/zh` and vice versa. An EN page with no ZH mirror fails.
- **Frontmatter check**: every page under `docs/en` and `docs/zh` must carry both `i18n-key` and `last-synced`.
- **Link check**: every relative link must resolve to a real file; a ZH page pointing to an old English filename fails.
- **Staleness check**: `validated_date` older than 180 days fails.

`last-synced` drift is not yet auto-compared with the EN git history, so reviewers must compare the dates manually. When the drift is older than 14 days, add `sync-required` and open a follow-up issue.

## Glossary Usage

- Use [`glossary.md`](glossary.md) as the single source of truth.
- Keep framework, brand, and protocol names unchanged: MCP, RAG, ReAct stay as-is.
- When the glossary offers no entry, prefer the most established Chinese community term and record it.
- Consistency beats clever local phrasing in tutorials, interviews, and Labs.

## Common Issues and Handling

- **English changed but `last-synced` not updated**: reviewer returns the PR; translator updates the date.
- **Chinese link target uses an old filename**: run the repository check to catch it.
- **Transliteration changes meaning of MCP, RAG, or ReAct**: revert to the glossary form.
- **Framework names translated**: keep brand names; only translate descriptions.
- **Two people claim the same page**: first comment wins; the second coordinates or picks another page.
- **EN source is unstable**: do not claim; comment with the blocker and wait for `docs-only` stabilization.

## Review Checklist

- `i18n-key` matches the paired file byte-for-byte.
- `last-synced` matches the latest accepted source update.
- Chinese links point to Chinese filenames where available.
- Framework names, brand names, and protocol names remain unchanged unless the glossary says otherwise.
- Technical terms are consistent with the glossary.
- Examples are not accidentally localized in a way that changes API, code, or command behavior.
- The translated page has no placeholder text or untranslated headings.

## Measurable Metrics

- Translation sync rate within 14 days (target: 100% of active pages).
- Claim-to-merge time (target: under 3 working days).
- Share of `translation-needed` issues that are re-claimed (target: under 20%).
- Number of `sync-required` issues opened per month (track, do not aim to zero).
- Percentage of ZH pages whose `last-synced` is current (target: above 90%).

## FAQ

- **Can I translate a page no one asked for?** Yes, but open an issue with `translation-needed` first so nobody duplicates it.
- **Who owns `last-synced`?** The translator updates it; the maintainer verifies it.
- **What if EN and ZH both changed?** Treat EN as source; re-derive the ZH page from EN.
- **Do I translate file names?** No, keep the stable key; only content and visible headings change.

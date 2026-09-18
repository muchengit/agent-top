---
title: Community Guide Index
validated_date: 2026-09-16
i18n-key: community-readme
last-synced: 2026-09-18
---

# Community Guide

Agent-Top is maintained as a bilingual, docs-first open source community.

## Start Here

- New contributors: [`contributor-onboarding.md`](contributor-onboarding.md)
- Writing or translating docs: [`contribution-paths.md`](contribution-paths.md)
- Translating EN to ZH: [`translation-workflow.md`](translation-workflow.md)
- Running labs: [`../../quick-reference/lab-command-cheatsheet.md`](../quick-reference/lab-command-cheatsheet.md)

## Core Links

- [`contribution-paths.md`](contribution-paths.md)
- [`contributor-onboarding.md`](contributor-onboarding.md)
- [`translation-workflow.md`](translation-workflow.md)
- [`community-rhythm.md`](community-rhythm.md)
- [`agent-community-lab.md`](agent-community-lab.md)
- [`community-lab-host-script.md`](community-lab-host-script.md)
- [`labels.md`](labels.md)
- [`glossary.md`](glossary.md)
- [`maintainer-rotation.md`](maintainer-rotation.md)
- [`contributor-of-the-month.md`](contributor-of-the-month.md)
- [`2026-09-contributor-report.md`](2026-09-contributor-report.md)
- [`experiment-log.md`](experiment-log.md)
- [`good-first-L5-candidates.md`](good-first-L5-candidates.md)

## Role Paths

| Role | Best First Tasks | Review Expectation |
| --- | --- | --- |
| Contributor | docs-only fixes, translation-needed pages, Lab improvements | One reviewer plus language check when Chinese changes |
| Reviewer | ordinary Lab/docs review, terminology checks | Must not review their own same-month content |
| Maintainer | architecture, safety, production, release-sensitive changes | Must keep stable patterns separate from framework code |
| Core | roadmap, governance, contributor recognition | Focuses on sustainability and review load |

## Good First Issue Rules

A good first issue should be:

- Scoped to one file or one small Lab.
- Testable with `python scripts/check_repository.py` or a Lab test.
- Clear about expected output and acceptance criteria.
- Marked with the right label: `good first issue`, `docs-only`, `translation-needed`, or `sync-required`.

## Before Submitting

- Update `validated_date` when touching examples.
- Preserve `tested_against` when touching Labs.
- Keep framework-specific code in Labs, not concept docs.
- Add bilingual metadata for docs under `docs/en` and `docs/zh`.
- Run: `python scripts/check_repository.py`.

## Community Norms

- Markdown + executable Lab is the default content format.
- English is the primary source; Chinese content is tracked with `i18n-key` and `last-synced`.
- Good first issues should be scoped and testable.
- Production content needs version anchors.
- Review quality should stay sustainable.

---
title: Roadmap Status
validated_date: 2026-09-16
---

# Roadmap Status

## Current State

| Area | Status | Evidence |
| --- | --- | --- |
| Repository basics | Done | `README.md`, `README.zh-CN.md`, `LICENSE`, `.gitignore` |
| Framework docs | Done | `docs/agent-top-concrete-framework.md` |
| Concepts | Done | `docs/concepts/` |
| Framework map | Done | `docs/frameworks/framework-map.md` |
| Executable Labs | Done | `labs/l0` through `labs/l5` |
| Interview assets | Done | `docs/interviews/` |
| Portfolio tracks | Done | `docs/portfolio/projects.md` |
| Production guides | Done | `docs/production/` |
| Community governance | Done | `GOVERNANCE.md`, `CONTRIBUTING.md`, `docs/community/` |
| Bilingual seed | Done | `docs/en/`, `docs/zh/` through L5 |
| Bilingual metadata | Done | frontmatter key and sync checks in `scripts/check_repository.py` |
| Community operations | Done | `docs/community/community-rhythm.md`, `docs/community/labels.md` |
| Community closed loops | Done | `docs/community/translation-workflow.md`, `docs/community/contributor-of-the-month.md`, `docs/community/maintainer-rotation.md` |
| GitHub labels config | Done | `.github/labels.yml` |
| Contributor onboarding | Done | `docs/community/contributor-onboarding.md` |
| Security policy | Done | `SECURITY.md` |
| Maintenance process | Done | `docs/production/quarterly-maintenance.md`, `templates/monthly-contributor-report.md` |
| CI checks | Done | `.github/workflows/ci.yml` |

## Health Targets

| Metric | Target |
| --- | --- |
| Dead link rate | < 1% |
| Bilingual sync | <= 14 days |
| Framework example freshness | reviewed before stale threshold |
| Review coverage | >= 2 backups per active module |

## Next Priority

Expand L2+ executable Labs with real framework integrations while keeping framework-specific code isolated.

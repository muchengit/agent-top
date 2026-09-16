---
title: Roadmap Status
validated_date: 2026-09-16
---

# Roadmap Status

## Current State

| Area | Status | Evidence |
| --- | --- | --- |
| Repository basics | Done | `README.md`, `README.zh-CN.md`, `LICENSE`, `.gitignore` |
| Concrete framework | Done | `docs/en/agent-top-concrete-framework.md` |
| Concepts | Done | `docs/en/concepts/`, including architecture and multi-round research flows |
| Framework map | Done | `docs/en/frameworks/framework-map.md` |
| Executable Labs | Done | `labs/l0` through `labs/l5`, including supplementary labs |
| Detailed tutorials | Done | `docs/en/` and `docs/zh/` through L5 |
| Tutorial reference map | Done | `docs/en/tutorials/reference-map.md`, `docs/zh/tutorials/reference-map.md` |
| Chinese tutorial filenames | Done | Chinese names under `docs/zh/` |
| Interview assets | Done | `docs/en/interviews/interview-framework.md`, `docs/en/interviews/questions/`, `docs/en/interviews/interview-answer-framework.md` |
| Portfolio tracks | Done | `docs/en/portfolio/projects.md`, `docs/en/portfolio/personal-agent-portfolio.md`, `docs/en/portfolio/open-source-impact-guide.md` |
| Production guides | Done | `docs/en/production/`, `docs/en/production/cost-stability-operations.md`, `docs/en/quick-reference/production-checklist.md` |
| Case studies | Done | `docs/en/cases/` and `docs/zh/cases/`, including enterprise tool, collaboration, RAG, regression, and pattern-contribution cases |
| Quick references | Done | `docs/en/quick-reference/`, including Chinese index |
| Agent skills | Done | `docs/en/skills/README.md`, `docs/zh/skills/Agent技能矩阵.md`, `templates/agent-skill-card-template.md` |
| Community governance | Done | `GOVERNANCE.md`, `CONTRIBUTING.md`, `CONTRIBUTING.zh-CN.md`, `docs/en/community/` |
| Bilingual metadata | Done | frontmatter key and sync checks in `scripts/check_repository.py` |
| Community operations | Done | rhythm, labels, maintainer rotation, translation workflow |
| GitHub labels config | Done | `.github/labels.yml` |
| Contributor onboarding | Done | `docs/en/community/contributor-onboarding.md` |
| Security policy | Done | `SECURITY.md` |
| Maintenance process | Done | `docs/en/production/quarterly-maintenance.md`, `templates/monthly-contributor-report.md` |
| CI checks | Done | `.github/workflows/ci.yml` |
| Reusable templates | Done | `templates/`, including Agent design and postmortem templates |

## Health Targets

| Metric | Target |
| --- | --- |
| Dead link rate | < 1% |
| Bilingual sync | <= 14 days |
| Framework example freshness | reviewed before stale threshold |
| Review coverage | >= 2 backups per active module |
| Tutorial coverage | L0-L5 EN and ZH present |
| Lab test coverage | 39 deterministic Lab tests pass locally |

## Next Priority

Continue improving coverage with more real-world examples, maintain bilingual SLA, and keep framework examples fresh through `sync-required` when APIs change.

## Completion Notes

The repository now includes the core learning framework, runnable Labs, bilingual L0-L5 tutorials, interview question banks, interview answer examples, portfolio tracks, open-source impact guidance, production guides, reusable design templates, community operations, governance, and CI checks.

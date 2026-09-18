---
title: Roadmap Status
validated_date: 2026-09-18
---

# Roadmap Status

## Current State

| Area | Status | Evidence |
| --- | --- | --- |
| Repository basics | Done | `README.md`, `README.zh-CN.md`, `LICENSE`, `.gitignore` |
| Concrete framework | Done | `docs/en/agent-top-concrete-framework.md` |
| Concepts | Done | `docs/en/concepts/`, including architecture, MCP, multi-agent scheduling, long-term memory, hallucination, plan decisions, deep-dive sources, and the implementation guide |
| Framework map | Done | `docs/en/frameworks/framework-map.md` |
| Executable Labs | Done | `labs/l0` through `labs/l5`, including supplementary labs |
| Task-first onboarding | Done | `docs/en/tutorials/quick-navigation.md`, `docs/zh/tutorials/快速导航卡.md`, `examples/README.md`, `examples/agent-decision-trace/`, `examples/rag-evidence-refusal/`, `examples/memory-vs-evidence/`, `examples/coding-workspace-safety/`, `examples/data-source-policy/`, `examples/coding-task-navigation/`, `examples/agent-eval-regression/`, `examples/github-agent-review/`, `examples/observability-trace/`, and `examples/model-gateway/`, `examples/safety-eval/`, `examples/mcp-tool-boundary/`, `examples/memory-index-evidence/`, `examples/release-gate-evidence/`, including runtime, gateway, safety, tool-boundary, index, and release-gate evidence |
| Design review assets | Done | `docs/en/concepts/design-review-workshop.md` and `docs/en/concepts/agent-system-blueprint.md` plus Chinese mirrors |
| Practice handbook | Done | `docs/en/tutorials/practice-handbook.md` plus Chinese mirror |
| Contribution assets | Done | Case study templates, contribution checklist, and enhanced PR template |
| Evaluation playbook | Done | `docs/en/production/evals-playbook.md` and Chinese mirror plus eval report template |
| Open-source pattern matrix | Done | `docs/en/tutorials/open-source-pattern-matrix.md`, Chinese mirror, `examples/memory-vs-evidence/`, `examples/coding-workspace-safety/`, `examples/data-source-policy/`, `examples/coding-task-navigation/`, `examples/agent-eval-regression/`, `examples/github-agent-review/`, `examples/observability-trace/`, and `examples/model-gateway/`, `examples/safety-eval/`, `examples/mcp-tool-boundary/`, `examples/memory-index-evidence/`, `examples/release-gate-evidence/`, including runtime, gateway, safety, tool-boundary, index, and release-gate evidence |
| Detailed tutorials | Done | `docs/en/` and `docs/zh/` through L5 |
| Industry benchmark and L5 expert path | Done | `docs/en/tutorials/industry-benchmark-and-l5-expert-path.md`, Chinese mirror, and `templates/l5-expert-evidence-template.md` |
| Team Agent infrastructure | Done | `docs/en/production/team-agent-infrastructure.md`, `docs/zh/production/团队Agent基础设施.md` |
| Tutorial reference map | Done | `docs/en/tutorials/reference-map.md`, `docs/zh/tutorials/教程参考地图.md` |
| Chinese tutorial filenames | Done | Chinese names under `docs/zh/` |
| Interview assets | Done | `docs/en/interviews/interview-framework.md`, `docs/en/interviews/questions/`, `docs/en/interviews/interview-answer-framework.md` |
| Portfolio tracks | Done | `docs/en/portfolio/projects.md`, `docs/en/portfolio/personal-agent-portfolio.md`, `docs/en/portfolio/open-source-impact-guide.md` |
| Production guides | Done | `docs/en/production/`, `docs/en/production/cost-stability-operations.md`, `docs/en/production/evals-playbook.md`, `docs/en/production/observability-trace-contract.md`, `docs/en/quick-reference/production-checklist.md`, and `examples/observability-trace/`, `examples/model-gateway/`, `examples/safety-eval/`, `examples/mcp-tool-boundary/`, `examples/memory-index-evidence/`, `examples/release-gate-evidence/`, including runtime, gateway, safety, tool-boundary, index, and release-gate evidence |
| Case studies | Done | `docs/en/cases/` and `docs/zh/cases/`, including enterprise tool, collaboration, RAG, regression, and pattern-contribution cases |
| Quick references | Done | `docs/en/quick-reference/`, including Chinese index |
| Agent skills | Done | `docs/en/skills/README.md`, `docs/zh/skills/Agent技能指南.md`, `templates/agent-skill-card-template.md` |
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
| Lab test coverage | 41 deterministic Lab tests pass locally |

## Recent Improvements

| Area | Status | Evidence |
| --- | --- | --- |
| README directory tree | Done | Streamlined tree in `README.md` and `README.zh-CN.md` |
| Lab level entry READMEs | Done | `labs/README.md` and `labs/l0/README.md` through `labs/l5/README.md` |
| Docs index cross-references | Done | `docs/en/README.md` and `docs/zh/README.md` now link Labs and Examples indexes |
| CI link-and-artifact-integrity job | Done | `link-and-artifact-integrity` job in `.github/workflows/ci.yml` |
| Repository checks | Done | `check_docs_topic_dirs`, `check_lab_level_readmes`, `check_example_dirs_readmes`, and `check_readme_mentions_lab_levels` in `scripts/check_repository.py` |
| Contribution Quality Gates | Done | `Quality Gates` section in `CONTRIBUTING.md` and `CONTRIBUTING.zh-CN.md` |
| Docs site Labs entry | Done | Labs navigation entries in `docs-site/index.html` |

## Next Priority

Continue improving coverage with more real-world examples, maintain bilingual SLA, and keep framework examples fresh through `sync-required` when APIs change.

## Completion Notes

The repository now includes the core learning framework, runnable Labs, bilingual L0-L5 tutorials, interview question banks, interview answer examples, portfolio tracks, open-source impact guidance, production guides, reusable design templates, community operations, governance, and CI checks.

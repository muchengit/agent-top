---
title: Project Dispatch Plan Template
validated_date: 2026-09-17
---

# Project Dispatch Plan

Use this when the main agent dispatches work to employees.

## Objective

- Project goal:
- Desired outcome:
- Target branch: `main`
- Date:

## Employees Assigned

| Employee ID | Employee | Lane | Objective | Expected output | Acceptance criteria | Required checks | Rework rule | Backup |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Research Discoverer | Research | Find a source that changes roadmap or content gaps | Source digest | Mapped to roadmap, dated, credible | Link check | No source-to-gap mapping | Community Operations Lead |
| 2 | Python Engineer | Multilingual Labs | Keep Python Lab deterministic and API-key-free | Python source + tests | Unit test passes | unittest | No deterministic tests | Language Parity Reviewer |
| 3 | Node.js/TypeScript Engineer | Multilingual Labs | Keep JS/TS behavior aligned with Python reference | JS runnable + TS source | Smoke/typecheck note | node smoke | Diverges from Python behavior | Language Parity Reviewer |
| 4 | Rust Engineer | Multilingual Labs | Keep Rust example compilable and pattern-aligned | Rust source + compile evidence | Compile passes | rustc smoke | Does not compile | Language Parity Reviewer |
| 5 | Go Engineer | Multilingual Labs | Keep Go module tested and runnable | go.mod + source + test | go test passes | go test | Missing module/tests | Language Parity Reviewer |
| 6 | Language Parity Reviewer | Multilingual Labs | Compare behavior across all languages | Parity matrix | No hidden behavior drift | manual + smoke | Missing language evidence | Rust/Go Engineer |
| 7 | Docs Structure Auditor | Docs | Keep docs link-safe and bilingual | Link/frontmatter report | Repo checks pass | check_repository | Broken links/metadata | Translation Editor |
| 8 | Translation Editor | Translation | Keep Chinese complete and synchronized | Chinese docs + metadata | Bilingual pair valid | check_repository | Stale or empty Chinese content | Docs Structure Auditor |
| 9 | Interview Coach | Interview | Expand L0-L5 interview coverage | Questions + rubric | Reviewable rubric | manual review | Memorization-only questions | Interview Candidate |
| 10 | Interview Candidate | Interview | Pressure-test interview answers | STAR answer + self critique | Explains trade-offs | manual review | Generic answer without evidence | Interview Coach |
| 11 | Open Source Contributor | Open source | Produce safe external contribution plan | Plan + checklist | Reviewable without private context | manual review | Too broad/private-dependent | Community Operations Lead |
| 12 | Eval and Observability Engineer | Production quality | Add replayable eval/trace evidence | Eval set + trace schema | Replayable evidence | manual review | Subjective metrics only | Safety Engineer |
| 13 | Safety and Guardrail Engineer | Safety | Guard destructive and permission-unclear actions | Guardrail checklist | Rollback/confirm present | manual review | Safety after execution | Cost and Reliability Engineer |
| 14 | Cost and Reliability Engineer | Production quality | Make examples cost/latency aware | Cost table + retry/rollback | No runaway retries | manual review | Ignores cost or reliability | Safety Engineer |
| 15 | Community Operations Lead | Community | Keep newcomer flow healthy | Issue/backlog/showcase notes | Sustainable scope | manual review | Burnout or stale backlog | Docs Structure Auditor |

## Quality Gates

- [ ] `python scripts/check_repository.py`
- [ ] `python -m unittest discover -s labs -p "test_*.py"`
- [ ] `python -m compileall -q labs scripts`
- [ ] `python -m ruff check .`
- [ ] `python scripts/smoke_multilingual_labs.py` when Labs change
- [ ] Bilingual metadata and Chinese filename conventions checked when docs change

## Merge Decision

- Main agent decision: approve | request changes | reject
- Reason:
- Remaining risk:
- Follow-up owner:

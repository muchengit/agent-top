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

| Employee | Task | Output files | Acceptance criteria | Backup |
| --- | --- | --- | --- | --- |
| Research Discoverer |  |  |  |  |
| Python Engineer |  |  |  |  |
| Node.js/TypeScript Engineer |  |  |  |  |
| Rust Engineer |  |  |  |  |
| Go Engineer |  |  |  |  |
| Language Parity Reviewer |  |  |  |  |
| Docs Structure Auditor |  |  |  |  |
| Translation Editor |  |  |  |  |
| Interview Coach |  |  |  |  |
| Interview Candidate |  |  |  |  |
| Open Source Contributor |  |  |  |  |

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

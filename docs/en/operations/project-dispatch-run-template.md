---
title: Project Dispatch Run Template
validated_date: 2026-09-17
i18n-key: operations-project-dispatch-run-template
last-synced: 2026-09-17
---

# YYYY-MM-DD Project Dispatch Run

Use this template after the main agent dispatches work to the employee roster.

## Main Agent Decision

Decision: accept | request changes | reject

Reason:

- Acceptance criteria met
- Quality gates checked
- No unresolved safety/release/community blocker
- Follow-up items assigned

## Dispatch Queue

| # | Employee | Lane | This-cycle output | Acceptance result |
| --- | --- | --- | --- | --- |
| 1 | Research Discoverer | Research |  |  |
| 2 | Python Engineer | Multilingual Labs |  |  |
| 3 | Node.js/TypeScript Engineer | Multilingual Labs |  |  |
| 4 | Rust Engineer | Multilingual Labs |  |  |
| 5 | Go Engineer | Multilingual Labs |  |  |
| 6 | Language Parity Reviewer | Multilingual Labs |  |  |
| 7 | Docs Structure Auditor | Docs |  |  |
| 8 | Translation Editor | Translation |  |  |
| 9 | Interview Coach | Interview |  |  |
| 10 | Interview Candidate | Interview |  |  |
| 11 | Open Source Contributor | Open source |  |  |
| 12 | Eval and Observability Engineer | Production quality |  |  |
| 13 | Safety and Guardrail Engineer | Safety |  |  |
| 14 | Cost and Reliability Engineer | Production quality |  |  |
| 15 | Community Operations Lead | Community |  |  |

## Evidence Checked

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p 'test_*.py'
python -m compileall -q labs scripts
python -m ruff check .
python scripts/smoke_multilingual_labs.py
python scripts/orchestrate_project.py --count 15 --output docs/en/operations/YYYY-MM-DD-project-dispatch-run.md
```

Observed results:

- Repository checks:
- Unit tests:
- Compileall:
- Ruff:
- Multilingual smoke:
- Language-specific notes:

## Follow-up Work

1. 
2. 
3. 

## Main Agent Review Notes

- What was accepted:
- What was rejected or narrowed:
- What should be deepened next cycle:

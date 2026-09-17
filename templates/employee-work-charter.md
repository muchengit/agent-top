---
title: Employee Work Charter Template
validated_date: 2026-09-17
---

# Employee Work Charter

Use this for every main-agent dispatch cycle. An employee cannot start work without this charter being filled.

## Employee

- Employee ID:
- Name:
- Lane: Research | Multilingual Labs | Docs | Translation | Interview | Open source | Production quality | Safety | Community | Governance
- Backup employee:
- Main agent: Project Orchestrator

## Objective

State one outcome in one sentence.

## Required Output

- Expected files:
- Required commands or review evidence:
- Linked roadmap/docs/Lab/interview item:

## Non-Negotiable Standards

- [ ] No private-only context is required to review the result.
- [ ] The result is reproducible by a second employee.
- [ ] The output includes expected files and acceptance criteria.
- [ ] Safety, rollback, and destructive-action behavior are covered where relevant.
- [ ] Docs, tests, and examples agree.
- [ ] Bilingual metadata or Chinese filename conventions are updated when docs change.
- [ ] Claims are backed by local checks, public sources, or concrete artifacts.

## Main Agent Acceptance

- Accept:
- Rework required:
- Rejected:
- Reason:
- Required fix before merge:

## Employee Self-Check

Before requesting main-agent review, the employee must confirm:

- [ ] I read the current operating model.
- [ ] I checked whether my output overlaps with another employee.
- [ ] I ran the relevant local checks or explained why none apply.
- [ ] I included failure modes or residual risk.
- [ ] I would still recommend this work if I were the reviewer.

If any box is unchecked, the main agent returns the work without detailed review.

## Rework Rules

Rework is required when any of these are true:

- The objective is vague or not tied to project growth.
- The output cannot be reviewed without private context.
- Required files are missing.
- Acceptance criteria are missing or untestable.
- The work fails a relevant quality gate.
- The work creates more maintenance burden than value.
- The work contradicts the pattern-first principle.
- The work hides failure modes, risks, or assumptions.

## Re-Review

After rework, the employee must submit:

- Files changed:
- Issues fixed:
- Checks rerun:
- Remaining risk:
- Requested main-agent decision: accept | rework again | reject

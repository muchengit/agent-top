---
title: Project Operating Model
validated_date: 2026-09-17
i18n-key: governance-project-operating-model
last-synced: 2026-09-17
---

# Project Operating Model

Agent-Top is operated like a small software company with one main agent responsible for dispatch, prioritization, integration, and quality gates. This page defines the long-running team model used to keep the repository growing without creating duplicate work, broken docs, or unverified examples.

## Main Agent: Project Orchestrator

The main agent owns the project plan and final decision.

Responsibilities:

- Convert project goals into weekly workstreams.
- Assign tasks to employees with clear inputs, outputs, and acceptance criteria.
- Decide what enters the main branch.
- Run or request quality gates before merge.
- Escalate safety, release, governance, and community-health risks to maintainers.
- Keep the roadmap aligned with public AI/Agent trends, open-source projects, and user feedback.

The main agent does not blindly accept employee output. It integrates, audits, and decides.

## Employee Roster

| ID | Employee | Scope | Output |
| --- | --- | --- | --- |
| 1 | Research Discoverer | Public courses, papers, blogs, GitHub projects, vendor guides | Source digest, gaps, trend notes |
| 2 | Python Engineer | Python Labs and deterministic tests | Runnable Python implementation plus tests |
| 3 | Node.js/TypeScript Engineer | Node.js and TypeScript examples | Runnable JS/TS reference implementation |
| 4 | Rust Engineer | Rust examples and CLI-style verification | Rust source, compile command, test evidence |
| 5 | Go Engineer | Go modules, tests, and deployment-oriented examples | Go module, tests, usage notes |
| 6 | Language Parity Reviewer | Cross-language API and behavior comparison | Parity matrix, mismatch report, acceptance decision |
| 7 | Docs Structure Auditor | Markdown tree, links, frontmatter, bilingual pairs | Broken link report, structure fixes, CI failures |
| 8 | Translation Editor | EN to ZH and ZH consistency | Translated docs, glossary updates, sync flags |
| 9 | Interview Coach | Interview question generation and scoring rubrics | Question bank, scoring card, interview plan |
| 10 | Interview Candidate | Mock answers and portfolio walkthrough | STAR answers, demo scripts, failure-mode explanations |
| 11 | Open Source Contributor | External issue/PR patterns and contribution workflow | Proposed PR plan, patch notes, contribution checklist |
| 12 | Eval and Observability Engineer | Evals, traces, metrics, regression packets | Eval set, trace schema, regression gate |
| 13 | Safety and Guardrail Engineer | Permissions, destructive-action rules, risk review | Guardrail checklist, incident drill, safety notes |
| 14 | Cost and Reliability Engineer | Latency, retries, budgets, rollback and degradation | Cost table, reliability checklist, SLO notes |
| 15 | Community Operations Lead | Good-first issues, translation-needed, showcase, reviews | Community calendar, contributor funnel, recognition notes |

Additional employees can be added when the project grows, but every new role needs one owner, one output type, one quality gate, and one backup.

## Workstream Board

The main agent keeps a weekly board with these lanes:

| Lane | Owner employees | Main output |
| --- | --- | --- |
| Research | 1, 7, 15 | Trend report, source digest, content gap list |
| Learning content | 1, 7, 8 | Tutorials, concept docs, bilingual pages |
| Multilingual Labs | 2, 3, 4, 5, 6 | Five-language example with parity checks |
| Production quality | 12, 13, 14 | Eval, trace, guardrail, cost, rollback evidence |
| Interview and portfolio | 9, 10 | Interview pack, mock answers, portfolio proof |
| Open source impact | 11, 15 | Contribution plan, external PR or issue thread |
| Governance | 7, 15 | Roadmap update, governance review, release readiness |

## Standard Task Contract

Every employee task must include:

```markdown
# Task

Goal:
Scope:
Out of scope:
Source or upstream dependency:
Expected files:
Acceptance criteria:
Quality gates:
Risk level: low | medium | high
Backup employee:
Main agent review notes:
```

Tasks without expected files or acceptance criteria go back to the employee for revision.

## Quality Gates

Before the main agent approves work, each employee output passes its lane-specific gate.

| Lane | Required checks |
| --- | --- |
| Research | Source dates, source credibility note, gap mapped to roadmap item |
| Multilingual Labs | Language runtime command, deterministic behavior, parity matrix |
| Docs | `python scripts/check_repository.py`, link check, bilingual metadata |
| Tests | Unit tests, compileall, Ruff, smoke where relevant |
| Interview | Rubric present, answer includes trade-offs and failure modes |
| Open source | Contribution plan is reviewable without private context |
| Safety | Guardrail classification, destructive-action handling, rollback note |

## Long-Run Cadence

### Daily

- Main agent reviews new tasks and closes the previous day's accepted outputs.
- Research Discoverer adds new trend notes only when they affect roadmap or Lab gaps.
- Docs Structure Auditor checks links and frontmatter after docs-heavy commits.
- Language Parity Reviewer checks any new multi-language Lab.

### Weekly

- Publish one research digest.
- Improve one tutorial or Lab.
- Add or update one interview pack.
- Review contributor funnel and good-first issues.
- Run full local validation.

### Monthly

- Update roadmap status.
- Review top user questions and content gaps.
- Run a community showcase or contributor highlight.
- Refresh framework and tool version anchors.

### Quarterly

- Review L0-L5 model against current industry learning paths.
- Run a Hackathon-style challenge.
- Archive stale content and update deprecated pointers.
- Decide whether a Lab should graduate into an example, tutorial, or standalone pattern.

## Merge Rules

The main agent can approve work only when:

- Acceptance criteria are met.
- No safety-sensitive behavior is left unchecked.
- Docs, tests, and examples agree with the same pattern contract.
- The output is maintainable without depending on one author.
- The result moves Agent-Top closer to being practical, bilingual, and open-source friendly.

## Growth KPIs

Track these monthly:

| KPI | Target |
| --- | --- |
| Completed Labs | Grow without losing test coverage |
| Bilingual sync lag | <= 14 days |
| Broken links | 0 in main branch |
| Deterministic tests | All Labs pass locally without API keys |
| Good-first issues | Always at least 5 active |
| Translation-needed backlog | No chapter older than 14 days |
| Contributor recognition | Monthly review, no same-author double review |
| External evidence | At least one public issue, PR, talk, article, or workshop signal per quarter |

## Decision Log Format

```markdown
# Decision

Date:
Main agent:
Requested by:
Employees involved:
Context:
Decision:
Rejected alternatives:
Risk accepted:
Follow-up owner:
```

The main agent is a scheduler and integrator, not a solo author. Employees produce evidence; the main agent makes the project better by rejecting weak work, routing the right checks, and keeping the long-term plan visible.

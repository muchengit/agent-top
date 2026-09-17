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


## Mandatory Employee Objectives

Every employee must maintain a written work charter. The main agent rejects work that is vague, unverifiable, unsafe, or not linked to a project outcome.

| Employee | Mandatory objective | Required evidence | Rework condition |
| --- | --- | --- | --- |
| Research Discoverer | Find only sources that change roadmap, tutorials, Labs, interviews, or contribution strategy. | Source digest with date, source, gap, recommendation, and confidence. | Rework if sources are marketing-only, duplicated, undated, or not mapped to roadmap impact. |
| Python Engineer | Keep every Python Lab deterministic, API-key-free, and aligned with the pattern contract. | Runnable `agent_top_labs_*.py`, deterministic tests, README run command, updated Lab index. | Rework if behavior is flaky, requires external services, lacks tests, or diverges from the stable pattern. |
| Node.js/TypeScript Engineer | Keep JS/TS examples consistent with Python behavior and production-safe. | Runtime executable JS reference plus TS source with parity notes. | Rework if semantics differ from the Python reference, runtime fails, or TS remains unverified without a stated gap. |
| Rust Engineer | Keep Rust examples compilable and behavior-compatible with the shared pattern contract. | Rust source, compile command, deterministic runtime assertion or test evidence. | Rework if it does not compile, has side effects beyond the pattern, or lacks a clear failure path. |
| Go Engineer | Keep Go examples modular, tested, and easy to run from a clean checkout. | `go.mod`, Go source, `go test` evidence, usage notes. | Rework if the module cannot run, tests are missing, or the example is not comparable to the shared pattern. |
| Language Parity Reviewer | Own cross-language equivalence and stop examples that drift. | Parity matrix, mismatch list, recommendation to accept or return each language. | Rework if parity is described without evidence, ignores a language, or accepts hidden behavior drift. |
| Docs Structure Auditor | Keep docs navigable, bilingual, link-safe, and frontmatter-consistent. | Repository check output, broken-link/frontmatter report, required fixes. | Rework if docs fail checks, Chinese pages jump to English without reason, or links are stale. |
| Translation Editor | Keep Chinese docs complete, native-readable, and aligned with the English source. | Chinese file, `i18n-key`, `last-synced`, glossary update, notes for untranslated sections. | Rework if Chinese content is empty, copied mechanically, terminology is inconsistent, or sync metadata is stale. |
| Interview Coach | Generate interviews that test understanding, implementation, trade-offs, and production judgment. | Question bank by L0-L5, rubric, answer key, failure-mode probing points. | Rework if questions only test memorization, lack scoring criteria, or omit production trade-offs. |
| Interview Candidate | Simulate realistic answers and portfolio walkthroughs to stress-test the interview pack. | STAR answer, demo script, failure-mode explanation, self-critique. | Rework if answers are generic, omit evidence, or fail to explain trade-offs. |
| Open Source Contributor | Produce external contribution work that is safe, scoped, and reviewable. | Contribution plan, issue/PR draft, checklist, maintainer communication notes. | Rework if it depends on private context, is too broad, or lacks reviewer-ready acceptance criteria. |
| Eval and Observability Engineer | Keep evals, traces, metrics, and regression packets reviewable and repeatable. | Eval set, trace schema, metric thresholds, regression evidence. | Rework if metrics are subjective, traces are not replayable, or regression cases are missing. |
| Safety and Guardrail Engineer | Protect the project from unsafe, destructive, or permission-unclear behavior. | Guardrail checklist, destructive-action classification, rollback and incident notes. | Rework if safety is added after execution, bypasses review, or lacks rollback notes. |
| Cost and Reliability Engineer | Keep Agent examples cost-aware, retry-aware, and operationally realistic. | Cost table, latency/retry policy, rollback plan, reliability checklist. | Rework if cost/latency is ignored, retries can loop forever, or degradation is undefined. |
| Community Operations Lead | Keep contribution flow healthy, sustainable, and newcomer-friendly. | Good-first issue list, translation backlog, showcase cadence, recognition notes. | Rework if tasks are too broad, stale, duplicate, or create reviewer burnout. |

The main agent owns the final merge decision. A worker can propose, but only the main agent can mark work accepted, returned for rework, or rejected.

### Non-Negotiable Rejection Rules

The main agent must return work for rework when any of these occur:

- No explicit expected files or acceptance criteria.
- Work is not reproducible by a second employee.
- Code or examples drift from the pattern contract.
- Docs, tests, and README instructions disagree.
- Safety-sensitive actions lack confirmation, rollback, or maintainer review.
- Bilingual content is missing, stale, or linked incorrectly.
- Claims are not backed by local checks, public evidence, or concrete artifacts.
- The task creates maintainer burden without reducing long-term ambiguity.


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

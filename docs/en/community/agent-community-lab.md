---
title: Agent Community Lab
validated_date: 2026-09-16
i18n-key: community-agent-community-lab
last-synced: 2026-09-18
---

# Agent Community Lab

Agent Community Lab is a lightweight group learning format for Agent-Top. It turns one tutorial, Lab, or architecture topic into a shared session with clear outputs.

## Format

A session should answer one question:

> What can participants build, explain, or improve by the end of this session?

Recommended duration:

- 60 to 90 minutes.
- One host.
- One topic.
- One runnable Lab or short docs review.

## Recommended Cadence

- Biweekly tutorial release sessions.
- Monthly interview practice sessions.
- Biweekly paper or article discussion sessions.
- Quarterly roadmap or production retrospectives.

These sessions complement the main content tree but should not replace it.

## Session Roles

| Role | Responsibility |
| --- | --- |
| Host | Runs the agenda, keeps time, captures decisions. |
| Contributor | Proposes one small change, translation, Lab, or answer. |
| Reviewer | Checks accuracy and maintainability. |
| Observer | Watches for blockers and follow-up issues. |

## Session Types

### Tutorial Walkthrough

Use when the topic is a new tutorial or Lab.

Outcome:

- Participants can run the Lab.
- The host identifies one common confusion.
- The team decides whether the docs need a follow-up patch.

### Interview Practice

Use when the topic is interview readiness.

Outcome:

- One question is discussed with STAR and trade-off notes.
- One follow-up question is added or improved.
- The session points back to the relevant capability level.

### Paper or Article Digest

Use when the topic is an external article, paper, or tutorial.

Outcome:

- Extract stable concepts.
- Separate stable concepts from framework-specific details.
- Add a comparison note only if it helps the repo.

### Production Retrospective

Use when the topic is postmortem, evals, observability, or rollback.

Outcome:

- A failure mode is made explicit.
- A prevention control is identified.
- A checklist or template update is proposed.

## Contribution Rules

- Use `docs-only` for documentation-only patches.
- Use `lab` for runnable Lab changes.
- Use `translation-needed` or `sync-required` for bilingual gaps.
- Avoid asking the same person to be author and reviewer in the same session unless the contribution is very small.

## Session Notes Output

At the end, publish a short note with:

- Topic.
- One-page summary.
- Runnable command or related Lab.
- Follow-up issue or PR.
- Whether the docs need updating.

Use the template:

- [`../../templates/community-lab-template.md`](../../../templates/community-lab-template.md)

## Health Checks

A good Agent Community Lab session should:

- Keep scope small.
- Produce one concrete artifact.
- Stay pattern-first.
- Avoid framework churn unless the pattern is stable.
- Leave the next contributor with a clear task.

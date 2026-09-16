# Agent-Top Governance

Agent-Top is maintained as an open, pattern-first learning framework.

## Roles

- Contributor: writes, translates, reviews, or maintains content.
- Reviewer: reviews ordinary Labs, docs, glossary entries, and interview questions.
- Maintainer: reviews architecture, safety, release process, and repository policy.
- Core: owns roadmap priorities and long-term framework decisions.

## Decision Principles

- Pattern first, framework second.
- Stable concepts before vendor-specific APIs.
- Executable Labs before prose-only examples.
- Version anchors and freshness checks before accepting framework examples.
- Community contribution paths before adding heavy maintenance work.

## Review Policy

- Architecture, safety, and deployment docs require Maintainer review.
- Ordinary Labs require Reviewer review.
- Translations require language review plus content-source consistency check.
- Same person should not be author and reviewer for the same module in the same month.

## Freshness Policy

Framework-sensitive examples must include:

- `validated_date`
- `tested_against`

Stale examples should receive `sync-required` or `deprecated` status through CI or reviewer action.

## Contribution Balance

Each active module should have at least two maintainers or backups to reduce bus factor and burnout.

## Communication

- Issues: concrete bugs, tasks, and feature requests.
- Discussions: learning questions, roadmap feedback, and community questions.
- PRs: documentation, Labs, review fixes, and maintenance updates.

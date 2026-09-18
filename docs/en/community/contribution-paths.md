---
title: Contribution Paths
validated_date: 2026-09-16
i18n-key: community-contribution-paths
last-synced: 2026-09-18
---

# Contribution Paths

Agent-Top has four main contribution paths.

## 1. Writing

Write new tutorials, concepts, or Labs.

Good writing contribution:

- Has a clear goal.
- Links to relevant labs or templates.
- Includes expected outputs.
- Explains trade-offs.
- Passes repository checks.

## 2. Translation

Translate English source content into Chinese.

Translation contribution:

- Uses the same `i18n-key`.
- Updates `last-synced`.
- Keeps technical terms consistent with the glossary.
- Leaves `translation-needed` closed only after review.

## 3. Review

Review content for correctness, clarity, and maintainability.

Review contribution should check:

- Accuracy.
- Broken links.
- Version anchors.
- Bilingual sync.
- Lab runnability.
- Trade-off explanations.

## 4. Maintenance

Maintain framework maps, CI, templates, and release hygiene.

## 5. L5 Expert Evidence

Submit evidence packages for L5 contributions: original patterns, architecture review, eval/trace/risk/release evidence, external influence artifacts, and mentoring/review proof. Use [`good-first-L5-candidates.md`](good-first-L5-candidates.md) for candidate L5 packages when preparing an issue or PR.

Good L5 evidence contribution:

- Package pattern, governance, and influence claims with the [`L5 expert evidence template`](../../../templates/l5-expert-evidence-template.md).
- Split claims into artifacts reviewers can check: a Lab, eval, trace, risk packet, design review, or issue/PR thread.
- Include failure modes, non-goals, rejected alternatives, and a residual-risk note.
- Mark the labels needed: `good-first-L5`, `original-pattern`, `external-impact`, `eval-evidence`, `safety-review`, `release-governance`, or `sig-candidate`.
- Include one mentoring or review signal proving the contributor raises the quality of other contributors.
- Start original patterns with a one-sentence spec (goal, interface, acceptance) from the [Vibe Coding workflow](../vibe-coding/README.md).

Maintenance contribution:

- Keeps CI green.
- Handles stale or breaking-change content.
- Rotates reviewers.
- Prevents documentation sprawl.

## Non-Python Lab Maintenance

Python remains the default runnable Lab language, but Node.js, Rust, Go, and TypeScript examples need explicit ownership when they are added.

Each non-Python Lab maintainer should:

- Keep the shared pattern contract unchanged.
- Update language-specific commands and version anchors.
- Run the relevant smoke path before requesting review.
- Document intentional parity differences.
- Route CI failures to the owning language lane, not to the docs reviewer.

Acceptance evidence:

- Node.js: runnable command and expected stdout.
- TypeScript: `npm ci` plus local TypeScript compile or smoke output.
- Rust: compile/test command and failure behavior.
- Go: module path, `go test`, and clean-checkout command.
- Parity reviewer: mismatch table with accept/rework decision.

## Labels

Start with:

- `good first issue`
- `docs-only`
- `translation-needed`
- `sync-required`
- `lab`
- `good-first-L5`
- `original-pattern`
- `external-impact`

## Community Lab Sessions

Community Lab sessions are a contribution path when they produce docs, Labs, translations, review notes, or follow-up issues. Use `docs-only` for writing-only patches and `lab` for runnable examples.

## Review Policy

Same person should not be author and both reviewers in the same month. Core contributors can use Contributor of the Month review exemption when workload allows.

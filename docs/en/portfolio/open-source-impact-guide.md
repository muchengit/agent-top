---
title: Open-Source Impact Guide
validated_date: 2026-09-17
i18n-key: portfolio-open-source-impact
last-synced: 2026-09-17
---

# Open-Source Impact Guide

Open-source impact is a way to prove L5-level Agent ability: define reusable patterns, improve tooling, and create evidence others can inspect. This guide is written for contributors who want to convert daily Agent work into maintainer-facing artifacts: stable patterns, deterministic Labs, evaluation improvements, observability contracts, documentation, and tooling.

## Audience and Purpose

- **Primary audience**: L4→L5 learners who need external, reviewable evidence of original patterns, plus maintainers who review those contributions.
- **Purpose**: show what a high-quality contribution package contains, how to prepare it, how to gather external evidence, and how to measure impact so reviewers can verify rather than trust.
- **Not for**: beginners who have not yet shipped a working single Agent. Complete [`learning-paths.md`](../tutorials/learning-paths.md) first.

## Contribution Types

- **Pattern contribution** — document a stable Agent pattern with tests or examples.
- **Lab contribution** — add a deterministic exercise that teaches a design trade-off.
- **Evaluation contribution** — improve eval design, negative cases, or release gates.
- **Observability contribution** — add trace contracts, alert examples, or debugging workflows.
- **Documentation contribution** — clarify concepts, mappings, glossary, or contributor paths.
- **Tooling contribution** — improve CI, docs checks, templates, or local validation.

## Good Contribution Package

A contribution should include:

- Problem statement.
- Stable pattern or workflow.
- Minimal reproducible example.
- Tests or validation commands.
- Failure modes.
- Maintainer notes.
- Bilingual documentation when the repository is bilingual.
- Links to related concepts and Labs.

## Step-by-Step Workflow

1. **Pick one gap.** Search issues, the contribution paths, and the pattern matrix before starting.
2. **Write the problem statement.** Name the user, the task, and the failure you observed in one paragraph.
3. **Prototype locally.** Use a minimal reproducible example and record the commands that reproduce the behavior.
4. **Stabilize the pattern.** Separate the stable idea from framework-specific glue, and document what breaks first.
5. **Add deterministic evidence.** Add tests, eval cases, or a Lab so the claim can be re-run.
6. **Open a small PR.** Keep the diff reviewable, run repository checks, and add a reviewer-friendly description.
7. **Collect external evidence.** Link the accepted PR, maintainer comments, and any follow-up use.

## Choosing Your First Contribution

- **Start where you failed.** The most convincing contribution comes from a bug or trade-off you hit in your own project.
- **Prefer a Lab over an essay.** A deterministic exercise teaches a trade-off better than prose.
- **Match repository conventions.** Read the contribution paths and existing Labs before writing a new one.
- **Keep the first PR small.** One pattern, one Lab, or one eval improvement is enough to start.
- **Ask for the gap list.** Maintainer issues often mark [`good-first-L5`](../../../docs/en/community/labels.md) candidates for external impact.

## Contribution Readiness

Before opening a PR:

- Run repository checks.
- Confirm the pattern is not just a framework API wrapper.
- Separate stable concepts from framework-specific code.
- Include negative examples or non-usage cases.
- Explain what happens when the pattern fails.
- For AI-assisted drafting, write a one-sentence spec (goal, interface, acceptance) first via the [Vibe Coding workflow](../vibe-coding/README.md).

## External Evidence

Useful external artifacts:

- Accepted PR.
- Maintainer comment explaining design trade-off.
- Talk or workshop notes.
- Article explaining a pattern with examples.
- Maintained Lab used by learners.
- Issue thread showing adoption or follow-up use.

## Impact Statement Template

```markdown
# Contribution Impact

## Problem
What gap did this contribution close?

## Pattern
What reusable idea is introduced?

## Evidence
What tests, examples, or reviews prove it works?

## Adoption
Who could use this next?

## Follow-Up
What is not covered yet?
```

## Example PR Description

```markdown
## Problem
Tool results were accepted without provenance, so stale data silently propagated.

## Pattern
A provenance-check gate: every tool result is tagged with source, timestamp, and
fetch status before the planner sees it.

## Evidence
- 2 negative eval cases that fail before the gate and pass after it.
- 1 deterministic Lab runnable with `python ../../../labs/l3/rag_evaluator`.
- Repository checks pass with `python scripts/check_repository.py`.

## Notes for Reviewer
The failure mode to check: what happens when the provenance source itself is
unavailable. The pattern keeps the planner unchanged and only guards the data layer.
```

## Common Mistakes and How to Avoid Them

- **Skipping the problem statement** — reviewers cannot evaluate intent. Always start with the gap.
- **Wrapping a framework API** — a thin wrapper is not an original pattern. Show the design decision and the failure mode you prevented.
- **Mixing stable and version-specific code** — put framework-dependent parts in a separate layer so the pattern survives upgrades.
- **Only positive examples** — include negative cases or non-usage cases so the boundary of the pattern is visible.
- **Silent failure** — describe what happens when the pattern fails and how to detect it.
- **Ignoring repository checks** — run `python scripts/check_repository.py` before opening the PR.

## Measurable Indicators

- **Adoption**: issue threads, downstream Labs, or learner usage that reference the contribution.
- **Reviewability**: accepted PR with maintainer comments that explain the trade-off.
- **Reproducibility**: a reviewer can re-run the tests or validation commands in one pass.
- **Reach**: talk notes, workshop notes, or articles that explain the pattern.
- **Retention**: the pattern survives a repository upgrade or a new contributor picks it up.

## Maintainer View

- **Maintainers verify, they do not trust.** Every claim in the PR description needs a re-runnable test or Lab.
- **Negative cases are the proof of judgment.** They show you know where the pattern stops working.
- **Small diffs get reviews.** Split large contributions into a series of PRs.
- **Bilingual sync is part of the definition of done.** The zh mirror must keep the same `i18n-key` and `last-synced` date.

## Realistic Example Snippet

```markdown
# Contribution Impact

## Problem
A single-agent deployment accepted tool results without provenance, so stale data
silently propagated. Users asked for a retry that hid the real failure.

## Pattern
A provenance-check gate: every tool result is tagged with source, timestamp, and
fetch status before the planner sees it.

## Evidence
- 2 negative eval cases that fail before the gate and pass after it.
- 1 deterministic Lab runnable with `python ../../../labs/l3/rag_evaluator`.
- Maintainer review: "The failure-mode section made the trade-off clear."

## Adoption
Any RAG or MCP-based Agent that merges results from multiple sources.

## Follow-Up
Behavior when the provenance source itself is unavailable.
```

## Next Actions Checklist

- [ ] Pick one contribution type and one gap from the contribution paths.
- [ ] Write a problem statement in one paragraph.
- [ ] Prototype with a minimal reproducible example.
- [ ] Separate the stable pattern from framework code.
- [ ] Add tests, eval cases, or a deterministic Lab.
- [ ] Run `python scripts/check_repository.py`.
- [ ] Open a small PR and collect external evidence.
- [ ] Fill the impact statement template and link it from your portfolio.

## Related Assets

- [`projects.md`](projects.md)
- [`personal-agent-portfolio.md`](personal-agent-portfolio.md)
- [`../l5-custom-patterns.md`](../l5-custom-patterns.md)
- [`../community/contribution-paths.md`](../community/contribution-paths.md)
- [`../community/labels.md`](../community/labels.md)
- [`../../../CONTRIBUTING.md`](../../../CONTRIBUTING.md)

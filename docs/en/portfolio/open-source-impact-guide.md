---
title: Open-Source Impact Guide
validated_date: 2026-09-16
i18n-key: portfolio-open-source-impact
last-synced: 2026-09-16
---

# Open-Source Impact Guide

Open-source impact is a way to prove L5-level Agent ability: define reusable patterns, improve tooling, and create evidence others can inspect.

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

## Contribution Readiness

Before opening a PR:

- Run repository checks.
- Confirm the pattern is not just a framework API wrapper.
- Separate stable concepts from framework-specific code.
- Include negative examples or non-usage cases.
- Explain what happens when the pattern fails.

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

## Related Assets

- [`projects.md`](projects.md)
- [`../l5-custom-patterns.md`](../l5-custom-patterns.md)
- [`../community/contribution-paths.md`](../community/contribution-paths.md)
- [`../../../CONTRIBUTING.md`](../../../CONTRIBUTING.md)

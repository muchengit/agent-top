---
title: Contributor Onboarding
validated_date: 2026-09-16
---

# Contributor Onboarding

Welcome. This guide helps you make a first contribution that maintainers can review quickly.

## First Steps

1. Read the README and documentation index.
2. Pick one label: `good first issue`, `docs-only`, or `translation-needed`.
3. Run the local checks before and after your change.
4. Keep the change small and reviewable.
5. Explain what you changed and why.

## Local Checks

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

## Before You Open a PR

- Are relative links valid?
- Is `validated_date` current when content changes?
- Is `tested_against` present for Labs or framework-sensitive content?
- Are bilingual files paired by `i18n-key`?
- Are claims tied to runnable examples where relevant?

## What Reviewers Look For

- Clear scope.
- Accurate language.
- Runnable examples.
- Stable concepts separated from framework APIs.
- No unnecessary rewrites.

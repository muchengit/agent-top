---
title: Run and Verify
validated_date: 2026-09-18
i18n-key: vibe-coding-run-verify
last-synced: 2026-09-18
---

# Run and Verify

## Rule

A vibe-coded change is not done until the repository's deterministic checks pass. In Agent-Top that means:

```bash
python3 scripts/check_repository.py
python3 -m unittest discover -s labs -p 'test_*.py'
python3 -m compileall -q labs scripts
python3 -m ruff check .
python3 scripts/smoke_examples.py
python3 scripts/smoke_multilingual_labs.py
```

## What "Verified" Means

- **Runnable**: the command exists and exits zero.
- **Deterministic**: the same input gives the same result without network or API keys.
- **Evidence**: tests, traces, or evals capture the behavior; a reviewer can re-run them.
- **Mirrored**: for Agent-Top docs, EN is the source and ZH keeps the same `i18n-key` with an updated `last-synced`.

## Feedback Loop

1. Run the narrowest check first (the test for the file you touched).
2. Then run the module-level suite.
3. Then run the repository-wide gate before opening a PR.

## Handling a Failing Check

- Read the first error, not the last summary.
- Reproduce with the exact failing input.
- Ask for the smallest fix; do not let the assistant rewrite unrelated code.
- Re-run the full gate, because a fix in one file can break another.

## Evidence for Reviewers

A vibe-coded contribution should include:

- What changed and why (one or two sentences).
- The acceptance command and its output.
- Any deliberate deviations from the spec.

This makes the PR reviewable without trusting the assistant.

# Contributing to Agent-Top

Thanks for helping improve Agent-Top. This repository prefers clear, small, reviewable contributions.

## Contribution Paths

- Writing tutorials or Labs
- Translating content
- Reviewing documentation
- Maintaining examples
- Adding interview questions
- Adding portfolio project tracks, interview answer examples, design templates, or open-source impact guides

Start with one of these labels:

- `good first issue`
- `docs-only`
- `translation-needed`
- `sync-required`

## Local Checks

Run the repository checker before opening a pull request:

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

## Documentation Standards

Every article or Lab should include:

- Goal
- Prerequisites with capability level
- Steps or Run command
- Expected outputs or verification
- Version anchors when code is framework-specific
- Common pitfalls
- Self-check questions

Use Markdown and executable Labs as the primary content format. For concrete Labs, keep code and tests in the same Lab directory and document the run command in the README.

## Bilingual Workflow

- English is the primary source unless explicitly marked otherwise.
- Chinese translations live under `docs/zh` and should keep the same `i18n-key`.
- Keep `last-synced` metadata updated when translation status changes.
- Use the glossary for stable terms.

## Review Rules

- One author should not also be the same-month content reviewer for the same module.
- Architecture and safety topics require Maintainer review.
- Ordinary Labs require Reviewer review.
- Translations require language review plus content-source consistency check.

## PR Description

Use [`templates/contribution-checklist.md`](templates/contribution-checklist.md) before opening a PR.

Include:

- What changed.
- Why it changed.
- Checks run.
- Any translation or framework version impact.
- Any follow-up needed.

# Contributing to Agent-Top

Thanks for helping improve Agent-Top. This repository prefers clear, small, reviewable contributions.

## Contribution Paths

- Writing tutorials or Labs
- Translating content
- Reviewing documentation
- Maintaining examples
- Adding interview questions
- Adding portfolio project tracks

## Good First Labels

- `good first issue`
- `docs-only`
- `translation-needed`

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
- Version anchors when code is framework-specific
- Common pitfalls
- Self-check questions

Use Markdown and executable Labs as the primary content format. For concrete Labs, keep code and tests in the same Lab directory and document the run command in the README.

## Bilingual Workflow

- English is the primary source unless explicitly marked otherwise.
- Chinese translations are tracked through `translation-needed`.
- Keep `last-synced` metadata updated when translation status changes.

## Review Rules

- One author should not also be the same-month content reviewer for the same module.
- Architecture and safety topics require Maintainer review.
- Ordinary Labs require Reviewer review.

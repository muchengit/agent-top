---
title: Contributor Onboarding
validated_date: 2026-09-17
i18n-key: community-contributor-onboarding
last-synced: 2026-09-17
---

# Contributor Onboarding

Welcome. This guide helps you make a first contribution that maintainers can review quickly. It assumes no prior maintainer experience, only a GitHub account and a local checkout.

## Goal

After finishing this guide you should be able to:

- Pick a first issue that fits your skills.
- Run the repository checks locally.
- Open a small PR with correct bilingual metadata.
- Understand what reviewers check and why.

## Before You Start

1. Read [`README.md`](../../../README.md) and the community index ([`README.md`](README.md)).
2. Read [`CONTRIBUTING.md`](../../../CONTRIBUTING.md) and [`CODE_OF_CONDUCT.md`](../../../CODE_OF_CONDUCT.md).
3. Fork the repository and clone it locally.
4. Install Python 3.10+ and make sure `python` runs the right interpreter.
5. Skim [`labels.md`](labels.md) so you understand the label system.

Estimated time for this setup: 30-45 minutes.

## First Steps

1. Pick one label: `good first issue`, `docs-only`, or `translation-needed`.
2. Comment on the issue saying you will take it, with a date.
3. Run the local checks before and after your change.
4. Keep the change small and reviewable: one issue, one PR.
5. Explain in the PR what you changed and why, with links to evidence.

Do not pick a `maintainer-review` issue as your first PR. Start with `docs-only` or a small translation.

## Label Guidance

| Label | First-PR friendly? | What you will touch |
| --- | --- | --- |
| `good first issue` | Yes | One file or one small Lab |
| `docs-only` | Yes | Markdown only, no behavior change |
| `translation-needed` | Yes | One Chinese mirror of an English page |
| `sync-required` | Maybe | Both EN and ZH pages, needs care |
| `maintainer-review` | No | Architecture, safety, production content |

## Local Checks

Run these from the repository root before opening the PR:

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

The first command is the community gate: broken links, stale `validated_date`, unpaired bilingual keys, and merge-conflict markers all fail it.

## PR Checklist

- [ ] Relative links are valid from the current file location.
- [ ] `validated_date` is updated to the current date when content changes.
- [ ] `tested_against` is present for Labs or framework-sensitive content.
- [ ] Bilingual files are paired by the same `i18n-key`.
- [ ] `last-synced` is updated when the mirrored content changes.
- [ ] Claims are tied to runnable examples where relevant.
- [ ] Glossary terms match [`glossary.md`](glossary.md).
- [ ] The PR title states the scope, e.g. `docs: fix broken link in onboarding`.

The template [`../../templates/contribution-checklist.md`](../../../templates/contribution-checklist.md) is the same list; fill it in and link it from the PR.

## Writing a Good First PR

- State the goal and the non-goals in the PR summary.
- Quote or link the issue you are closing.
- Show the before and after for docs changes.
- For translations, point to the English source file.
- If you changed an example, show the command output.

## What Reviewers Look For

- Clear scope: one issue, one file, one reason.
- Accurate language: terminology matches the glossary.
- Runnable examples: code that is tested, not pasted.
- Stable concepts separated from framework APIs.
- No unnecessary rewrites of working content.

## Getting Help

- Comment on your issue with `@maintainer` questions.
- Ask in the community issue tracker before guessing on scope.
- If you are blocked by a failing check, paste the exact command and output.
- For translation work, read [`translation-workflow.md`](translation-workflow.md) first.

## Common Issues and Handling

- **Check fails with broken link**: fix the relative path from your file's directory.
- **`i18n-key` mismatch**: copy the key from the paired English file exactly.
- **PR too large**: split it; ask the reviewer which part to keep first.
- **`validated_date` not updated**: touch it on every content change, not just new files.
- **Reviewer asks for changes**: reply within 3 days; use checklists to track comments.

## Measurable Metrics

For the community, track per quarter:

- Time from first comment to first merged PR (target: under 14 days).
- First-PR merge rate (target: above 80%).
- Number of new contributors who open a second PR (target: above 50%).
- Average number of review rounds on first PRs (target: under 3).

## FAQ

- **Do I need to be an expert in Agent frameworks?** No. Most first PRs are docs or translation.
- **Can I work on two issues at once?** Prefer one; a small PR is easier to review.
- **What if the issue is already claimed?** Comment and coordinate; do not open a duplicate PR.
- **Where do I find the issue list?** The repo issue tracker with the `good first issue` filter.

# Contribution Checklist

Use this before opening a PR.

## Scope

- [ ] Change is small and reviewable.
- [ ] Goal is stated in the PR summary.
- [ ] Non-goals are clear.
- [ ] Existing docs or Labs were checked for overlap.

## Documentation

- [ ] `validated_date` is current for touched Markdown.
- [ ] Relative links work from the current file location.
- [ ] Markdown is readable and consistent with `STYLE.md`.
- [ ] Framework-specific content is separated from stable concepts.
- [ ] Examples do not duplicate Lab source code.

## Bilingual Docs

- [ ] English and Chinese files use the same `i18n-key`.
- [ ] `last-synced` is updated for translated or mirrored content.
- [ ] Chinese docs under `docs/zh` use Chinese file names where existing.
- [ ] Glossary terms are consistent.

## Labs And Examples

- [ ] New Labs have code and deterministic tests.
- [ ] New Labs include Goal, Prerequisites, Run, Common Pitfalls, and Self-Check.
- [ ] Example JSONL files are valid.
- [ ] Example exercises do not require API keys or external services.
- [ ] Lab README lists expected output or verification.

## Safety And Production

- [ ] Tool actions are classified as read, write, or destructive.
- [ ] Destructive actions require confirmation or approval.
- [ ] Privacy-sensitive data is fictional or synthetic.
- [ ] Security-relevant topics include maintainer review.
- [ ] Rollback or failure handling is described when relevant.

## Verification

- [ ] `python scripts/check_repository.py`
- [ ] `python -m unittest discover -s labs -p "test_*.py"`
- [ ] `python -m compileall -q labs scripts`
- [ ] `python -m ruff check .`

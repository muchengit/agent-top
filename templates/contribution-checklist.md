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
- [ ] AI-assisted Lab or example drafts start from a one-sentence spec (goal, interface, acceptance) and pass the [`vibe_coding_spec` readiness check](../labs/l5/vibe_coding_spec/README.md).
- [ ] Example JSONL files are valid.
- [ ] Example exercises do not require API keys or external services.
- [ ] Lab README lists expected output or verification.

## Safety And Production

- [ ] Tool actions are classified as read, write, or destructive.
- [ ] Destructive actions require confirmation or approval.
- [ ] Privacy-sensitive data is fictional or synthetic.
- [ ] Security-relevant topics include maintainer review.
- [ ] Rollback or failure handling is described when relevant.

## L5 Expert Evidence

- [ ] If this PR claims L5 readiness, it includes or links an L5 expert evidence bundle.
- [ ] L5 claims distinguish pattern quality, governance quality, and external influence.
- [ ] L5 work includes failure modes, non-goals, rejected alternatives, and residual-risk notes.
- [ ] L5 work that touches safety, release, permissions, or governance is labeled for maintainer review.

## Verification

- [ ] `python scripts/check_repository.py`
- [ ] `python -m unittest discover -s labs -p "test_*.py"`
- [ ] `python -m compileall -q labs scripts`
- [ ] `python -m ruff check .`

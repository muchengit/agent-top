## Summary

What does this PR change?

## Type of Change

- [ ] Docs
- [ ] Lab
- [ ] Interview question
- [ ] Translation
- [ ] Maintenance
- [ ] Governance

## Docs Sync

- [ ] I kept en/zh mirrors in sync (same `i18n-key`) and updated `last-synced` when changing docs
- [ ] I marked framework/API changes with `sync-required` and `breaking-change` labels as appropriate

## Checklist

- [ ] I ran `python scripts/check_repository.py`
- [ ] I ran `python -m ruff check .`
- [ ] I ran `python -m unittest discover -s labs -p "test_*.py"` when changing Labs
- [ ] I updated version anchors when changing framework-sensitive content
- [ ] I wrote a one-sentence spec (goal, interface, acceptance) before prompting for new Labs or examples
- [ ] I avoided duplicating code between prose and Labs
- [ ] I added or updated eval evidence when changing Agent behavior
- [ ] I documented rollback behavior for production or safety changes
- [ ] I explained relevant trade-offs

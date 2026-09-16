---
title: Contributor Onboarding
validated_date: 2026-09-16
---

# Contributor Onboarding

Welcome. Agent-Top is built around durable Agent patterns, executable Labs, and clear community workflows.

## 30-Minute Start

1. Read `README.md` and `CONTRIBUTING.md`.
2. Pick one label: `good first issue`, `docs-only`, or `translation-needed`.
3. Read the relevant template in `templates/`.
4. Run local checks before opening a PR:

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
```

## Contribution Types

- Writing: tutorials, concepts, Labs, portfolio tracks.
- Translation: `docs/en/` to `docs/zh/` with matching `i18n-key`.
- Review: content, language, framework accuracy, or safety.
- Maintenance: links, freshness, labels, CI, templates.

## Review Expectations

- Keep examples executable.
- Keep framework-specific code in Labs.
- Add `validated_date` and version anchors where relevant.
- Call out trade-offs and failure modes.

## Where to Start Next

- Community labels: [`labels.md`](labels.md)
- Translation workflow: [`translation-workflow.md`](translation-workflow.md)
- Contribution paths: [`contribution-paths.md`](contribution-paths.md)

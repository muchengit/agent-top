# Agent-Top Style Guide

Agent-Top uses a pattern-first, bilingual, docs-and-Labs workflow. Keep changes small, reviewable, and runnable.

## Content Principles

- Teach stable patterns before framework APIs.
- Keep concepts in `docs/en` and mirror structure in `docs/zh`.
- Put framework-specific code in Labs.
- Prefer examples that run locally without API keys.
- Explain failure modes, not only happy paths.
- Prefer trade-off reasoning over slogans.

## Markdown Standards

- Use Markdown as the default content format.
- Use Mermaid or editable source for diagrams.
- Include expected outputs for tutorials and Labs.
- Use tables for comparisons and scoring rubrics.
- Keep headings parallel across English and Chinese mirrors.

## Frontmatter

Every bilingual docs file under `docs/en` and `docs/zh` should include:

```yaml
i18n-key: stable-key
last-synced: YYYY-MM-DD
validated_date: YYYY-MM-DD
```

Use `validated_date` for framework-sensitive or time-sensitive content. Use `tested_against` in Labs or framework examples.

## Links

- Prefer relative links that pass `python scripts/check_repository.py`.
- English docs may link to Labs directly.
- Chinese docs should prefer Chinese mirrors when they exist.
- Do not leave placeholder-only Chinese pages when English content is complete.

## Labs

Every Lab should include:

- Goal.
- Prerequisites.
- Run command.
- Common Pitfalls.
- Self-Check.
- Deterministic test coverage.

Labs should not require API keys or call real production systems.

## Glossary and Terminology

Prefer stable translations for core terms:

- Agent: Agent
- RAG: RAG
- MCP: MCP
- ReAct: ReAct
- Guardrail: guardrail / 护栏
- Rollback: rollback / 回滚
- Postmortem: postmortem

## Review Checklist

Before requesting review:

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

A good PR explains:

- What changed.
- Why it changed.
- Which checks were run.
- Whether bilingual sync is affected.
- Whether framework or Lab examples need `validated_date` or `tested_against`.

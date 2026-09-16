---
title: Architecture Patterns Quick Reference
validated_date: 2026-09-16
i18n-key: quick-reference-architecture-patterns
last-synced: 2026-09-16
---

# Architecture Patterns Quick Reference

| Pattern | Use When | Avoid When |
| --- | --- | --- |
| Single LLM call | Simple answer, no tools | Evidence or action is needed |
| ReAct loop | Tool use with observable steps | Tool results are untrusted |
| RAG Agent | Answer depends on private or current docs | Corpus is stale or untrustworthy |
| Tool-using Agent | External state or side effects are needed | Permissions are unclear |
| Multi-agent supervisor | Specialization and verification help | A single Agent with tools is enough |
| Production Agent | Auth, evals, traces, rollback are required | You only need a prototype |

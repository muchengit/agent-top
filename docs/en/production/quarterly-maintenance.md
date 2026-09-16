---
title: Quarterly Maintenance Guide
validated_date: 2026-09-16
i18n-key: production-quarterly-maintenance
last-synced: 2026-09-16
---

# Quarterly Maintenance Guide

Quarterly maintenance keeps Agent content fresh without turning documentation into a stale burden.

## Quarterly Review Steps

1. Check every `validated_date`.
2. Check `tested_against` anchors for Labs.
3. Run repository checks.
4. Run Lab tests.
5. Scan for dead links.
6. Scan for framework breaking changes.
7. Review translation sync.
8. Review deprecated content.
9. Check contributor workload.

## Content Health Metrics

- Completion rate by capability level.
- Translation sync rate within 14 days.
- Dead link rate below 1%.
- Stale Lab rate.
- Contributor burnout signals.
- Reader feedback NPS.

## Breaking Change Process

When a framework or SDK changes behavior:

1. Add `breaking-change` label.
2. Check whether the Lab still runs.
3. Update `validated_date` and `tested_against`.
4. If not updated within one quarter, mark `deprecated`.
5. Add replacement link if content was rewritten.

## Archive Policy

- Deprecated content stays for one quarter.
- Replace with pointer to the new tutorial.
- Preserve stable concepts even if framework examples change.
- Archive only after replacement is reviewed.

## Review Checklist

```markdown
# Quarterly Review

## Scope
- Repository version:
- Reviewed by:

## Results
- Stale docs:
- Broken links:
- Failed Labs:
- Translation drift:

## Actions
| Item | Owner | Due | Status |
| --- | --- | --- | --- |
```

---
title: Quarterly Maintenance Guide
validated_date: 2026-09-17
i18n-key: production-quarterly-maintenance
last-synced: 2026-09-17
---

# Quarterly Maintenance Guide

Quarterly maintenance keeps Agent content fresh without turning documentation into a stale burden. This guide is the operational contract for finding stale content, re-validating Labs, re-syncing translations, and keeping the docs index truthful. Use it at the start of each quarter and after any framework breaking change.

## Purpose And Scope

This guide applies to every bilingual document and executable Lab under `docs/en`, `docs/zh`, and `labs/`. It covers:

- Validating `validated_date` freshness across all Markdown files.
- Re-running Lab tests after dependency, framework, or Python changes.
- Checking translation sync between English and Chinese mirrors.
- Managing breaking changes and deprecations.
- Reporting health metrics to maintainers.

Out of scope: content authoring for brand-new tutorials and interview questions, which follow the contribution workflow instead.

## Quarterly Review Steps

Run the review in the order below so that each step's findings feed the next step.

1. **Refresh the working tree.** Pull the latest `main` and confirm the branch is clean:

   ```bash
   git pull --ff-only origin main
   git status --short
   ```

2. **Check every `validated_date`.** The repository script flags files older than 180 days:

   ```bash
   python scripts/check_repository.py
   ```

   Additionally, list every document with a date anchor so you can review the newest first:

   ```bash
   rg -l "validated_date:" docs | xargs -I{} sh -c 'echo "$(rg -o "validated_date: .*" "{}") {}"'
   ```

3. **Check `tested_against` anchors for Labs.** Every Lab README that pins a runtime or dependency version must state it explicitly:

   ```bash
   rg -n "tested_against:" labs docs
   ```

4. **Run repository checks.** This validates required paths, frontmatter, bilingual pairs, links, and conflicts in one pass:

   ```bash
   python scripts/check_repository.py
   ```

5. **Run Lab tests.** Execute the deterministic suite locally; no API keys are required:

   ```bash
   python -m unittest discover -s labs -p "test_*.py"
   ```

6. **Scan for dead links.** Relative links are checked by the repository script, but also scan the docs site:

   ```bash
   python scripts/check_repository.py
   rg -n "\]\(\.\.?/|\[.*\]\([a-z]" docs --glob "*.md" | head -50
   ```

7. **Scan for framework breaking changes.** Watch the upstream changelogs of the frameworks and SDKs referenced in `tested_against` anchors (for example, LangChain, LangGraph, or MCP SDK releases). When a change lands, follow the Breaking Change Process below.

8. **Review translation sync.** Confirm that every `i18n-key` in `docs/en` has an exact match in `docs/zh`:

   ```bash
   python - <<'PY'
   from pathlib import Path
   import re
   def keys(lang):
       out = set()
       for p in Path("docs", lang).rglob("*.md"):
           m = re.search(r"^i18n-key:\s*(.+)$", p.read_text(encoding="utf-8"), re.M)
           if m:
               out.add(m.group(1).strip())
       return out
   en, zh = keys("en"), keys("zh")
   print("missing in zh:", sorted(en - zh))
   print("extra in zh:", sorted(zh - en))
   print("pairs:", len(en & zh))
   PY
   ```

9. **Review deprecated content.** List all `deprecated` markers and confirm each one has an owner, an expiry, and a replacement link:

   ```bash
   rg -n -i "deprecated" docs labs
   ```

10. **Check contributor workload.** Review the open issue and PR labels for burnout signals (for example, a single maintainer owning more than three quarters of `maintainer-review` or `translation-needed` items), and rebalance ownership on the next planning call.

## Content Health Metrics

Track these metrics in the quarterly review report and compare against the previous quarter:

| Metric | Definition | Target | Where To Get It |
| --- | --- | --- | --- |
| Completion rate by level | Docs/Labs with a passing self-check or test, per L0-L5 | 100% for shipped content | `python -m unittest discover -s labs` |
| Translation sync rate | Mirrored docs whose `last-synced` is within 14 days | ≥ 95% | `rg "last-synced" docs/zh` |
| Dead link rate | Broken relative links / total relative links | < 1% | `check_repository.py` output |
| Stale Lab rate | Labs with `validated_date` older than 180 days | 0 | `check_version_anchors` in `check_repository.py` |
| Contributor burnout signals | Open PRs older than 30 days, unassigned `maintainer-review`, repeated reviewer swaps | 0 unresolved | GitHub labels + issue search |
| Reader feedback NPS | Survey responses on tutorial pages | ≥ 30 | docs-site feedback form |

## Breaking Change Process

When a framework or SDK changes behavior, follow this sequence to keep every anchor truthful:

1. **Add the `breaking-change` label** to the affected document and Lab issue.
2. **Check whether the Lab still runs.** Re-run the suite:

   ```bash
   python -m unittest labs.l4.regression_gate.test_lab
   ```

3. **Update `validated_date` and `tested_against`** to the verified runtime and date:

   ```yaml
   validated_date: 2026-09-17
   tested_against: langchain 0.3.x, openai 1.x, python 3.12
   ```

4. **If not updated within one quarter**, mark the content `deprecated` with a pointer to the replacement.
5. **Add a replacement link** when the content is rewritten, so readers never land on a dead end.

## Archive Policy

- Deprecated content stays for one quarter after replacement is published.
- Replace the old page with a pointer to the new tutorial; keep stable concepts even if framework examples change.
- Archive only after the replacement has been reviewed by a maintainer.
- Archive by moving the file under `docs/en/archive/` or `docs/zh/archive/` and removing it from the index; never delete without a recorded decision.

## Roles And Responsibilities

| Role | Quarterly Duties |
| --- | --- |
| Docs maintainer | Owns the quarterly review report, final archive decision, and breaking-change triage. |
| Lab owner | Re-runs Lab tests, updates `tested_against`, fixes broken Labs. |
| Translation lead | Confirms `i18n-key` parity, updates `last-synced`, resolves translation drift. |
| Community lead | Tracks contributor workload and burnout signals. |
| Reviewer | Validates the health metrics table and approves the report. |

## Common Failures And Handling

| Failure | Symptom | Handling |
| --- | --- | --- |
| Stale `validated_date` | `check_repository.py` exits with `is stale` | Re-validate content or deprecate; never bump the date without re-checking the facts. |
| Lab test regression | `unittest` reports failures after a dependency bump | Pin the new version in `tested_against`, fix the Lab, re-run the suite. |
| Translation drift | `en` and `zh` `i18n-key` sets differ | Update the missing mirror and bump `last-synced` on both sides. |
| Broken relative link | Link checker lists a missing target | Fix the path or remove the link; add the target file if it was moved. |
| Framework breaking change | `tested_against` anchor no longer matches reality | Follow the Breaking Change Process, then re-run Lab tests. |

## Worked Example

Quarterly review for `2026-Q4`:

```markdown
# Quarterly Review 2026-Q4

## Scope
- Repository version: `64d4678`
- Reviewed by: docs maintainer + translation lead
- Date: 2026-09-17

## Results
- Stale docs: 0 (2 fixed, 1 deprecated)
- Broken links: 0
- Failed Labs: 0 (re-validated after `langchain 0.3.2` release)
- Translation drift: 1 pair re-synced (`production-cost-stability-operations`)

## Actions
| Item | Owner | Due | Status |
| --- | --- | --- | --- |
| Deprecate outdated MCP example | docs maintainer | 2026-12-01 | open |
| Re-run L4 regression gate | lab owner | 2026-10-15 | done |
| Sync zh mirror for cost guide | translation lead | 2026-09-24 | done |
```

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

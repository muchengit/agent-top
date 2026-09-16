#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    Path("README.md"),
    Path("LICENSE"),
    Path("docs-site/index.html"),
    Path("README.zh-CN.md"),
    Path("agent-top-roadmap.md"),
    Path("ROADMAP_STATUS.md"),
    Path("docs/agent-top-concrete-framework.md"),
    Path("GOVERNANCE.md"),
    Path("CONTRIBUTING.md"),
    Path("CONTRIBUTING.zh-CN.md"),
    Path("docs/community/contribution-paths.md"),
    Path("docs/community/community-rhythm.md"),
    Path("docs/community/labels.md"),
    Path("docs/production/quarterly-maintenance.md"),
    Path("templates/monthly-contributor-report.md"),
    Path("CODE_OF_CONDUCT.md"),
    Path("docs/community/glossary.md"),
    Path("templates/article-template.md"),
    Path("templates/lab-template.md"),
    Path("templates/interview-question-template.md"),
    Path("templates/postmortem-template.md"),
]
MAX_STALE_DAYS = 180
DATE_PATTERN = re.compile(r"validated_date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})")
TESTED_PATTERN = re.compile(r"tested_against:\s*([^\n]+)")
RELATIVE_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def iter_markdown() -> list[Path]:
    paths = sorted(ROOT.rglob("*.md"))
    return [path for path in paths if ".git" not in path.parts]


def check_required_paths() -> None:
    missing = [str((ROOT / path).relative_to(ROOT)) for path in REQUIRED_PATHS if not (ROOT / path).exists()]
    if missing:
        fail("missing required paths: " + ", ".join(missing))


def check_version_anchors(markdown_paths: list[Path]) -> None:
    for path in markdown_paths:
        text = path.read_text(encoding="utf-8")
        if "tested_against:" in text and not TESTED_PATTERN.search(text):
            fail(f"{path.relative_to(ROOT)} has malformed tested_against")

        date_match = DATE_PATTERN.search(text)
        if date_match:
            try:
                parsed = datetime.strptime(date_match.group(1), "%Y-%m-%d").date()
            except ValueError as exc:
                fail(f"{path.relative_to(ROOT)} has invalid validated_date: {exc}")
                return
            days_old = (date.today() - parsed).days
            if days_old > MAX_STALE_DAYS:
                fail(f"{path.relative_to(ROOT)} is stale: {days_old} days old")


def check_relative_links(markdown_paths: list[Path]) -> None:
    broken: list[str] = []
    for path in markdown_paths:
        text = path.read_text(encoding="utf-8")
        for match in RELATIVE_LINK_PATTERN.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if target.startswith("file://"):
                broken.append(f"{path.relative_to(ROOT)} -> {target}")
                continue
            cleaned = target.split("#", 1)[0]
            if not cleaned:
                continue
            candidate = (path.parent / cleaned).resolve()
            if not candidate.exists():
                broken.append(f"{path.relative_to(ROOT)} -> {target}")
    if broken:
        fail("broken relative links: " + json.dumps(broken, ensure_ascii=False))


def check_no_conflict_markers(markdown_paths: list[Path]) -> None:
    markers = ["<<<<<<<", "=======", ">>>>>>>"]
    bad: list[str] = []
    for path in markdown_paths:
        text = path.read_text(encoding="utf-8")
        if any(marker in text for marker in markers):
            bad.append(str(path.relative_to(ROOT)))
    if bad:
        fail("merge conflict markers found: " + ", ".join(bad))


def main() -> None:
    check_required_paths()
    markdown_paths = iter_markdown()
    check_no_conflict_markers(markdown_paths)
    check_version_anchors(markdown_paths)
    check_relative_links(markdown_paths)
    print(f"Repository checks passed: {len(markdown_paths)} Markdown files checked.")


if __name__ == "__main__":
    main()

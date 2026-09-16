#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime
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
    Path("SECURITY.md"),
    Path("docs/community/contribution-paths.md"),
    Path("docs/community/community-rhythm.md"),
    Path("docs/community/labels.md"),
    Path("docs/community/maintainer-rotation.md"),
    Path("docs/community/contributor-of-the-month.md"),
    Path("docs/community/translation-workflow.md"),
    Path(".github/labels.yml"),
    Path("docs/community/contributor-onboarding.md"),
    Path("docs/community/README.md"),
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
FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
DATE_PATTERN = re.compile(r"validated_date:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})")
TESTED_PATTERN = re.compile(r"tested_against:\s*([^\n]+)")
RELATIVE_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
LAB_README_REQUIRED_SECTIONS = (
    "## Goal",
    "## Prerequisites",
    "## Run",
    "## Common Pitfalls",
    "## Self-Check",
)
LABEL_NAMES = {
    "good first issue",
    "docs-only",
    "translation-needed",
    "sync-required",
    "deprecated",
    "breaking-change",
    "maintainer-review",
    "lab",
    "interview",
    "production",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def iter_markdown() -> list[Path]:
    paths = sorted(ROOT.rglob("*.md"))
    return [path for path in paths if ".git" not in path.parts]


def check_required_paths() -> None:
    missing = [
        str((ROOT / path).relative_to(ROOT))
        for path in REQUIRED_PATHS
        if not (ROOT / path).exists()
    ]
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


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def check_github_labels() -> None:
    labels_path = ROOT / ".github" / "labels.yml"
    names = set()
    for line in labels_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("- name:"):
            continue
        name = stripped[len("- name:"):].strip().strip('"').strip("'")
        if name:
            names.add(name)
    missing = sorted(LABEL_NAMES - names)
    extra = sorted(names - LABEL_NAMES)
    if missing or extra:
        fail("label config mismatch: missing=" + ", ".join(missing) + "; extra=" + ", ".join(extra))

def check_no_conflict_markers(markdown_paths: list[Path]) -> None:
    markers = ["<<<<<<<", "=======", ">>>>>>>"]
    bad: list[str] = []
    for path in markdown_paths:
        text = path.read_text(encoding="utf-8")
        if any(marker in text for marker in markers):
            bad.append(str(path.relative_to(ROOT)))
    if bad:
        fail("merge conflict markers found: " + ", ".join(bad))


def check_bilingual_frontmatter(markdown_paths: list[Path]) -> None:
    bad: list[str] = []
    for path in markdown_paths:
        if "docs/en" not in path.parts and "docs/zh" not in path.parts:
            continue
        meta = parse_frontmatter(path)
        if "i18n-key" not in meta or "last-synced" not in meta:
            bad.append(str(path.relative_to(ROOT)))
    if bad:
        fail("bilingual frontmatter missing: " + ", ".join(bad))



def check_lab_readmes(markdown_paths: list[Path]) -> None:
    lab_readmes = [
        path
        for path in markdown_paths
        if path.name == "README.md"
        and path.relative_to(ROOT).parts[0] == "labs"
        and len(path.relative_to(ROOT).parts) == 4
    ]
    if not lab_readmes:
        fail("no lab README files found")
    bad: list[str] = []
    for path in lab_readmes:
        text = path.read_text(encoding="utf-8")
        missing = [section for section in LAB_README_REQUIRED_SECTIONS if section not in text]
        if missing:
            bad.append(str(path.relative_to(ROOT)) + ": " + ", ".join(missing))
    if bad:
        fail("lab README sections missing: " + "; ".join(bad))


def main() -> None:
    check_required_paths()
    markdown_paths = iter_markdown()
    check_no_conflict_markers(markdown_paths)
    check_version_anchors(markdown_paths)
    check_relative_links(markdown_paths)
    check_bilingual_frontmatter(markdown_paths)
    check_lab_readmes(markdown_paths)
    print(f"Repository checks passed: {len(markdown_paths)} Markdown files checked.")


if __name__ == "__main__":
    main()

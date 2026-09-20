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
    Path("docs/en/agent-top-concrete-framework.md"),
    Path("GOVERNANCE.md"),
    Path("CONTRIBUTING.md"),
    Path("CONTRIBUTING.zh-CN.md"),
    Path("SECURITY.md"),
    Path("docs/en/community/contribution-paths.md"),
    Path("docs/en/community/community-rhythm.md"),
    Path("docs/en/community/labels.md"),
    Path("docs/en/community/maintainer-rotation.md"),
    Path("docs/en/community/contributor-of-the-month.md"),
    Path("docs/en/community/translation-workflow.md"),
    Path(".github/labels.yml"),
    Path("docs/en/community/contributor-onboarding.md"),
    Path("docs/en/community/README.md"),
    Path("docs/en/production/quarterly-maintenance.md"),
    Path("templates/monthly-contributor-report.md"),
    Path("CODE_OF_CONDUCT.md"),
    Path("docs/en/community/glossary.md"),
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
    "good-first-L5",
    "original-pattern",
    "external-impact",
    "eval-evidence",
    "safety-review",
    "release-governance",
    "sig-candidate",
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
        rel_parts = path.relative_to(ROOT).parts
        is_bilingual = rel_parts[:2] in (("docs", "en"), ("docs", "zh"))
        if len(rel_parts) < 3 or not is_bilingual:
            continue
        meta = parse_frontmatter(path)
        missing = [
            key
            for key in ("title", "i18n-key", "last-synced", "validated_date")
            if key not in meta or not meta[key]
        ]
        if missing:
            bad.append(str(path.relative_to(ROOT)) + ": " + ", ".join(missing))
    if bad:
        fail("bilingual frontmatter missing: " + ", ".join(bad))




def check_bilingual_pairs(markdown_paths: list[Path]) -> None:
    keys_by_lang: dict[str, set[str]] = {"en": set(), "zh": set()}
    for path in markdown_paths:
        rel_parts = path.relative_to(ROOT).parts
        if len(rel_parts) < 2 or rel_parts[0] != "docs" or rel_parts[1] not in keys_by_lang:
            continue
        meta = parse_frontmatter(path)
        key = meta.get("i18n-key", "").strip().strip('"')
        if key:
            keys_by_lang[rel_parts[1]].add(key)
    missing = sorted(keys_by_lang["en"] ^ keys_by_lang["zh"])
    if missing:
        fail("unpaired bilingual keys: " + ", ".join(missing))


def check_root_doc_cross_links() -> None:
    """Root-level bilingual pairs must link each version to its counterpart."""
    bad: list[str] = []
    for en_path in sorted(ROOT.glob("*.md")):
        if en_path.name.endswith(".zh-CN.md"):
            continue
        zh_path = ROOT / f"{en_path.stem}.zh-CN.md"
        if not zh_path.exists():
            continue
        for path, counterpart in ((en_path, zh_path.name), (zh_path, en_path.name)):
            targets = {
                match.group(1).strip()
                for match in RELATIVE_LINK_PATTERN.finditer(path.read_text(encoding="utf-8"))
            }
            if counterpart not in targets:
                bad.append(f"{path.name}: no link to {counterpart}")
    if bad:
        fail("root doc bilingual cross-link missing: " + "; ".join(bad))


def check_docs_index_coverage() -> None:
    """Each docs/{lang}/README.md must link every docs/{lang} Markdown file."""
    for lang in ("en", "zh"):
        index_path = ROOT / "docs" / lang / "README.md"
        if not index_path.exists():
            fail(f"docs/{lang}/README.md missing")
        text = index_path.read_text(encoding="utf-8")
        linked = set()
        for match in RELATIVE_LINK_PATTERN.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            cleaned = target.split("#", 1)[0]
            if not cleaned:
                continue
            candidate = (index_path.parent / cleaned).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                continue
            linked.add(str(candidate.relative_to(ROOT)))
        all_docs = {
            str(path.relative_to(ROOT))
            for path in (ROOT / "docs" / lang).rglob("*.md")
            if path != index_path
        }
        missing = sorted(all_docs - linked)
        if missing:
            fail(f"docs/{lang}/README.md does not list: " + ", ".join(missing))


def check_docs_index_examples() -> None:
    """Each docs/{lang}/README.md must link every examples/*/README.md."""
    examples = {
        str(path.relative_to(ROOT))
        for path in (ROOT / "examples").glob("*/README.md")
    }
    if not examples:
        return
    for lang in ("en", "zh"):
        index_path = ROOT / "docs" / lang / "README.md"
        if not index_path.exists():
            continue
        text = index_path.read_text(encoding="utf-8")
        linked: set[str] = set()
        for match in RELATIVE_LINK_PATTERN.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            cleaned = target.split("#", 1)[0]
            if not cleaned:
                continue
            candidate = (index_path.parent / cleaned).resolve()
            if candidate.is_relative_to(ROOT):
                linked.add(str(candidate.relative_to(ROOT)))
        missing = sorted(examples - linked)
        if missing:
            fail(f"docs/{lang}/README.md does not list examples: " + ", ".join(missing))


UNITTEST_MODULE_PATTERN = re.compile(
    r"python3? -m unittest\s+(?!discover)([a-zA-Z0-9_.]+)"
)


def check_lab_readmes(markdown_paths: list[Path]) -> None:
    lab_readmes = [
        path
        for path in markdown_paths
        if path.name == "README.md"
        and is_concrete_lab_readme(path.relative_to(ROOT).parts)
    ]
    if not lab_readmes:
        fail("no lab README files found")
    bad: list[str] = []
    bad_run: list[str] = []
    for path in lab_readmes:
        text = path.read_text(encoding="utf-8")
        missing = [section for section in LAB_README_REQUIRED_SECTIONS if section not in text]
        if missing:
            bad.append(str(path.relative_to(ROOT)) + ": " + ", ".join(missing))
        run_match = UNITTEST_MODULE_PATTERN.search(text)
        if not run_match:
            bad_run.append(
                str(path.relative_to(ROOT))
                + ": no `python -m unittest <module>` command in ## Run"
            )
            continue
        module_path = run_match.group(1).replace(".", "/") + ".py"
        candidate = (ROOT / module_path).resolve()
        if not candidate.exists():
            bad_run.append(
                str(path.relative_to(ROOT))
                + f": ## Run targets missing test file {module_path}"
            )
    if bad:
        fail("lab README sections missing: " + "; ".join(bad))
    if bad_run:
        fail("lab README run commands invalid: " + "; ".join(bad_run))



def is_concrete_lab_readme(parts: tuple[str, ...]) -> bool:
    return len(parts) == 4 and parts[0] == "labs" and parts[1].startswith("l")


MIN_LAB_TESTS = 6


def count_test_methods(path: Path) -> int:
    """Count ``def test_*`` methods in a lab test module."""
    return sum(
        1
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.lstrip().startswith("def test_")
    )


def check_executable_labs() -> None:
    labs_root = ROOT / "labs"
    bad: list[str] = []
    thin: list[str] = []
    missing_zh: list[str] = []
    for level_dir in sorted(labs_root.glob("l*")):
        if not level_dir.is_dir():
            continue
        for lab_dir in sorted(level_dir.iterdir()):
            if not lab_dir.is_dir() or lab_dir.name == "__pycache__":
                continue
            code = list(lab_dir.glob("agent_top_labs_*.py"))
            tests = list(lab_dir.glob("test_*.py"))
            if not (lab_dir / "README.md").exists():
                bad.append(str(lab_dir.relative_to(ROOT)) + ": missing README.md")
                continue
            if not (lab_dir / "README.zh-CN.md").exists():
                missing_zh.append(str(lab_dir.relative_to(ROOT)))
            if not code or not tests:
                bad.append(str(lab_dir.relative_to(ROOT)) + ": missing code or tests")
                continue
            test_count = sum(count_test_methods(path) for path in tests)
            if test_count < MIN_LAB_TESTS:
                thin.append(f"{lab_dir.relative_to(ROOT)} ({test_count} tests)")
    if bad:
        fail("labs missing executable code or tests: " + ", ".join(bad))
    if thin:
        fail(
            f"labs below {MIN_LAB_TESTS} tests: "
            + ", ".join(thin)
        )
    if missing_zh:
        fail("labs missing Chinese README mirror: " + ", ".join(missing_zh))


def check_examples_jsonl() -> None:
    examples_root = ROOT / "examples"
    if not examples_root.is_dir():
        return
    jsonl_paths = sorted(examples_root.rglob("*.jsonl"))
    if not jsonl_paths:
        fail("no example JSONL files found under examples/")
    for path in jsonl_paths:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                json.loads(line)
            except json.JSONDecodeError as exc:
                fail(f"{path.relative_to(ROOT)}:{number} is not valid JSONL: {exc}")


ANSWER_KEY_ID_SPECS: dict[str, tuple[str, str, str]] = {
    "agent-decision-trace": ("ID", "tool-calls.jsonl", "id"),
    "agent-eval-regression": ("Fixture", "fixtures.jsonl", "fixture_id"),
    "coding-task-navigation": ("Request ID", "requests.jsonl", "request_id"),
    "coding-workspace-safety": ("ID", "changes.jsonl", "id"),
    "data-source-policy": ("ID", "sources.jsonl", "id"),
    "github-agent-review": ("PR", "pr-context.jsonl", "pr_id"),
    "memory-vs-evidence": ("Prompt ID", "prompts.jsonl", "id"),
    "rag-evidence-refusal": ("Prompt ID", "prompts.jsonl", "id"),
}


def check_example_answer_keys() -> None:
    """Answer Key IDs in example READMEs must match data file IDs."""
    bad: list[str] = []
    for name, (column, data_file, id_field) in ANSWER_KEY_ID_SPECS.items():
        example_dir = ROOT / "examples" / name
        readme = example_dir / "README.md"
        if not readme.exists():
            continue
        text = readme.read_text(encoding="utf-8")
        match = re.search(r"## Answer Key\n\n((?:\|.*\|\n)+)", text)
        if not match:
            bad.append(f"{name}: no Answer Key table")
            continue
        key_ids = {
            cells[0].strip()
            for line in match.group(1).strip().splitlines()
            if (cells := [cell.strip() for cell in line.strip().strip("|").split("|")])
            and cells[0] != column
            and not cells[0].startswith("---")
        }
        data_path = example_dir / data_file
        data_ids = {
            json.loads(line)[id_field]
            for line in data_path.read_text(encoding="utf-8").splitlines()
            if line.strip() and id_field in json.loads(line)
        }
        missing = sorted(data_ids - key_ids)
        extra = sorted(key_ids - data_ids)
        if missing or extra:
            bad.append(
                f"{name}: Answer Key missing {missing}, extra {extra}"
            )
    if bad:
        fail("example Answer Key mismatch: " + "; ".join(bad))


def check_docs_site_links() -> None:
    broken: list[str] = []
    for page in ("index.html", "search.html"):
        path = ROOT / "docs-site" / page
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r'href="([^"]*)"', text):
            href = match.group(1).strip()
            if not href or href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            cleaned = href.split("#", 1)[0]
            if not cleaned:
                continue
            candidate = (ROOT / "docs-site" / cleaned).resolve()
            if not candidate.exists():
                broken.append(f"{page}: {href}")
        # Validate search ENTRIES `p:` target paths as well
        for match in re.finditer(r'p: "([^"]+)"', text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://")):
                continue
            candidate = (ROOT / "docs-site" / target).resolve()
            if not candidate.exists():
                broken.append(f"{page}: p:{target}")
    if broken:
        fail("broken docs-site links: " + json.dumps(broken, ensure_ascii=False))


def check_docs_topic_dirs() -> None:
    en_root = ROOT / "docs" / "en"
    zh_root = ROOT / "docs" / "zh"
    if not en_root.is_dir() or not zh_root.is_dir():
        fail("docs/en or docs/zh missing")
    en_topics = {p.name for p in en_root.iterdir() if p.is_dir()}
    zh_topics = {p.name for p in zh_root.iterdir() if p.is_dir()}
    for missing in sorted(en_topics - zh_topics):
        print(f"WARN: topic dir in docs/en but not docs/zh: {missing}")
    for missing in sorted(zh_topics - en_topics):
        print(f"WARN: topic dir in docs/zh but not docs/en: {missing}")


def check_lab_level_readmes() -> None:
    missing_levels: list[str] = []
    missing_zh: list[str] = []
    bad: list[str] = []
    for level_dir in sorted((ROOT / "labs").glob("l*")):
        if not level_dir.is_dir():
            continue
        readme = level_dir / "README.md"
        if not readme.exists():
            missing_levels.append(level_dir.name)
            continue
        if not (level_dir / "README.zh-CN.md").exists():
            missing_zh.append(level_dir.name)
        text = readme.read_text(encoding="utf-8")
        missing = [section for section in LAB_README_REQUIRED_SECTIONS if section not in text]
        if missing:
            bad.append(f"{level_dir.name}: " + ", ".join(missing))
    if missing_levels:
        fail("lab level README missing: " + ", ".join(missing_levels))
    if missing_zh:
        fail("lab level README missing Chinese mirror: " + ", ".join(missing_zh))
    if bad:
        fail("lab level README sections missing: " + "; ".join(bad))


def concrete_lab_dirs(level_dir: Path) -> set[str]:
    """Executable lab directories inside one `labs/l*` level directory."""
    return {
        path.name
        for path in level_dir.iterdir()
        if path.is_dir() and path.name != "__pycache__"
    }


def check_lab_level_index_coverage() -> None:
    """Each lab level index must link every executable lab in that level."""
    missing: list[str] = []
    for level_dir in sorted((ROOT / "labs").glob("l*")):
        if not level_dir.is_dir():
            continue
        for index_name in ("README.md", "README.zh-CN.md"):
            index_path = level_dir / index_name
            if not index_path.exists():
                continue
            text = index_path.read_text(encoding="utf-8")
            linked = {
                match.group(1).split("/")[0]
                for match in RELATIVE_LINK_PATTERN.finditer(text)
                if "/" in match.group(1)
                and match.group(1).endswith(("/README.md", "/README.zh-CN.md"))
            }
            for name in sorted(concrete_lab_dirs(level_dir) - linked):
                missing.append(f"{index_path.relative_to(ROOT)}: {name}")
    if missing:
        fail("lab level index does not list: " + ", ".join(missing))


def check_example_dirs_readmes() -> None:
    examples_root = ROOT / "examples"
    if not examples_root.is_dir():
        return
    missing: list[str] = []
    missing_shape: list[str] = []
    index_missing: list[str] = []
    for example_dir in sorted(examples_root.iterdir()):
        if not example_dir.is_dir():
            continue
        readme = example_dir / "README.md"
        if not readme.exists():
            missing.append(example_dir.name)
            continue
        if "## JSONL Shape" not in readme.read_text(encoding="utf-8"):
            missing_shape.append(example_dir.name)
    for name in missing:
        print(f"WARN: example dir missing README.md: {name}")
    if missing_shape:
        fail("example READMEs missing ## JSONL Shape: " + ", ".join(missing_shape))
    index_path = examples_root / "README.md"
    if index_path.exists():
        index_text = index_path.read_text(encoding="utf-8")
        linked_dirs = {
            match.group(1).split("/")[0]
            for match in RELATIVE_LINK_PATTERN.finditer(index_text)
            if match.group(1).endswith("/README.md")
            and "/" in match.group(1)
        }
        example_dirs = {
            path.name
            for path in examples_root.iterdir()
            if path.is_dir()
        }
        index_missing = sorted(example_dirs - linked_dirs)
    if index_missing:
        fail(
            "examples/README.md does not list: "
            + ", ".join(index_missing)
        )


def expand_lab_level_ranges(text: str) -> list[str]:
    """Expand explicit lab level ranges (e.g. `labs/l0`-`labs/l5`) into
    individual `labs/l{level}` substrings for loose matching."""
    found: list[str] = []
    for start, end in re.findall(r"labs/l(\d)`-`labs/l(\d)", text):
        for level in range(int(start), int(end) + 1):
            found.append(f"labs/l{level}")
    return found


def check_readme_mentions_lab_levels() -> None:
    expected = set(f"labs/l{level}" for level in range(6))
    missing: list[str] = []
    for readme_name in ("README.md", "README.zh-CN.md"):
        readme_path = ROOT / readme_name
        if not readme_path.exists():
            missing.append(f"{readme_name}: file missing")
            continue
        text = readme_path.read_text(encoding="utf-8")
        mentioned = set(expand_lab_level_ranges(text))
        mentioned.update(re.findall(r"labs/l\d", text))
        for substring in sorted(expected - mentioned):
            if substring not in text:
                missing.append(f"{readme_name}: no mention of {substring}")
    if missing:
        fail("READMEs must mention lab level READMEs: " + "; ".join(missing))




def check_template_pairs() -> None:
    """Every template listed in templates/README.md must exist as an EN/CN pair."""
    readme = ROOT / "templates" / "README.md"
    if not readme.exists():
        return
    text = readme.read_text(encoding="utf-8")
    pairs = re.findall(r"\[`([^`]+)`\]\([^)]*\) \(EN\) ↔ \[`([^`]+)`\]\([^)]*\) \(CN\)", text)
    bad: list[str] = []
    for en_name, zh_name in pairs:
        en_path = ROOT / "templates" / en_name
        zh_path = ROOT / "templates" / zh_name
        if not en_path.exists():
            bad.append(f"missing EN {en_name}")
        if not zh_path.exists():
            bad.append(f"missing CN {zh_name}")
    if bad:
        fail("template pair mismatch: " + "; ".join(bad))




SEARCH_ENTRY_PATTERN = re.compile(
    r'^\s*\{ t: "[^"]+", p: "[^"]+", c: "[^"]+", l: "(?:en|zh)" \},\s*$'
)


def check_search_entries_shape() -> None:
    """Every search entry must stay a single-line object literal with exactly one
    trailing comma, so the ENTRIES array keeps parsing as valid JavaScript."""
    search_path = ROOT / "docs-site" / "search.html"
    if not search_path.exists():
        return
    bad: list[str] = []
    for line in search_path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("{ t: "):
            continue
        if not SEARCH_ENTRY_PATTERN.match(line):
            bad.append(line.strip())
    if bad:
        fail(
            "docs-site/search.html has malformed ENTRIES lines "
            "(single line, exactly one trailing comma): "
            + " | ".join(bad)
        )


def check_search_coverage() -> None:
    """Every repository Markdown file must be reachable from docs-site/search.html."""
    search_path = ROOT / "docs-site" / "search.html"
    if not search_path.exists():
        return
    text = search_path.read_text(encoding="utf-8")
    entry_paths = re.findall(r'p: "([^"]+)"', text)
    entries = {match.replace("../", "").rstrip("/") for match in entry_paths}
    excluded_roots = {".git", "node_modules", ".github"}
    all_md: set[str] = set()
    for path in ROOT.rglob("*.md"):
        parts = path.relative_to(ROOT).parts
        if parts and parts[0] in excluded_roots:
            continue
        all_md.add(str(path.relative_to(ROOT)))
    missing = sorted(all_md - entries)
    if missing:
        fail("search.html missing entries: " + ", ".join(missing))


NAV_TOPIC_DIRS = (
    "cases",
    "community",
    "concepts",
    "frameworks",
    "governance",
    "interviews",
    "operations",
    "portfolio",
    "production",
    "quick-reference",
    "skills",
    "tutorials",
    "vibe-coding",
)


def check_nav_topic_coverage() -> None:
    """Every docs topic directory must be represented in docs-site/index.html."""
    index_path = ROOT / "docs-site" / "index.html"
    if not index_path.exists():
        fail("docs-site/index.html missing")
    text = index_path.read_text(encoding="utf-8")
    for topic in NAV_TOPIC_DIRS:
        en_dir = ROOT / "docs" / "en" / topic
        if not en_dir.is_dir():
            continue
        en_prefix = f"../docs/en/{topic}/"
        zh_prefix = f"../docs/zh/{topic}/"
        if en_prefix not in text and zh_prefix not in text:
            fail(f"docs-site/index.html has no links for docs/{topic}/")


def main() -> None:
    check_required_paths()
    markdown_paths = iter_markdown()
    check_no_conflict_markers(markdown_paths)
    check_version_anchors(markdown_paths)
    check_relative_links(markdown_paths)
    check_bilingual_frontmatter(markdown_paths)
    check_bilingual_pairs(markdown_paths)
    check_root_doc_cross_links()
    check_docs_index_coverage()
    check_docs_index_examples()
    check_lab_readmes(markdown_paths)
    check_lab_level_readmes()
    check_lab_level_index_coverage()
    check_executable_labs()
    check_example_dirs_readmes()
    check_readme_mentions_lab_levels()
    check_docs_topic_dirs()
    check_examples_jsonl()
    check_example_answer_keys()
    check_docs_site_links()
    check_template_pairs()
    check_search_entries_shape()
    check_search_coverage()
    check_nav_topic_coverage()
    print(f"Repository checks passed: {len(markdown_paths)} Markdown files checked.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Normalize repository content into JSON for the Agent-Top app shell."""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "build" / "app-content"
FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LEVEL_FILE_PATTERNS = {
    0: ["l0-first-llm-call.md", "L0第一次LLM调用.md"],
    1: ["l1-minimal-react-agent.md", "L1最小ReActAgent.md"],
    2: ["l2-single-agent-mcp.md", "L2可靠单Agent与MCP.md"],
    3: ["l3-rag-memory-observability.md", "L3RAG记忆与可观测.md"],
    4: ["l4-production.md", "L4生产化.md"],
    5: ["l5-custom-patterns.md", "L5原创模式.md"],
}
LEVEL_TITLES = {
    0: "First LLM Call",
    1: "Minimal ReAct Agent",
    2: "Single Agent + MCP",
    3: "RAG, Memory, Observability",
    4: "Production",
    5: "Custom Patterns",
}


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


def first_heading(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def summary_from_markdown(path: Path, frontmatter: dict[str, str], limit: int = 180) -> str:
    if frontmatter.get("summary"):
        return frontmatter["summary"]
    text = FRONTMATTER_PATTERN.sub("", path.read_text(encoding="utf-8"), count=1)
    blocks: list[str] = []
    current: list[str] = []
    skip_prefixes = ("#", "- ", "[", "|", "```", "!", ">", "<", "`", "---")
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            if current:
                blocks.append(" ".join(current))
                current = []
            continue
        if stripped.startswith(skip_prefixes):
            if current:
                blocks.append(" ".join(current))
                current = []
            continue
        current.append(stripped)
    if current:
        blocks.append(" ".join(current))
    summary_parts: list[str] = []
    for block in blocks:
        summary_parts.append(block)
        if sum(len(part) for part in summary_parts) >= limit:
            break
        if len(summary_parts) >= 2:
            break
    summary = " ".join(summary_parts).strip()
    return summary[:limit].strip()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "item"


def level_for_doc(path: Path, frontmatter: dict[str, str]) -> int | None:
    if "capability_level" in frontmatter:
        value = frontmatter["capability_level"].strip().strip('"')
        if value.startswith("L") and value[1:].isdigit():
            return int(value[1:])
    if path.parts and path.parts[0] in {"docs", "labs"}:
        return None
    for level, names in LEVEL_FILE_PATTERNS.items():
        if path.name in names:
            return level
    return None


def docs_lesson(path: Path) -> dict[str, object] | None:
    rel = path.relative_to(ROOT).as_posix()
    parts = rel.split("/")
    if parts[0] != "docs" or parts[1] not in {"en", "zh"}:
        return None
    if len(parts) < 3:
        return None
    language = "en" if parts[1] == "en" else "zh"
    frontmatter = parse_frontmatter(path)
    title = frontmatter.get("title") or first_heading(path)
    level = level_for_doc(path, frontmatter)
    key = frontmatter.get("i18n-key", path.stem)
    return {
        "id": slugify(f"{language}-{key}"),
        "courseId": f"level-{level}" if level is not None else slugify(parts[2]),
        "level": level,
        "title": title,
        "language": language,
        "sourcePath": rel,
        "summary": summary_from_markdown(path, frontmatter),
        "validatedDate": frontmatter.get("validated_date"),
    }


def lab_entry(path: Path) -> dict[str, object] | None:
    rel = path.relative_to(ROOT).as_posix()
    if not rel.startswith("labs/") or not rel.endswith(".md"):
        return None
    frontmatter = parse_frontmatter(path)
    text = path.read_text(encoding="utf-8")
    level = level_for_doc(path, frontmatter)
    source_parts = rel.split("/")
    if level is None and len(source_parts) >= 2:
        token = source_parts[1]
        if token.startswith("l") and token[1:].isdigit():
            level = int(token[1:])
    objective = ""
    objective_match = re.search(r"^## Goal\n(.+?)(?=\n## |\Z)", text, re.MULTILINE | re.DOTALL)
    if objective_match:
        objective = " ".join(objective_match.group(1).strip().split())[:240]
    self_check: list[str] = []
    check_block = re.search(r"^## Self-Check\n(.+?)(?=\n## |\Z)", text, re.MULTILINE | re.DOTALL)
    if check_block:
        for line in check_block.group(1).splitlines():
            stripped = line.strip()
            if stripped.startswith(("-", "*", "1.", "2.", "3.")):
                self_check.append(re.sub(r"^[-*0-9.]+\s*", "", stripped))
    title = frontmatter.get("title") or first_heading(path)
    return {
        "id": slugify(rel.replace("labs/", "").replace(".md", "")),
        "title": title,
        "level": level,
        "sourcePath": rel,
        "objective": objective,
        "selfCheck": self_check,
        "testedAgainst": frontmatter.get("tested_against"),
        "validatedDate": frontmatter.get("validated_date"),
    }


def search_entry(path: Path) -> dict[str, object] | None:
    rel = path.relative_to(ROOT).as_posix()
    frontmatter = parse_frontmatter(path)
    title = frontmatter.get("title") or first_heading(path)
    if rel.startswith("docs/en/"):
        category = "Docs"
        language = "en"
    elif rel.startswith("docs/zh/"):
        category = "Docs"
        language = "zh"
    elif rel.startswith("labs/"):
        category = "Labs"
        language = "zh" if rel.endswith(".zh-CN.md") else "en"
    elif rel.startswith("examples/"):
        category = "Examples"
        language = "en"
    elif rel.startswith("templates/"):
        category = "Templates"
        language = "en"
    else:
        category = "Research"
        language = "zh" if path.name.endswith(".zh-CN.md") else "en"
    return {
        "id": slugify(rel),
        "title": title,
        "sourcePath": rel,
        "category": category,
        "language": language,
        "summary": summary_from_markdown(path, frontmatter, limit=140),
    }


def build_courses() -> list[dict[str, object]]:
    courses: list[dict[str, object]] = []
    for level, en_names in LEVEL_FILE_PATTERNS.items():
        en_path = ROOT / "docs" / "en" / en_names[0]
        if not en_path.exists():
            continue
        frontmatter = parse_frontmatter(en_path)
        courses.append(
            {
                "id": f"level-{level}",
                "level": level,
                "title": LEVEL_TITLES[level],
                "summary": summary_from_markdown(en_path, frontmatter),
                "sourcePath": en_path.relative_to(ROOT).as_posix(),
                "lessonIds": [
                    entry["id"]
                    for entry in map(docs_lesson, sorted((ROOT / "docs").rglob("*.md")))
                    if entry and entry.get("level") == level
                ],
            }
        )
    return courses


def write_json(name: str, data: object) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / name
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return out_path


def main() -> None:
    markdown_paths = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    lessons = [entry for entry in map(docs_lesson, markdown_paths) if entry]
    labs = [entry for entry in map(lab_entry, markdown_paths) if entry]
    search_index = [entry for entry in map(search_entry, markdown_paths) if entry]
    courses = build_courses()
    generated_at = datetime.utcnow().strftime("%Y-%m-%d")
    write_json("courses.json", courses)
    write_json("lessons.json", lessons)
    write_json("labs.json", labs)
    write_json("search-index.json", search_index)
    print(
        f"app content generated: courses={len(courses)} lessons={len(lessons)} "
        f"labs={len(labs)} search={len(search_index)} generated_at={generated_at}"
    )


if __name__ == "__main__":
    main()

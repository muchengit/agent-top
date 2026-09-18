#!/usr/bin/env python3
"""Smoke checks for examples/ JSONL fixtures and per-directory READMEs."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"


@dataclass
class Report:
    passed: int = 0
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def warned(self) -> int:
        return len(self.warnings)

    @property
    def failed(self) -> int:
        return len(self.errors)

    def record_warning(self, message: str) -> None:
        self.warnings.append(message)
        print(f"WARN: {message}")

    def record_error(self, message: str) -> None:
        self.errors.append(message)
        print(f"ERROR: {message}")


def iter_jsonl_files(example_dir: Path) -> list[Path]:
    return sorted(example_dir.glob("*.jsonl"))


def read_objects(path: Path) -> list[dict[str, object]]:
    objects: list[dict[str, object]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            parsed = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"line {number} is not valid JSON: {exc}") from exc
        if not isinstance(parsed, dict):
            raise ValueError(f"line {number} is not a JSON object: {type(parsed).__name__}")
        objects.append(parsed)
    return objects


def object_fields(obj: dict[str, object]) -> set[str]:
    return set(obj.keys())


def check_jsonl_file(path: Path, report: Report) -> None:
    try:
        objects = read_objects(path)
    except (OSError, ValueError) as exc:
        report.record_error(f"{relative(path)} failed: {exc}")
        return
    if not objects:
        report.record_error(f"{relative(path)} has no JSON objects")
        return
    for number, obj in enumerate(objects, 1):
        if not obj:
            report.record_error(f"{relative(path)}:{number} is an empty object")
            return
    report.passed += 1


def check_template_fields(example_dir: Path, report: Report) -> None:
    jsonl_paths = iter_jsonl_files(example_dir)
    templates = [
        path
        for path in jsonl_paths
        if ".template." in path.name or "-template." in path.name
    ]
    if not templates:
        return
    for path in templates:
        objects = read_objects(path)
        if not objects:
            report.record_error(f"{relative(path)} has no JSON objects")
            continue
        template_fields = object_fields(objects[0])
        inconsistent = any(object_fields(obj) != template_fields for obj in objects[1:])
        if inconsistent:
            report.record_warning(
                f"{relative(path)} template objects have inconsistent fields"
            )
        report.passed += 1


def check_example_dir(example_dir: Path, report: Report) -> None:
    if not (example_dir / "README.md").is_file():
        report.record_error(f"{relative(example_dir)} missing README.md")
        return
    jsonl_paths = iter_jsonl_files(example_dir)
    if not jsonl_paths:
        report.record_error(f"{relative(example_dir)} has no JSONL files")
        return
    for path in jsonl_paths:
        check_jsonl_file(path, report)
    check_template_fields(example_dir, report)


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    if not EXAMPLES.is_dir():
        print(f"ERROR: {relative(EXAMPLES)} not found")
        return 1

    report = Report()
    example_dirs = sorted(
        path for path in EXAMPLES.iterdir() if path.is_dir() and not path.name.startswith(".")
    )
    if not example_dirs:
        report.record_error("no example directories found under examples/")
    for example_dir in example_dirs:
        check_example_dir(example_dir, report)

    print(
        f"examples smoke: passed={report.passed} "
        f"warned={report.warned} failed={report.failed}"
    )
    return 1 if report.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

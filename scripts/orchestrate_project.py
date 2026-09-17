#!/usr/bin/env python3
"""Generate a lightweight project dispatch queue for the Agent-Top main agent."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

EMPLOYEES = {
    "Research Discoverer": "Find public sources that affect roadmap gaps or Lab updates.",
    "Python Engineer": "Update deterministic Python Labs and tests.",
    "Node.js/TypeScript Engineer": "Update JS/TS examples and keep runtime behavior aligned.",
    "Rust Engineer": "Update Rust examples and compile evidence.",
    "Go Engineer": "Update Go modules, tests, and usage notes.",
    "Language Parity Reviewer": "Compare behavior across all supported language examples.",
    "Docs Structure Auditor": "Check Markdown tree, links, frontmatter, and bilingual pairs.",
    "Translation Editor": "Translate or synchronize English and Chinese docs.",
    "Interview Coach": "Add interview questions, rubrics, and scoring notes.",
    "Interview Candidate": "Prepare STAR answers and portfolio walkthrough material.",
    "Open Source Contributor": "Prepare contribution plans and external issue/PR notes.",
    "Eval and Observability Engineer": "Add evals, traces, metrics, and regression evidence.",
    "Safety and Guardrail Engineer": "Review permissions, destructive actions, and rollback notes.",
    "Cost and Reliability Engineer": "Review latency, retries, budgets, and degradation plans.",
    "Community Operations Lead": "Maintain issues, translation backlog, and showcase flow.",
}

QUEUE_ORDER = [
    "Research Discoverer",
    "Language Parity Reviewer",
    "Docs Structure Auditor",
    "Python Engineer",
    "Node.js/TypeScript Engineer",
    "Rust Engineer",
    "Go Engineer",
    "Translation Editor",
    "Interview Coach",
    "Interview Candidate",
    "Open Source Contributor",
    "Eval and Observability Engineer",
    "Safety and Guardrail Engineer",
    "Cost and Reliability Engineer",
    "Community Operations Lead",
]


def build_queue(start: int, count: int) -> list[tuple[str, str]]:
    workers = [name for name in EMPLOYEES if name in QUEUE_ORDER]
    queue: list[tuple[str, str]] = []
    for index in range(count):
        name = workers[(start + index) % len(workers)]
        queue.append((name, EMPLOYEES[name]))
    return queue


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    queue = build_queue(args.start, max(args.count, 0))
    lines = [
        "# Project Dispatch Queue",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
    ]
    for number, (name, objective) in enumerate(queue, start=1):
        lines.extend(
            [
                f"## {number}. {name}",
                "",
                f"- Objective: {objective}",
                "- Expected files:",
                "- Acceptance criteria:",
                "- Quality gates: repository checks plus lane-specific review",
                "- Main agent review notes:",
                "",
            ]
        )
    content = "\n".join(lines)
    if args.output:
        args.output.write_text(content, encoding="utf-8")
    else:
        print(content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

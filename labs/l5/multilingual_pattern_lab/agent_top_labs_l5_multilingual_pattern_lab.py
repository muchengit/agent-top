"""Shared constants for the multilingual L5 pattern lab."""

from __future__ import annotations

SAFETY_RULE = "delete_all"
READY_REASON = "ready_for_execution"
BLOCKED_REASON = "blocked_by_safety_rule"


def run_python_pattern(request: str) -> tuple[str, list[tuple[str, str, str]]]:
    if any(rule in request for rule in (SAFETY_RULE,)):
        return BLOCKED_REASON, []
    return (
        READY_REASON,
        [
            ("clarify", "validator", "remove unclear fields"),
            ("execute", "tool_gateway", "restore previous state"),
            ("verify", "eval_probe", "disable path"),
        ],
    )


def assert_ready_plan(stop_reason: str, steps: list[tuple[str, str, str]]) -> None:
    assert stop_reason == READY_REASON
    assert [intent for intent, _, _ in steps] == ["clarify", "execute", "verify"]


def assert_blocked_plan(stop_reason: str, steps: list[tuple[str, str, str]]) -> None:
    assert stop_reason == BLOCKED_REASON
    assert not steps

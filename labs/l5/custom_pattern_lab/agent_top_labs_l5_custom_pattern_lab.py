"""L5 custom pattern lab."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlanStep:
    intent: str
    tool: str
    rollback_hint: str


@dataclass(frozen=True)
class PatternResult:
    steps: tuple[PlanStep, ...]
    stop_reason: str


class VerifiableActionPattern:
    """A reusable pattern that plans, acts, verifies, and stops."""

    def __init__(self, safety_rules: tuple[str, ...]) -> None:
        self.safety_rules = safety_rules

    def plan(self, request: str) -> PatternResult:
        if any(rule in request for rule in self.safety_rules):
            return PatternResult((), "blocked_by_safety_rule")
        return PatternResult(
            (
                PlanStep("clarify", "validator", "remove unclear fields"),
                PlanStep("execute", "tool_gateway", "restore previous state"),
                PlanStep("verify", "eval_probe", "disable path"),
            ),
            "ready_for_execution",
        )

"""L4 release gate simulation."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GateResult:
    name: str
    passed: bool
    blocking: bool


@dataclass(frozen=True)
class ReleaseProfile:
    critical_safety_failures: int
    missing_trace_fields: int
    rollback_plan_present: bool
    cost_ratio: float
    cost_budget_ratio: float


def evaluate_release(profile: ReleaseProfile) -> tuple[bool, list[str]]:
    failures: list[str] = []
    if profile.critical_safety_failures > 0:
        failures.append("critical_safety_failures")
    if profile.missing_trace_fields > 0:
        failures.append("missing_trace_fields")
    if not profile.rollback_plan_present:
        failures.append("missing_rollback_plan")
    if profile.cost_ratio > profile.cost_budget_ratio:
        failures.append("cost_over_budget")
    return (not failures, failures)

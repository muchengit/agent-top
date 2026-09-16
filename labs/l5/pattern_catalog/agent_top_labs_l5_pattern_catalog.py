"""L5 deterministic catalog for reusable Agent patterns."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PatternEntry:
    name: str
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    safety_checks: tuple[str, ...]
    verification: tuple[str, ...]


PATTERN_CATALOG: dict[str, PatternEntry] = {
    "verifiable-action": PatternEntry(
        name="verifiable-action",
        inputs=("request", "safety_rules"),
        outputs=("plan", "stop_reason"),
        safety_checks=("block_on_rule",),
        verification=("eval_probe",),
    ),
    "safe-tool-routing": PatternEntry(
        name="safe-tool-routing",
        inputs=("request", "tool_policy", "role"),
        outputs=("route", "outcome"),
        safety_checks=("role_check", "confirmation_check"),
        verification=("tool_audit_log",),
    ),
}


def ready_pattern(name: str) -> bool:
    entry = PATTERN_CATALOG.get(name)
    if entry is None:
        return False
    return bool(entry.inputs and entry.outputs and entry.safety_checks and entry.verification)

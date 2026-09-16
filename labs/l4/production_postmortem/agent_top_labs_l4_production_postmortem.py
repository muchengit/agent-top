"""L4 local skeleton for production postmortem review."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum


class Severity(Enum):
    SEV1 = 1
    SEV2 = 2
    SEV3 = 3
    SEV4 = 4


class ActionType(Enum):
    IMMEDIATE_FIX = "immediate-fix"
    SAFETY_GUARDRAIL = "safety-guardrail"
    EVAL_REGRESSION = "eval-regression"
    OBSERVABILITY = "observability"
    ROLLBACK = "rollback"
    PROCESS_CHANGE = "process-change"


@dataclass(frozen=True)
class ActionItem:
    title: str
    owner: str
    due_date: date
    action_type: ActionType
    done: bool = False

    def has_required_fields(self) -> bool:
        return bool(self.title.strip()) and bool(self.owner.strip())

    def is_overdue(self, today: date) -> bool:
        return not self.done and self.due_date < today


@dataclass(frozen=True)
class PostmortemDraft:
    summary: str
    root_causes: tuple[str, ...]
    action_items: tuple[ActionItem, ...]
    rollback_plan: str
    evaluation_plan: str
    safety_controls: tuple[str, ...]


def required_coverage(draft: PostmortemDraft) -> list[str]:
    missing: list[str] = []
    if not draft.summary.strip():
        missing.append("summary")
    if not draft.root_causes:
        missing.append("root causes")
    if not draft.rollback_plan.strip():
        missing.append("rollback plan")
    if not draft.evaluation_plan.strip():
        missing.append("evaluation plan")
    if not draft.safety_controls:
        missing.append("safety controls")
    if not draft.action_items:
        missing.append("action items")
    return missing


def unresolved_actions(draft: PostmortemDraft) -> list[ActionItem]:
    return [item for item in draft.action_items if not item.done or not item.has_required_fields()]


def highest_severity(items: list[ActionItem], today: date) -> Severity | None:
    def is_active(item: ActionItem) -> bool:
        return item.has_required_fields() and (not item.done or item.is_overdue(today))

    active = [item for item in items if is_active(item)]
    if not active:
        return None

    def priority(item: ActionItem) -> tuple[int, str]:
        if item.is_overdue(today):
            return (0, item.title)
        urgent_types = {
            ActionType.IMMEDIATE_FIX,
            ActionType.SAFETY_GUARDRAIL,
            ActionType.ROLLBACK,
        }
        if item.action_type in urgent_types:
            return (1, item.title)
        return (2, item.title)

    return Severity(1) if any(priority(item)[0] == 0 for item in active) else Severity(2)

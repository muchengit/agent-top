"""L1 guardrail helper lab for local Agent safety boundaries."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RiskLevel(Enum):
    READ_ONLY = "read_only"
    WRITE = "write"
    DESTRUCTIVE = "destructive"


class ToolOutcome(Enum):
    ALLOWED = "allowed"
    CONFIRMATION_REQUIRED = "confirmation_required"
    BLOCKED = "blocked"


@dataclass(frozen=True)
class ToolPolicy:
    name: str
    risk_level: RiskLevel
    allowed_roles: tuple[str, ...]
    requires_confirmation: bool = False


@dataclass(frozen=True)
class ToolRequest:
    tool_name: str
    role: str
    user_confirmed: bool = False


def evaluate_tool_request(policy: ToolPolicy, request: ToolRequest) -> ToolOutcome:
    if policy.name != request.tool_name:
        return ToolOutcome.BLOCKED
    if request.role not in policy.allowed_roles:
        return ToolOutcome.BLOCKED
    if policy.risk_level == RiskLevel.DESTRUCTIVE and not request.user_confirmed:
        return ToolOutcome.CONFIRMATION_REQUIRED
    if policy.requires_confirmation and not request.user_confirmed:
        return ToolOutcome.CONFIRMATION_REQUIRED
    return ToolOutcome.ALLOWED

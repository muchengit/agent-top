"""L4 local guardrail simulation for Agent cost and stability."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RuntimeAction(Enum):
    CONTINUE = "continue"
    DEGRADE = "degrade"
    BLOCK = "block"


@dataclass(frozen=True)
class BudgetPolicy:
    max_steps: int
    max_tool_calls: int
    max_retries: int
    max_latency_ms: int
    max_tokens: int


@dataclass(frozen=True)
class RuntimeState:
    steps: int
    tool_calls: int
    retries: int
    latency_ms: int
    tokens_used: int
    next_call_tokens: int


@dataclass(frozen=True)
class GuardrailDecision:
    action: RuntimeAction
    reasons: tuple[str, ...]


def decide_guardrail(state: RuntimeState, policy: BudgetPolicy) -> GuardrailDecision:
    reasons: list[str] = []
    if state.steps >= policy.max_steps:
        reasons.append("step_budget_exhausted")
    if state.tool_calls >= policy.max_tool_calls:
        reasons.append("tool_call_budget_exhausted")
    if state.retries >= policy.max_retries:
        reasons.append("retry_budget_exhausted")
    if state.latency_ms >= policy.max_latency_ms:
        reasons.append("latency_budget_exhausted")
    if state.tokens_used + state.next_call_tokens > policy.max_tokens:
        reasons.append("token_budget_exhausted")
    if state.steps >= policy.max_steps:
        return GuardrailDecision(RuntimeAction.BLOCK, tuple(reasons))
    if state.retries >= policy.max_retries:
        return GuardrailDecision(RuntimeAction.BLOCK, tuple(reasons))
    if not reasons:
        return GuardrailDecision(RuntimeAction.CONTINUE, ())
    return GuardrailDecision(RuntimeAction.DEGRADE, tuple(reasons))


def degraded_response(
    decision: GuardrailDecision,
    *,
    fallback_summary: str,
    request_id: str,
) -> dict[str, object]:
    if decision.action is RuntimeAction.BLOCK:
        return {
            "request_id": request_id,
            "status": "blocked",
            "reasons": decision.reasons,
            "message": (
                "The Agent stopped before taking another action "
                "because a blocking budget was exhausted."
            ),
        }
    return {
        "request_id": request_id,
        "status": "degraded",
        "reasons": decision.reasons,
        "message": fallback_summary,
        "trace_required": True,
    }

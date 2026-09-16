"""L2 local router for cost and latency-aware Agent routing."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Route(Enum):
    SIMPLE_ANSWER = "simple_answer"
    RETRIEVAL = "retrieval"
    TOOL_CALL = "tool_call"
    ESCALATE = "escalate"


@dataclass(frozen=True)
class RequestProfile:
    needs_retrieval: bool
    needs_tool: bool
    needs_confirmation: bool
    user_confirmed: bool
    estimated_latency_ms: int
    latency_budget_ms: int


def route_request(profile: RequestProfile) -> Route:
    if profile.needs_confirmation and not profile.user_confirmed:
        return Route.ESCALATE
    if profile.estimated_latency_ms > profile.latency_budget_ms:
        return Route.ESCALATE
    if profile.needs_tool:
        return Route.TOOL_CALL
    if profile.needs_retrieval:
        return Route.RETRIEVAL
    return Route.SIMPLE_ANSWER

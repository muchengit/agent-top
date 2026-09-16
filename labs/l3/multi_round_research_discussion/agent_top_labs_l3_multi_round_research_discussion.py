"""L3 deterministic multi-round search and discussion workflow."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class DiscussionStatus(Enum):
    NEEDS_MORE_EVIDENCE = "needs_more_evidence"
    READY_TO_ANSWER = "ready_to_answer"
    SHOULD_ASK_USER = "should_ask_user"
    SHOULD_REFUSE = "should_refuse"


@dataclass(frozen=True)
class CandidateSource:
    name: str
    relevance_score: float
    freshness_score: float
    trust_score: float
    contains_answer: bool


@dataclass(frozen=True)
class ResearchState:
    question: str
    selected_sources: tuple[str, ...]
    rounds_used: int
    clarified_with_user: bool


def candidate_priority(source: CandidateSource) -> float:
    """Higher is better; sources must contain relevant evidence."""
    if not source.contains_answer:
        return -1.0
    return source.relevance_score * 0.5 + source.freshness_score * 0.3 + source.trust_score * 0.2


def select_sources(sources: list[CandidateSource], max_sources: int = 3) -> list[CandidateSource]:
    return sorted(
        sources,
        key=lambda source: (candidate_priority(source), source.name),
        reverse=True,
    )[:max_sources]


def evaluate_discussion(
    state: ResearchState,
    selected_sources: list[CandidateSource],
    requires_clarification: bool = False,
) -> DiscussionStatus:
    if not state.question.strip():
        return DiscussionStatus.SHOULD_ASK_USER
    if requires_clarification and not state.clarified_with_user:
        return DiscussionStatus.SHOULD_ASK_USER
    evidence_sources = [source for source in selected_sources if source.contains_answer]
    if not evidence_sources:
        return DiscussionStatus.SHOULD_REFUSE
    if any(source.freshness_score < 0.5 for source in evidence_sources):
        return DiscussionStatus.NEEDS_MORE_EVIDENCE
    return DiscussionStatus.READY_TO_ANSWER

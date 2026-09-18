"""L4 deterministic trace integrity validation for production observability."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class EventType(Enum):
    """Supported trace event types."""

    PROMPT = "prompt"
    TOOL_CALL = "tool_call"
    DECISION = "decision"
    RESULT = "result"


@dataclass(frozen=True)
class TraceEvent:
    """A single observability event inside a trace."""

    event_id: str
    trace_id: str
    timestamp: int
    event_type: EventType
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class TraceIssue:
    """A single integrity problem found by the validator."""

    trace_id: str
    event_id: str
    problem_type: str
    suggestion: str


@dataclass(frozen=True)
class TraceIntegrityReport:
    """Aggregated results of validating an event stream."""

    total_traces: int
    complete_traces: int
    broken_traces: int
    issues: list[TraceIssue] = field(default_factory=list)


class TraceIntegrityValidator:
    """Deterministic validator for production trace event streams."""

    REQUIRED_FIELDS: dict[EventType, tuple[str, ...]] = {
        EventType.PROMPT: ("content",),
        EventType.TOOL_CALL: ("tool", "arguments"),
        EventType.DECISION: ("choice",),
        EventType.RESULT: ("content",),
    }

    def group_by_trace(self, events: Sequence[TraceEvent]) -> dict[str, list[TraceEvent]]:
        """Group events by trace id, preserving stream order inside each group.

        Events without a trace id are returned under the empty-string key.
        """
        groups: dict[str, list[TraceEvent]] = {}
        for event in events:
            groups.setdefault(event.trace_id, []).append(event)
        return groups

    def validate(self, events: Sequence[TraceEvent]) -> TraceIntegrityReport:
        """Validate an event stream and return a deterministic integrity report."""
        issues: list[TraceIssue] = []
        groups = self.group_by_trace(events)
        trace_ids = [trace_id for trace_id in groups if trace_id]
        broken: set[str] = set()
        for trace_id in sorted(trace_ids):
            trace_issues = self._validate_trace(trace_id, groups[trace_id])
            if trace_issues:
                broken.add(trace_id)
            issues.extend(trace_issues)
        orphan_issues = [
            TraceIssue(
                trace_id="",
                event_id=event.event_id,
                problem_type="missing_trace_id",
                suggestion="attach the event to a valid trace_id or drop it before ingest",
            )
            for event in groups.get("", [])
        ]
        issues.extend(sorted(orphan_issues, key=lambda issue: issue.event_id))
        total = len(trace_ids)
        return TraceIntegrityReport(
            total_traces=total,
            complete_traces=total - len(broken),
            broken_traces=len(broken),
            issues=issues,
        )

    def _validate_trace(self, trace_id: str, events: list[TraceEvent]) -> list[TraceIssue]:
        """Validate a single trace group and return its issues in stream order."""
        issues: list[TraceIssue] = []
        first_event_id = events[0].event_id if events else ""
        has_prompt = any(event.event_type == EventType.PROMPT for event in events)
        has_result = any(event.event_type == EventType.RESULT for event in events)
        if not has_prompt:
            issues.append(
                TraceIssue(
                    trace_id=trace_id,
                    event_id=first_event_id,
                    problem_type="missing_prompt_event",
                    suggestion=(
                        "start each trace with a prompt event before any tool_call"
                        " or decision events"
                    ),
                )
            )
        if not has_result:
            issues.append(
                TraceIssue(
                    trace_id=trace_id,
                    event_id=first_event_id,
                    problem_type="missing_result_event",
                    suggestion="end each trace with a result event",
                )
            )
        previous_timestamp: int | None = None
        for event in events:
            if previous_timestamp is not None and event.timestamp < previous_timestamp:
                issues.append(
                    TraceIssue(
                        trace_id=trace_id,
                        event_id=event.event_id,
                        problem_type="out_of_order_timestamp",
                        suggestion=(
                        "re-emit or sort the event so timestamps do not decrease"
                        " within a trace"
                    ),
                    )
                )
            previous_timestamp = event.timestamp
            missing = [
                field_name
                for field_name in self.REQUIRED_FIELDS.get(event.event_type, ())
                if field_name not in event.payload
            ]
            if missing:
                issues.append(
                    TraceIssue(
                        trace_id=trace_id,
                        event_id=event.event_id,
                        problem_type="missing_required_field",
                        suggestion=(
                        f"add required field(s): {', '.join(missing)}"
                        f" to the {event.event_type.value} event payload"
                    ),
                    )
                )
        return issues


def validate_trace_integrity(events: Sequence[TraceEvent]) -> TraceIntegrityReport:
    """Validate an event stream using a fresh validator instance."""
    return TraceIntegrityValidator().validate(events)

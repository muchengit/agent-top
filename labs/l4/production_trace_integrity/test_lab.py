"""Deterministic tests for the L4 trace integrity lab."""

from __future__ import annotations

import unittest

from .agent_top_labs_l4_production_trace_integrity import (
    EventType,
    TraceEvent,
    TraceIntegrityValidator,
    validate_trace_integrity,
)


def make_event(
    event_id: str,
    trace_id: str,
    timestamp: int,
    event_type: EventType,
    payload: dict[str, object] | None = None,
) -> TraceEvent:
    """Build a trace event with an optional payload."""
    return TraceEvent(event_id, trace_id, timestamp, event_type, payload or {})


def full_trace() -> list[TraceEvent]:
    """Return a structurally complete trace."""
    return [
        make_event("e1", "trace-1", 1000, EventType.PROMPT, {"content": "summarize"}),
        make_event(
            "e2",
            "trace-1",
            1100,
            EventType.TOOL_CALL,
            {"tool": "search", "arguments": {"q": "sales"}},
        ),
        make_event("e3", "trace-1", 1200, EventType.DECISION, {"choice": "use_first_result"}),
        make_event("e4", "trace-1", 1300, EventType.RESULT, {"content": "done"}),
    ]


class TraceIntegrityTest(unittest.TestCase):
    def test_complete_trace_passes(self) -> None:
        report = TraceIntegrityValidator().validate(full_trace())
        self.assertEqual(report.total_traces, 1)
        self.assertEqual(report.complete_traces, 1)
        self.assertEqual(report.broken_traces, 0)
        self.assertEqual(report.issues, [])

    def test_missing_result_event(self) -> None:
        report = validate_trace_integrity(full_trace()[:-1])
        self.assertEqual(len(report.issues), 1)
        issue = report.issues[0]
        self.assertEqual(issue.trace_id, "trace-1")
        self.assertEqual(issue.problem_type, "missing_result_event")
        self.assertEqual(report.broken_traces, 1)
        self.assertEqual(report.complete_traces, 0)

    def test_missing_prompt_event(self) -> None:
        report = validate_trace_integrity(full_trace()[1:])
        self.assertEqual(len(report.issues), 1)
        self.assertEqual(report.issues[0].problem_type, "missing_prompt_event")
        self.assertEqual(report.broken_traces, 1)

    def test_out_of_order_timestamp(self) -> None:
        events = [
            make_event("e1", "trace-1", 1000, EventType.PROMPT, {"content": "x"}),
            make_event("e2", "trace-1", 900, EventType.TOOL_CALL, {"tool": "t", "arguments": {}}),
            make_event("e3", "trace-1", 1000, EventType.RESULT, {"content": "y"}),
        ]
        report = validate_trace_integrity(events)
        issues = [i for i in report.issues if i.problem_type == "out_of_order_timestamp"]
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].event_id, "e2")
        self.assertEqual(report.broken_traces, 1)

    def test_orphan_event_without_trace_id(self) -> None:
        report = validate_trace_integrity(
            [make_event("e9", "", 1000, EventType.PROMPT, {"content": "x"})]
        )
        self.assertEqual(report.total_traces, 0)
        self.assertEqual(len(report.issues), 1)
        self.assertEqual(report.issues[0].trace_id, "")
        self.assertEqual(report.issues[0].event_id, "e9")
        self.assertEqual(report.issues[0].problem_type, "missing_trace_id")

    def test_tool_call_missing_required_fields(self) -> None:
        events = [
            make_event("e1", "trace-1", 1000, EventType.PROMPT, {"content": "x"}),
            make_event("e2", "trace-1", 1100, EventType.TOOL_CALL, {}),
            make_event("e3", "trace-1", 1200, EventType.RESULT, {"content": "y"}),
        ]
        report = validate_trace_integrity(events)
        issues = [i for i in report.issues if i.problem_type == "missing_required_field"]
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].event_id, "e2")
        self.assertIn("tool", issues[0].suggestion)
        self.assertIn("arguments", issues[0].suggestion)

    def test_mixed_traces_multiple_groups(self) -> None:
        events = full_trace() + [
            make_event("a1", "trace-2", 2000, EventType.PROMPT, {"content": "q"}),
            make_event(
                "a2",
                "trace-2",
                2100,
                EventType.TOOL_CALL,
                {"tool": "calc", "arguments": {"expr": "1+1"}},
            ),
        ]
        report = validate_trace_integrity(events)
        self.assertEqual(report.total_traces, 2)
        self.assertEqual(report.complete_traces, 1)
        self.assertEqual(report.broken_traces, 1)
        self.assertEqual(len(report.issues), 1)
        self.assertEqual(report.issues[0].trace_id, "trace-2")

    def test_empty_input(self) -> None:
        report = validate_trace_integrity([])
        self.assertEqual(report.total_traces, 0)
        self.assertEqual(report.complete_traces, 0)
        self.assertEqual(report.broken_traces, 0)
        self.assertEqual(report.issues, [])

    def test_report_statistics_correct(self) -> None:
        events = [
            make_event("t1", "trace-1", 3000, EventType.PROMPT, {"content": "a"}),
            make_event("t2", "trace-1", 3100, EventType.RESULT, {"content": "b"}),
            make_event("t3", "trace-2", 3000, EventType.PROMPT, {"content": "c"}),
            make_event("t4", "trace-3", 3000, EventType.PROMPT, {"content": "d"}),
            make_event("t5", "trace-3", 2500, EventType.TOOL_CALL, {"tool": "t", "arguments": {}}),
            make_event("t6", "trace-3", 3100, EventType.RESULT, {"content": "e"}),
        ]
        report = validate_trace_integrity(events)
        self.assertEqual(report.total_traces, 3)
        self.assertEqual(report.complete_traces, 1)
        self.assertEqual(report.broken_traces, 2)
        self.assertEqual(len(report.issues), 2)

    def test_group_by_trace(self) -> None:
        groups = TraceIntegrityValidator().group_by_trace(full_trace())
        self.assertEqual(list(groups.keys()), ["trace-1"])
        self.assertEqual(len(groups["trace-1"]), 4)


if __name__ == "__main__":
    unittest.main()

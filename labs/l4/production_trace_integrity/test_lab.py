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

    def test_missing_required_field_prompt(self) -> None:
        events = [
            make_event("e1", "trace-1", 1000, EventType.PROMPT, {}),
            make_event("e2", "trace-1", 1100, EventType.RESULT, {"content": "y"}),
        ]
        report = validate_trace_integrity(events)
        issues = [i for i in report.issues if i.problem_type == "missing_required_field"]
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].event_id, "e1")
        self.assertIn("content", issues[0].suggestion)

    def test_missing_required_field_decision(self) -> None:
        events = [
            make_event("e1", "trace-1", 1000, EventType.PROMPT, {"content": "q"}),
            make_event("e2", "trace-1", 1100, EventType.DECISION, {}),
            make_event("e3", "trace-1", 1200, EventType.RESULT, {"content": "y"}),
        ]
        report = validate_trace_integrity(events)
        issues = [i for i in report.issues if i.problem_type == "missing_required_field"]
        self.assertEqual(len(issues), 1)
        self.assertIn("choice", issues[0].suggestion)

    def test_multiple_issues_same_trace_collected(self) -> None:
        events = [
            make_event("e1", "trace-1", 2000, EventType.PROMPT, {"content": "q"}),
            make_event("e2", "trace-1", 1900, EventType.TOOL_CALL, {"tool": "t"}),
        ]
        report = validate_trace_integrity(events)
        self.assertEqual(report.broken_traces, 1)
        problem_types = {issue.problem_type for issue in report.issues}
        self.assertIn("missing_result_event", problem_types)
        self.assertIn("out_of_order_timestamp", problem_types)
        self.assertIn("missing_required_field", problem_types)

    def test_group_by_trace_multiple_ids(self) -> None:
        events = [
            make_event("a", "trace-1", 1000, EventType.PROMPT, {"content": "x"}),
            make_event("b", "trace-2", 1000, EventType.PROMPT, {"content": "y"}),
            make_event("c", "trace-1", 1100, EventType.RESULT, {"content": "z"}),
        ]
        groups = TraceIntegrityValidator().group_by_trace(events)
        self.assertEqual(set(groups), {"trace-1", "trace-2"})
        self.assertEqual(len(groups["trace-1"]), 2)

    def test_equal_timestamp_is_not_out_of_order(self) -> None:
        events = [
            make_event("e1", "trace-1", 1000, EventType.PROMPT, {"content": "x"}),
            make_event("e2", "trace-1", 1000, EventType.RESULT, {"content": "y"}),
        ]
        report = validate_trace_integrity(events)
        self.assertNotIn(
            "out_of_order_timestamp",
            [i.problem_type for i in report.issues],
        )

    def test_orphan_events_sorted_by_event_id(self) -> None:
        events = [
            make_event("b9", "", 1000, EventType.PROMPT, {"content": "x"}),
            make_event("a1", "", 1000, EventType.PROMPT, {"content": "y"}),
        ]
        report = validate_trace_integrity(events)
        issues = [i for i in report.issues if i.problem_type == "missing_trace_id"]
        self.assertEqual([i.event_id for i in issues], ["a1", "b9"])

    def test_prompt_present_anywhere_in_trace_counts(self) -> None:
        events = [
            make_event("e1", "trace-1", 1000, EventType.RESULT, {"content": "first"}),
            make_event("e2", "trace-1", 1100, EventType.PROMPT, {"content": "late"}),
        ]
        report = validate_trace_integrity(events)
        self.assertNotIn(
            "missing_prompt_event",
            [i.problem_type for i in report.issues],
        )
        self.assertNotIn(
            "missing_result_event",
            [i.problem_type for i in report.issues],
        )

    def test_trace_event_default_payload_is_empty(self) -> None:
        event = make_event("e1", "trace-1", 1000, EventType.PROMPT)
        self.assertEqual(event.payload, {})

    def test_issue_dataclass_fields(self) -> None:
        from .agent_top_labs_l4_production_trace_integrity import TraceIssue

        issue = TraceIssue("trace-1", "e1", "missing_prompt_event", "suggestion")
        self.assertEqual(issue.trace_id, "trace-1")
        self.assertEqual(issue.event_id, "e1")
        self.assertEqual(issue.problem_type, "missing_prompt_event")
        self.assertEqual(issue.suggestion, "suggestion")


if __name__ == "__main__":
    unittest.main()

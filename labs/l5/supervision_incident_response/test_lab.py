"""Deterministic tests for the L5 supervision and incident response lab."""

from __future__ import annotations

import unittest

from .agent_top_labs_l5_supervision_incident_response import (
    ACTION_CONTINUE,
    ACTION_ESCALATE,
    ACTION_PAUSE,
    ACTION_ROLLBACK,
    SEVERITY_CRITICAL,
    SEVERITY_WARNING,
    STATUS_OPEN,
    STATUS_RESOLVED,
    Incident,
    SupervisionGate,
    WorkerHeartbeat,
)

HEALTHY = WorkerHeartbeat(
    worker_id="worker-a",
    status="healthy",
    last_task="classify-request",
)

OPEN_CRITICAL = Incident(
    incident_id="inc-1",
    severity=SEVERITY_CRITICAL,
    source_worker="worker-a",
    affected_traces=("trace_1", "trace_2"),
    signal="refusal-loop",
    status=STATUS_OPEN,
)


class SupervisionGateTest(unittest.TestCase):
    def test_healthy_fleet_continues(self) -> None:
        report = SupervisionGate().evaluate((HEALTHY,), ())
        self.assertEqual(report.decision, ACTION_CONTINUE)
        self.assertEqual(report.open_incidents, ())
        self.assertEqual(report.actions, ())

    def test_two_critical_incidents_trigger_rollback(self) -> None:
        second = Incident(
            incident_id="inc-2",
            severity=SEVERITY_CRITICAL,
            source_worker="worker-b",
            affected_traces=("trace_3",),
            signal="cost-blowout",
            status=STATUS_OPEN,
        )
        report = SupervisionGate(max_open_critical=1).evaluate(
            (HEALTHY,), (OPEN_CRITICAL, second)
        )
        self.assertEqual(report.decision, ACTION_ROLLBACK)
        self.assertTrue(
            any(item.action == "rollback last release" for item in report.actions)
        )

    def test_resolved_incident_is_not_open(self) -> None:
        resolved = Incident(
            incident_id="inc-1",
            severity=SEVERITY_CRITICAL,
            source_worker="worker-a",
            affected_traces=("trace_1",),
            signal="refusal-loop",
            status=STATUS_RESOLVED,
        )
        report = SupervisionGate().evaluate((HEALTHY,), (resolved,))
        self.assertEqual(report.open_incidents, ())
        self.assertEqual(report.decision, ACTION_CONTINUE)

    def test_unhealthy_worker_escalates_and_creates_action(self) -> None:
        dead = WorkerHeartbeat(
            worker_id="worker-b",
            status="dead",
            last_task="search-vector-index",
            error="OOM after retry",
        )
        report = SupervisionGate().evaluate((HEALTHY, dead), ())
        self.assertEqual(report.decision, ACTION_ESCALATE)
        self.assertTrue(
            any(item.owner == "worker-b" and "restart" in item.action
                for item in report.actions)
        )

    def test_too_many_warnings_pause_fan_out(self) -> None:
        warnings = tuple(
            Incident(
                incident_id=f"warn-{i}",
                severity=SEVERITY_WARNING,
                source_worker="worker-a",
                affected_traces=(f"trace_{i}",),
                signal="slow-tool",
                status=STATUS_OPEN,
            )
            for i in range(4)
        )
        report = SupervisionGate(max_open_warnings=3).evaluate(
            (HEALTHY,), warnings
        )
        self.assertEqual(report.decision, ACTION_PAUSE)
        self.assertIn("pause new fan-out", {a.action for a in report.actions})

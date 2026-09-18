"""Deterministic tests for the L5 supervision and incident response lab."""

from __future__ import annotations

import unittest

from .agent_top_labs_l5_supervision_incident_response import (
    ACTION_CONTINUE,
    ACTION_ESCALATE,
    ACTION_PAUSE,
    ACTION_ROLLBACK,
    SEVERITY_CRITICAL,
    SEVERITY_INFO,
    SEVERITY_WARNING,
    STATUS_CONTAINED,
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

    def test_critical_at_exact_limit_does_not_rollback(self) -> None:
        report = SupervisionGate(max_open_critical=1).evaluate(
            (HEALTHY,), (OPEN_CRITICAL,)
        )
        self.assertEqual(report.decision, ACTION_CONTINUE)

    def test_warnings_at_exact_limit_do_not_pause(self) -> None:
        warnings = tuple(
            Incident(
                incident_id=f"warn-{i}",
                severity=SEVERITY_WARNING,
                source_worker="worker-a",
                affected_traces=(f"trace_{i}",),
                signal="slow-tool",
                status=STATUS_OPEN,
            )
            for i in range(3)
        )
        report = SupervisionGate(max_open_warnings=3).evaluate((HEALTHY,), warnings)
        self.assertEqual(report.decision, ACTION_CONTINUE)

    def test_critical_open_incident_adds_contain_action(self) -> None:
        report = SupervisionGate().evaluate((HEALTHY,), (OPEN_CRITICAL,))
        self.assertTrue(
            any(
                item.owner == "incident-commander"
                and item.target == "inc-1"
                and item.action == "contain critical incident"
                for item in report.actions
            )
        )

    def test_resolved_critical_does_not_trigger_rollback_or_contain(self) -> None:
        resolved = Incident(
            incident_id="inc-1",
            severity=SEVERITY_CRITICAL,
            source_worker="worker-a",
            affected_traces=("trace_1",),
            signal="refusal-loop",
            status=STATUS_RESOLVED,
        )
        report = SupervisionGate().evaluate((HEALTHY,), (resolved,))
        self.assertEqual(report.decision, ACTION_CONTINUE)
        self.assertEqual(report.actions, ())

    def test_precedence_rollback_beats_pause(self) -> None:
        critical = Incident(
            incident_id="inc-9",
            severity=SEVERITY_CRITICAL,
            source_worker="worker-a",
            affected_traces=("t1",),
            signal="refusal-loop",
            status=STATUS_OPEN,
        )
        critical2 = Incident(
            incident_id="inc-10",
            severity=SEVERITY_CRITICAL,
            source_worker="worker-b",
            affected_traces=("t2",),
            signal="cost-blowout",
            status=STATUS_OPEN,
        )
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
        report = SupervisionGate().evaluate((HEALTHY,), (critical, critical2) + warnings)
        self.assertEqual(report.decision, ACTION_ROLLBACK)

    def test_dead_worker_with_critical_at_limit_escalates(self) -> None:
        dead = WorkerHeartbeat(
            worker_id="worker-b",
            status="dead",
            last_task="search-vector-index",
            error="OOM after retry",
        )
        report = SupervisionGate().evaluate((HEALTHY, dead), (OPEN_CRITICAL,))
        self.assertEqual(report.decision, ACTION_ESCALATE)

    def test_contained_incident_is_still_open(self) -> None:
        contained = Incident(
            incident_id="inc-1",
            severity=SEVERITY_WARNING,
            source_worker="worker-a",
            affected_traces=("trace_1",),
            signal="slow-tool",
            status=STATUS_CONTAINED,
        )
        report = SupervisionGate().evaluate((HEALTHY,), (contained,))
        self.assertEqual(report.open_incidents, ("inc-1",))

    def test_info_incident_is_not_critical_or_warning(self) -> None:
        info = Incident(
            incident_id="info-1",
            severity=SEVERITY_INFO,
            source_worker="worker-a",
            affected_traces=("trace_1",),
            signal="telemetry",
            status=STATUS_OPEN,
        )
        report = SupervisionGate().evaluate((HEALTHY,), (info,))
        self.assertEqual(report.decision, ACTION_CONTINUE)

    def test_summary_counts_everything(self) -> None:
        dead = WorkerHeartbeat(
            worker_id="worker-b",
            status="dead",
            last_task="x",
            error="boom",
        )
        report = SupervisionGate().evaluate((HEALTHY, dead), (OPEN_CRITICAL,))
        self.assertEqual(
            report.summary,
            "1 open incident(s), 1 critical, 0 warning, 1 unhealthy worker(s)",
        )

    def test_multiple_dead_workers_get_actions(self) -> None:
        dead_a = WorkerHeartbeat("worker-a", "dead", "t1", "e1")
        dead_b = WorkerHeartbeat("worker-b", "dead", "t2", "e2")
        report = SupervisionGate().evaluate((dead_a, dead_b), ())
        self.assertEqual(report.decision, ACTION_ESCALATE)
        owners = {item.owner for item in report.actions}
        self.assertEqual(owners, {"worker-a", "worker-b"})

    def test_empty_fleet_and_no_incidents_continues(self) -> None:
        report = SupervisionGate().evaluate((), ())
        self.assertEqual(report.decision, ACTION_CONTINUE)
        self.assertEqual(report.open_incidents, ())
        self.assertEqual(report.actions, ())
        self.assertEqual(
            report.summary,
            "0 open incident(s), 0 critical, 0 warning, 0 unhealthy worker(s)",
        )

    def test_critical_threshold_zero_blocks_any_critical(self) -> None:
        report = SupervisionGate(max_open_critical=0).evaluate(
            (HEALTHY,), (OPEN_CRITICAL,)
        )
        self.assertEqual(report.decision, ACTION_ROLLBACK)

    def test_critical_incident_with_resolved_status_still_counts_for_rollback(self) -> None:
        resolved = Incident(
            incident_id="inc-1",
            severity=SEVERITY_CRITICAL,
            source_worker="worker-a",
            affected_traces=("trace_1",),
            signal="refusal-loop",
            status=STATUS_RESOLVED,
        )
        resolved2 = Incident(
            incident_id="inc-2",
            severity=SEVERITY_CRITICAL,
            source_worker="worker-b",
            affected_traces=("trace_2",),
            signal="refusal-loop",
            status=STATUS_RESOLVED,
        )
        report = SupervisionGate().evaluate((HEALTHY,), (resolved, resolved2))
        self.assertEqual(report.decision, ACTION_ROLLBACK)

    def test_rollback_and_contain_actions_are_both_present(self) -> None:
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
        actions = {a.action for a in report.actions}
        self.assertIn("rollback last release", actions)
        self.assertIn("contain critical incident", actions)
        rollback_notes = {a.rollback for a in report.actions}
        self.assertIn("notify stakeholders", rollback_notes)

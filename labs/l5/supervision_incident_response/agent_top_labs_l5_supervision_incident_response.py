"""L5 deterministic supervision and incident response for multi-agent production.

This lab models a lightweight production supervisor: it aggregates worker
heartbeats and incident reports, decides whether an incident is contained,
and produces an action plan with owners and rollback targets. Everything is
deterministic and requires no network or API keys.
"""

from __future__ import annotations

from dataclasses import dataclass

SEVERITY_INFO = "info"
SEVERITY_WARNING = "warning"
SEVERITY_CRITICAL = "critical"

STATUS_OPEN = "open"
STATUS_CONTAINED = "contained"
STATUS_RESOLVED = "resolved"

ACTION_CONTINUE = "continue"
ACTION_ESCALATE = "escalate"
ACTION_PAUSE = "pause"
ACTION_ROLLBACK = "rollback"


@dataclass(frozen=True)
class WorkerHeartbeat:
    worker_id: str
    status: str
    last_task: str
    error: str | None = None


@dataclass(frozen=True)
class Incident:
    incident_id: str
    severity: str
    source_worker: str
    affected_traces: tuple[str, ...]
    signal: str
    status: str = STATUS_OPEN


@dataclass(frozen=True)
class ActionItem:
    owner: str
    action: str
    target: str
    rollback: str


@dataclass(frozen=True)
class SupervisionReport:
    decision: str
    open_incidents: tuple[str, ...]
    actions: tuple[ActionItem, ...]
    summary: str


class SupervisionGate:
    """Deterministic supervision rules for a worker fleet."""

    def __init__(
        self,
        max_open_critical: int = 1,
        max_open_warnings: int = 3,
    ) -> None:
        self.max_open_critical = max_open_critical
        self.max_open_warnings = max_open_warnings

    def evaluate(
        self,
        heartbeats: tuple[WorkerHeartbeat, ...],
        incidents: tuple[Incident, ...],
    ) -> SupervisionReport:
        open_incidents = tuple(
            inc.incident_id for inc in incidents if inc.status != STATUS_RESOLVED
        )
        critical = sum(
            1 for inc in incidents if inc.severity == SEVERITY_CRITICAL
        )
        warnings = sum(
            1 for inc in incidents if inc.severity == SEVERITY_WARNING
        )
        dead_workers = tuple(
            hb.worker_id for hb in heartbeats if hb.status != "healthy"
        )

        actions: list[ActionItem] = []
        if critical > self.max_open_critical:
            decision = ACTION_ROLLBACK
            actions.append(
                ActionItem(
                    owner="platform-oncall",
                    action="rollback last release",
                    target="affected traces",
                    rollback="re-apply previous release",
                )
            )
        elif warnings > self.max_open_warnings:
            decision = ACTION_PAUSE
            actions.append(
                ActionItem(
                    owner="platform-oncall",
                    action="pause new fan-out",
                    target="scheduler queue",
                    rollback="resume after triage",
                )
            )
        elif dead_workers:
            decision = ACTION_ESCALATE
            actions.extend(
                ActionItem(
                    owner=worker,
                    action="restart worker and replay checkpoint",
                    target="worker runtime",
                    rollback="keep worker paused",
                )
                for worker in dead_workers
            )
        else:
            decision = ACTION_CONTINUE

        for inc in incidents:
            if inc.severity == SEVERITY_CRITICAL and inc.status == STATUS_OPEN:
                actions.append(
                    ActionItem(
                        owner="incident-commander",
                        action="contain critical incident",
                        target=inc.incident_id,
                        rollback="notify stakeholders",
                    )
                )

        summary = (
            f"{len(open_incidents)} open incident(s), "
            f"{critical} critical, {warnings} warning, "
            f"{len(dead_workers)} unhealthy worker(s)"
        )
        return SupervisionReport(
            decision=decision,
            open_incidents=open_incidents,
            actions=tuple(actions),
            summary=summary,
        )

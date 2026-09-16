"""L3 deterministic multi-agent supervisor router."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class AgentName(Enum):
    RESEARCH = "research"
    TOOL = "tool"
    VERIFIER = "verifier"
    HUMAN = "human"


@dataclass(frozen=True)
class TaskProfile:
    needs_retrieval: bool
    needs_tool: bool
    needs_verification: bool
    needs_confirmation: bool
    user_confirmed: bool


def assign_agents(task: TaskProfile) -> tuple[AgentName, ...]:
    """Assign the smallest useful set of agents for a task."""
    agents: list[AgentName] = []
    if task.needs_retrieval:
        agents.append(AgentName.RESEARCH)
    if task.needs_tool:
        if task.needs_confirmation and not task.user_confirmed:
            agents.append(AgentName.HUMAN)
        agents.append(AgentName.TOOL)
    if task.needs_verification:
        agents.append(AgentName.VERIFIER)
    return tuple(agents)


def supervisor_decision(task: TaskProfile) -> AgentName:
    """Return the first agent that should act next."""
    agents = assign_agents(task)
    if not agents:
        return AgentName.RESEARCH
    return agents[0]

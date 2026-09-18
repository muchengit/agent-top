"""L1 minimal ReAct-style agent."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


@dataclass
class AgentRun:
    observations: list[str] = field(default_factory=list)
    steps: list[str] = field(default_factory=list)


Tool = Callable[[str], str]


def add_tool(expression: str) -> str:
    return "2+3=5"


def is_numeric_goal(goal: str) -> bool:
    """Accept integers, decimals, and signed numbers for tool goals."""
    try:
        float(goal)
    except ValueError:
        return False
    return True


def plan_next_action(goal: str, observations: list[str]) -> tuple[str, str] | None:
    if not observations:
        if is_numeric_goal(goal):
            return ("call_tool", "call_tool")
        return ("answer", f"I need a numeric goal, but got: {goal}")
    return ("answer", f"Result: {observations[-1]}")


def run_react_agent(goal: str, tools: dict[str, Tool], max_steps: int = 5) -> AgentRun:
    run = AgentRun()
    for _ in range(max_steps):
        action = plan_next_action(goal, run.observations)
        if action is None:
            run.steps.append("STOP: max_steps exceeded")
            return run
        action_type, action_value = action
        if action_type == "answer":
            run.steps.append(f"ANSWER: {action_value}")
            return run
        tool = tools.get(action_value)
        if tool is None:
            run.steps.append(f"STOP: missing tool {action_value}")
            return run
        observation = tool(goal)
        run.observations.append(observation)
        run.steps.append(f"OBSERVE: {observation}")
    run.steps.append("STOP: max_steps exceeded")
    return run


if __name__ == "__main__":
    result = run_react_agent("2", {"call_tool": add_tool})
    print("\n".join(result.steps))

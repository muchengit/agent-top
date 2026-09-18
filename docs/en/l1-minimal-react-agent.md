---
title: L1 Minimal ReAct Agent
validated_date: 2026-09-18
tested_against: "python 3.10+"
i18n-key: l1-minimal-react-agent
last-synced: 2026-09-18
---

# L1 Minimal ReAct Agent

## Goal

Build a tiny ReAct-style Agent loop from first principles, without using an Agent framework.

## Prerequisites

- L0 completed
- Comfort with Python functions, loops, and simple control flow
- No API key required

## What Is ReAct?

ReAct means the Agent alternates between reasoning and acting.

A minimal loop looks like this:

1. Observe the current state.
2. Think about the next step.
3. Call a tool if needed.
4. Observe the tool output.
5. Repeat until the Agent can answer or must stop.

This tutorial deliberately uses a simple deterministic plan instead of a real LLM. The goal is to understand the control flow first.

## The Core Idea

An Agent needs four pieces:

- **Goal**: what the user wants.
- **Observation**: what the Agent has seen so far.
- **Tool**: an action that returns more information.
- **Stop condition**: a way to end the loop safely.

## Minimal Implementation

Here is the shape of the Lab code:

```python
from dataclasses import dataclass, field
from typing import Callable

Tool = Callable[[str], str]

@dataclass
class AgentRun:
    observations: list[str] = field(default_factory=list)
    steps: list[str] = field(default_factory=list)

def add_tool(expression: str) -> str:
    return "2+3=5"

def plan_next_action(goal: str, observations: list[str]) -> tuple[str, str] | None:
    if not observations:
        if goal.isdigit():
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
```

## Step-by-Step Walkthrough

### 1. Run the Lab directly

```bash
python -m labs.l1.minimal_react_agent.agent_top_labs_l1_minimal_react_agent
```

Expected output:

```text
OBSERVE: 2+3=5
ANSWER: Result: 2+3=5
```

### 2. Run a numeric goal through the loop

```bash
python - <<'PY'
from labs.l1.minimal_react_agent.agent_top_labs_l1_minimal_react_agent import run_react_agent, add_tool
result = run_react_agent("5", {"call_tool": add_tool})
print(result.steps)
print(result.observations)
PY
```

Expected output:

```text
['OBSERVE: 2+3=5', 'ANSWER: Result: 2+3=5']
['2+3=5']
```

What happened:

1. The Agent saw no observations yet.
2. It planned to call a tool because the goal was numeric.
3. It called `add_tool`.
4. It observed `2+3=5`.
5. It produced the final answer.

### 3. Run a non-numeric goal

```bash
python - <<'PY'
from labs.l1.minimal_react_agent.agent_top_labs_l1_minimal_react_agent import run_react_agent, add_tool
result = run_react_agent("hello", {"call_tool": add_tool})
print(result.steps)
PY
```

Expected output:

```text
['ANSWER: I need a numeric goal, but got: hello']
```

This demonstrates a stop condition. The Agent does not loop forever when the input is not suitable for the tool.

### 4. Run the tests

```bash
python -m unittest labs.l1.minimal_react_agent.test_lab
```

Expected result:

```text
Ran 3 tests in 0.00Xs

OK
```

## Why `max_steps` Matters

Without `max_steps`, an Agent can loop forever if:

- the model keeps requesting the same tool;
- tool output is malformed;
- the planner never recognizes an answer state;
- a tool keeps returning the same observation.

A maximum step count is a simple production guardrail.

## What a Real Agent Adds

A real Agent would replace `plan_next_action()` with a model call. But even then, you still need:

- structured tool calls;
- tool result validation;
- stop conditions;
- error handling;
- logging or traces;
- cost and latency limits.

## Debugging Questions

If the Agent behaves unexpectedly, ask:

- Did the planner choose the right action?
- Did the tool return what the planner expected?
- Did the Agent observe the tool output?
- Did the stop condition trigger?
- Was the tool missing from the tool map?

## Common Mistakes

- No stop condition.
- Treating tool output as trustworthy without checking it.
- Mixing observation, planning, and execution into one opaque step.
- Ignoring missing tools.
- Letting the loop run past a safe maximum.

## Self-Check

1. What are the four pieces of a minimal Agent?
2. Why does `max_steps` matter?
3. What happens when a tool is missing?
4. What should happen when tool output is malformed?
5. How would you convert this fake planner into a real model-backed planner?

## Related Lab

Read the Lab README: [`../../labs/l1/minimal_react_agent/README.md`](../../labs/l1/minimal_react_agent/README.md).

Run the Lab tests:

```bash
python -m unittest labs.l1.minimal_react_agent.test_lab
```

## Next Step

Continue with [`L2 Single Agent with MCP`](l2-single-agent-mcp.md) to add a clearer tool boundary.

## Interview Questions

Reinforce L1 concepts with the component question bank: [`L1 Component Questions`](interviews/questions/l1-components.md).

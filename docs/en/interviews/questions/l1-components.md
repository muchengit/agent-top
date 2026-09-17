---
title: L1 Component Questions
validated_date: 2026-09-17
i18n-key: interviews-questions-l1-components
last-synced: 2026-09-17
---

# L1 Component Questions

These questions check whether the candidate can turn the four-component mental model (perception, planning, tools, memory) into working loops, schemas, and stop conditions.

## Question Bank

Four question types are covered: concept, implementation, debugging, and design.

### Concept

#### 1. Explain the four core Agent components.

**Answer points:**

- Perception turns input, tools, and observations into context.
- Planning decides what to try next.
- Tool use executes external actions.
- Memory preserves context across steps or sessions.

**What the interviewer wants to hear:**

- Trade-off: clean component boundaries make failure localizable, but real systems leak — a bad tool result often looks like a memory problem and vice versa.
- Production counterexample: a booking agent "remembered" a cancelled reservation because the cancellation observation was never written into the working state; the failure was in perception-to-memory handoff, not in the model.
- Data thinking: instrument each component boundary with counts (inputs seen, plans emitted, tools called, memory reads/writes) so you can say which component degrades first.

**Bonus / Common mistakes:**

- Bonus: describe where each component fails and what a minimal logging point for each boundary looks like.
- Mistake: describing components as modules in a diagram without saying how failure propagates between them.

#### 2. What is the ReAct loop, and why does it work?

**Answer points:**

- ReAct alternates Reasoning (thought) and Acting (tool call) with Observation feeding the next step.
- It works because it makes intermediate steps inspectable and lets the model correct itself from observations.
- The loop is bounded by stop conditions such as a max step count, a final answer, or a policy check.

**What the interviewer wants to hear:**

- Trade-off: reasoning tokens improve task success but add latency and cost per step; there is a point where more steps stop adding accuracy.
- Production counterexample: an agent stuck in a think-act-observe cycle on a flaky API eventually burned more tokens retrying than the task was worth; a "retry with degraded data" branch would have been cheaper.
- Data thinking: plot task success against steps taken; the curve usually flattens, and that flat point is your step budget, not a round number.

**Bonus / Common mistakes:**

- Bonus: mention that observation must be truthful; if the tool returns a wrapper error instead of real data, the loop reasons over garbage.
- Mistake: describing ReAct as "tool calling" only and ignoring the observe-and-correct loop.

#### 3. What is the difference between planning and execution in an Agent?

**Answer points:**

- Planning chooses a sequence or strategy before acting; execution performs steps and may revise the plan.
- Good planners are cheap, fallible, and checkable; execution surfaces reality that planning could not see.
- A strong answer distinguishes single-step tool selection from multi-step plan generation.

**What the interviewer wants to hear:**

- Trade-off: planning upfront improves coherence on long tasks but wastes tokens and can be invalidated by the first tool result; plan-as-you-go trades coherence for responsiveness.
- Production counterexample: a travel agent generated a detailed itinerary, then the first flight API call returned no results, and the plan was worthless; replanning from observation beat the original plan.
- Data thinking: measure plan validity (how often the executed path matched the plan) and replan rate; a 40% replan rate means planning is decorative.

**Bonus / Common mistakes:**

- Bonus: treat plans as cheap hypotheses that execution can revise, not as contracts.
- Mistake: assuming a plan is correct just because the model wrote it confidently.

### Implementation

#### 4. How do you design a tool schema that an LLM can use reliably?

**Answer points:**

- One clear job per tool; name and description say when to use it, not just what it does.
- Inputs and outputs are typed and validated; descriptions are written for the model, not only for humans.
- Errors are distinguishable from empty results; schema includes explicit "no data found" states.

**What the interviewer wants to hear:**

- Trade-off: rich descriptions improve tool selection but consume tokens on every step; short names with good descriptions beat long names with vague descriptions.
- Production counterexample: two tools named `search_documents` and `search_documents_v2` made the model pick the deprecated one; a versioned alias plus a deprecation note fixed selection without retraining.
- Data thinking: log tool-selection confusion (wrong tool, then corrected) and tune descriptions on that data, not on intuition.

**Bonus / Common mistakes:**

- Bonus: validate outputs with schema validation and return structured error codes so the loop can react programmatically.
- Mistake: hiding failure inside a 200 response with an error string, so the Agent cannot tell failure from empty success.

#### 5. What belongs in short-term versus long-term memory?

**Answer points:**

- Short-term memory stores current conversation and task state.
- Long-term memory stores durable facts, preferences, or policies.
- Long-term memory must be scoped, stale-checked, and privacy-sensitive.

**What the interviewer wants to hear:**

- Trade-off: long-term memory personalizes and saves tokens but can poison answers with stale or wrong facts; short-term memory is honest but forgets.
- Production counterexample: a support agent recalled a user's "preferred language" stored a year ago and answered in the wrong language; the fix was a timestamp plus a freshness check on every memory read.
- Data thinking: separate retrieval evidence from user profile; measure profile-hit accuracy on a sample of corrected answers before trusting memory at scale.

**Bonus / Common mistakes:**

- Bonus: design memory writes as explicit, reviewable events instead of silent background saves.
- Mistake: storing sensitive data because "it might be useful later" without a retention policy.

#### 6. Why use a max step limit in a ReAct loop?

**Answer points:**

- Prevents infinite loops and bounds latency and cost.
- Makes failure visible and debuggable by forcing a terminal state.
- Forces a policy decision: fail, clarify, summarize, or escalate when the limit is hit.

**What the interviewer wants to hear:**

- Trade-off: a low limit cuts cost but aborts legitimate long tasks; a high limit hides runaway loops until the bill arrives.
- Production counterexample: an agent with a 50-step limit on a monitoring task looped on a flaky status endpoint all night; a per-tool retry cap plus a total budget stopped the bleed.
- Data thinking: track the distribution of steps per successful task; set the limit at the 95th percentile plus headroom, not at a guess.

**Bonus / Common mistakes:**

- Bonus: use both a step budget and a token budget, because one long step can be more expensive than ten short ones.
- Mistake: treating the step limit as a safety net while ignoring per-step cost.

#### 7. How do you stop an Agent loop correctly?

**Answer points:**

- Define explicit stop conditions: final answer produced, max steps reached, tool policy violated, or safety check tripped.
- Distinguish "done" from "give up": both must be visible to the caller.
- Stop logic lives outside the model so it cannot be talked out of stopping.

**What the interviewer wants to hear:**

- Trade-off: model-decided stopping is flexible but unreliable; code-enforced stopping is reliable but needs explicit rules for every path.
- Production counterexample: an agent kept looping because its prompt said "ask clarifying questions until confident" with no budget; adding a hard turn cap and a clarification budget fixed it.
- Data thinking: log stop reasons per session and alert on any stop-reason distribution shift after prompt changes.

**Bonus / Common mistakes:**

- Bonus: emit a structured terminal status (completed, max_steps, aborted, safety_blocked) for downstream handling.
- Mistake: relying on the model to "realize" it should stop without any external budget.

### Debugging

#### 8. An Agent calls the wrong tool. How do you debug tool selection?

**Answer points:**

- Reproduce with the exact prompt, context, and tool list.
- Check the tool descriptions and name ambiguity, then the schema and examples.
- Look at the observation the model received after the wrong call; selection may be correct but feedback misleading.

**What the interviewer wants to hear:**

- Trade-off: more tools increase capability but degrade selection accuracy; each added tool needs a discriminating description.
- Production counterexample: adding a 12th tool with an overlapping description dropped selection accuracy by 8 points; merging two tools and writing a decision table restored it.
- Data thinking: keep a confusion matrix of intended vs selected tool and fix the top-confusion pairs first.

**Bonus / Common mistakes:**

- Bonus: add explicit "when NOT to use this tool" sections to descriptions.
- Mistake: blaming the model before checking whether the descriptions actually discriminate.

#### 9. A tool returns valid data but the Agent answers incorrectly. How do you debug it?

**Answer points:**

- Verify whether the observation reached context intact and unparsed.
- Check unit conversion, timezone, and field mapping between tool output and the answer.
- Replay the exact step with the same context to separate model error from data error.

**What the interviewer wants to hear:**

- Trade-off: strict parsing prevents silent corruption but breaks on new field shapes; tolerant parsing survives but can map the wrong field.
- Production counterexample: a weather agent returned the wrong city's temperature because the API response used "name" for a different field than the model assumed; the fix was explicit field mapping in the schema.
- Data thinking: run mismatch checks between raw tool output and what the model quoted; a persistent mismatch rate above zero is a schema or parsing bug, not a hallucination.

**Bonus / Common mistakes:**

- Bonus: keep raw tool payloads in the trace so field mapping bugs are provable.
- Mistake: classifying every wrong answer as hallucination before checking the data path.

### Design

#### 10. Design memory and context management for a multi-session support Agent.

**Answer points:**

- Define what is stored (facts, preferences, resolved state), what expires, and what is never stored.
- Store short-term task state per session and long-term profile facts separately.
- Every memory read includes a source and a freshness check; sensitive writes require explicit consent.

**What the interviewer wants to hear:**

- Trade-off: more memory improves personalization but increases staleness, privacy, and retrieval-noise risk.
- Production counterexample: a health assistant stored a screening date, never invalidated it, and later answered with outdated eligibility; a policy field with a TTL and a re-verify trigger fixed it.
- Data thinking: measure the read/write ratio of memory and the hit rate of retrieved facts; a low hit rate means retrieval, not storage, is the problem.

**Bonus / Common mistakes:**

- Bonus: add a forget or correct path so users can remove wrong memories.
- Mistake: storing everything "for future use" without a retention policy or a deletion API.

#### 11. Design a guardrail for an Agent that can write to external systems.

**Answer points:**

- Classify actions by reversibility, blast radius, and data sensitivity before execution.
- Require confirmation or approval for destructive writes; allow read-only actions with rate limits.
- Enforce policy in code, emit audit logs, and verify the result after execution.

**What the interviewer wants to hear:**

- Trade-off: code-enforced guardrails are reliable but inflexible; model-level judgment is flexible but unreliable, so the safety-critical checks belong in code.
- Production counterexample: a "confirm before sending email" prompt was bypassed when the model summarized the email as "final confirmation preview" and the user clicked through; the fix was a separate confirmation step the model could not phrase.
- Data thinking: track guardrail trigger rate and override rate; a high override rate means the guardrail is either wrong or invisible to users.

**Bonus / Common mistakes:**

- Bonus: treat the guardrail as the outer ring and the prompt as the inner ring; never let the prompt be the only barrier.
- Mistake: believing a strong system prompt is sufficient protection for irreversible actions.

## Follow-Up Bank

- What breaks if tool feedback is ambiguous?
- What should happen when the step limit is reached: fail, clarify, summarize, or escalate?
- How do you avoid storing sensitive data in memory?
- How do you prevent an Agent from using a tool when it only has stale retrieved context?
- What does a good stop-condition log look like in production?

## Common Red Flags

- Treats max steps as a fixed constant instead of a measured budget.
- Cannot distinguish model error from tool data error.
- Treats memory as append-only storage with no freshness or consent.
- Trusts the model to stop or to stay safe without any code-enforced control.
- Describes ReAct as tool calling without the observe-and-correct loop.

## Portfolio Evidence

For L1, acceptable evidence is:

- A working ReAct loop with a measured step budget and stop reasons.
- A tool schema with typed inputs, output validation, and distinguishable empty results.
- A memory design that separates short-term state from long-term profile facts.

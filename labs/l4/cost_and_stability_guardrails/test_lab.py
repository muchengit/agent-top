from __future__ import annotations

import unittest

from .agent_top_labs_l4_cost_and_stability_guardrails import (
    BudgetPolicy,
    RuntimeAction,
    RuntimeState,
    decide_guardrail,
    degraded_response,
)


class CostAndStabilityGuardrailsTest(unittest.TestCase):
    def test_continue_when_budgets_are_available(self) -> None:
        policy = BudgetPolicy(5, 3, 2, 1000, 1000)
        state = RuntimeState(1, 1, 0, 100, 100, 100)
        decision = decide_guardrail(state, policy)
        self.assertEqual(decision.action, RuntimeAction.CONTINUE)
        self.assertEqual(decision.reasons, ())

    def test_step_budget_blocks_runtime(self) -> None:
        policy = BudgetPolicy(3, 3, 2, 1000, 1000)
        state = RuntimeState(3, 1, 0, 100, 100, 100)
        decision = decide_guardrail(state, policy)
        self.assertEqual(decision.action, RuntimeAction.BLOCK)
        self.assertIn("step_budget_exhausted", decision.reasons)

    def test_token_budget_degrades_before_next_model_call(self) -> None:
        policy = BudgetPolicy(5, 3, 2, 1000, 100)
        state = RuntimeState(1, 1, 0, 100, 80, 40)
        decision = decide_guardrail(state, policy)
        self.assertEqual(decision.action, RuntimeAction.DEGRADE)
        self.assertIn("token_budget_exhausted", decision.reasons)

    def test_degraded_response_keeps_trace_contract(self) -> None:
        decision = decide_guardrail(
            RuntimeState(1, 1, 0, 100, 80, 40),
            BudgetPolicy(5, 3, 2, 1000, 100),
        )
        response = degraded_response(
            decision,
            fallback_summary="Return a concise sourced answer.",
            request_id="req-1",
        )
        self.assertEqual(response["status"], "degraded")
        self.assertTrue(response["trace_required"])

    def test_retry_budget_blocks(self) -> None:
        policy = BudgetPolicy(5, 3, 2, 1000, 1000)
        state = RuntimeState(1, 1, 2, 100, 100, 100)
        decision = decide_guardrail(state, policy)
        self.assertEqual(decision.action, RuntimeAction.BLOCK)
        self.assertIn("retry_budget_exhausted", decision.reasons)

    def test_tool_call_budget_degrades_not_blocks(self) -> None:
        policy = BudgetPolicy(5, 3, 2, 1000, 1000)
        state = RuntimeState(1, 3, 0, 100, 100, 100)
        decision = decide_guardrail(state, policy)
        self.assertEqual(decision.action, RuntimeAction.DEGRADE)
        self.assertIn("tool_call_budget_exhausted", decision.reasons)

    def test_latency_boundary_equal_degrades(self) -> None:
        policy = BudgetPolicy(5, 3, 2, 1000, 1000)
        state = RuntimeState(1, 1, 0, 1000, 100, 100)
        decision = decide_guardrail(state, policy)
        self.assertEqual(decision.action, RuntimeAction.DEGRADE)
        self.assertIn("latency_budget_exhausted", decision.reasons)

    def test_token_boundary_exact_is_not_exhausted(self) -> None:
        policy = BudgetPolicy(5, 3, 2, 1000, 100)
        state = RuntimeState(1, 1, 0, 100, 60, 40)
        decision = decide_guardrail(state, policy)
        self.assertEqual(decision.action, RuntimeAction.CONTINUE)
        self.assertEqual(decision.reasons, ())

    def test_multiple_degrade_reasons_preserved_in_order(self) -> None:
        policy = BudgetPolicy(5, 3, 2, 1000, 100)
        state = RuntimeState(1, 3, 0, 1000, 80, 40)
        decision = decide_guardrail(state, policy)
        self.assertEqual(decision.action, RuntimeAction.DEGRADE)
        self.assertEqual(
            decision.reasons,
            ("tool_call_budget_exhausted", "latency_budget_exhausted", "token_budget_exhausted"),
        )

    def test_zero_budget_policy_blocks_immediately(self) -> None:
        policy = BudgetPolicy(0, 0, 0, 0, 0)
        state = RuntimeState(0, 0, 0, 0, 0, 0)
        decision = decide_guardrail(state, policy)
        self.assertEqual(decision.action, RuntimeAction.BLOCK)
        self.assertIn("step_budget_exhausted", decision.reasons)

    def test_steps_and_retries_both_block(self) -> None:
        policy = BudgetPolicy(2, 3, 1, 1000, 1000)
        state = RuntimeState(2, 1, 1, 100, 100, 100)
        decision = decide_guardrail(state, policy)
        self.assertEqual(decision.action, RuntimeAction.BLOCK)
        self.assertIn("step_budget_exhausted", decision.reasons)
        self.assertIn("retry_budget_exhausted", decision.reasons)

    def test_blocked_response_shape(self) -> None:
        decision = decide_guardrail(
            RuntimeState(3, 1, 0, 100, 100, 100),
            BudgetPolicy(3, 3, 2, 1000, 1000),
        )
        response = degraded_response(
            decision,
            fallback_summary="unused",
            request_id="req-2",
        )
        self.assertEqual(response["status"], "blocked")
        self.assertEqual(response["request_id"], "req-2")
        self.assertNotIn("trace_required", response)

    def test_chinese_fallback_preserved(self) -> None:
        decision = decide_guardrail(
            RuntimeState(1, 1, 0, 100, 80, 40),
            BudgetPolicy(5, 3, 2, 1000, 100),
        )
        response = degraded_response(
            decision,
            fallback_summary="返回简短的带来源回答",
            request_id="req-中文",
        )
        self.assertEqual(response["message"], "返回简短的带来源回答")
        self.assertEqual(response["request_id"], "req-中文")

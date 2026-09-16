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

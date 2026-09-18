from __future__ import annotations

import unittest

from .agent_top_labs_l2_cost_aware_router import RequestProfile, Route, route_request


class CostAwareRouterTest(unittest.TestCase):
    def test_simple_answer_route(self) -> None:
        profile = RequestProfile(False, False, False, False, 100, 1000)
        self.assertEqual(route_request(profile), Route.SIMPLE_ANSWER)

    def test_tool_route(self) -> None:
        profile = RequestProfile(True, True, False, False, 200, 1000)
        self.assertEqual(route_request(profile), Route.TOOL_CALL)

    def test_latency_budget_escalates(self) -> None:
        profile = RequestProfile(False, False, False, False, 2000, 1000)
        self.assertEqual(route_request(profile), Route.ESCALATE)

    def test_confirmation_required_escalates_even_if_fast(self) -> None:
        profile = RequestProfile(False, False, True, False, 1, 1000)
        self.assertEqual(route_request(profile), Route.ESCALATE)

    def test_confirmed_high_latency_still_escalates(self) -> None:
        profile = RequestProfile(False, False, True, True, 2000, 1000)
        self.assertEqual(route_request(profile), Route.ESCALATE)

    def test_retrieval_route(self) -> None:
        profile = RequestProfile(True, False, False, False, 100, 1000)
        self.assertEqual(route_request(profile), Route.RETRIEVAL)

    def test_latency_boundary_equal_is_not_escalated(self) -> None:
        profile = RequestProfile(False, False, False, False, 1000, 1000)
        self.assertEqual(route_request(profile), Route.SIMPLE_ANSWER)

    def test_tool_takes_precedence_over_retrieval(self) -> None:
        profile = RequestProfile(True, True, False, False, 100, 1000)
        self.assertEqual(route_request(profile), Route.TOOL_CALL)

    def test_negative_latency_is_always_within_budget(self) -> None:
        profile = RequestProfile(False, False, False, False, -5, 0)
        self.assertEqual(route_request(profile), Route.SIMPLE_ANSWER)

    def test_zero_latency_budget_escalates_positive_latency(self) -> None:
        profile = RequestProfile(False, False, False, False, 1, 0)
        self.assertEqual(route_request(profile), Route.ESCALATE)

    def test_confirmation_flag_without_needs_is_ignored(self) -> None:
        profile = RequestProfile(False, False, False, True, 100, 1000)
        self.assertEqual(route_request(profile), Route.SIMPLE_ANSWER)

    def test_negative_budget_escalates_everything_positive(self) -> None:
        profile = RequestProfile(False, False, False, False, 50, -10)
        self.assertEqual(route_request(profile), Route.ESCALATE)

    def test_zero_latency_with_zero_budget_stays_simple(self) -> None:
        profile = RequestProfile(False, False, False, False, 0, 0)
        self.assertEqual(route_request(profile), Route.SIMPLE_ANSWER)

    def test_confirmed_tool_call_within_budget_routes_tool(self) -> None:
        profile = RequestProfile(True, True, True, True, 500, 1000)
        self.assertEqual(route_request(profile), Route.TOOL_CALL)

    def test_confirmed_retrieval_within_budget_routes_retrieval(self) -> None:
        profile = RequestProfile(True, False, True, True, 300, 1000)
        self.assertEqual(route_request(profile), Route.RETRIEVAL)

    def test_route_enum_values(self) -> None:
        self.assertEqual(Route.SIMPLE_ANSWER.value, "simple_answer")
        self.assertEqual(Route.RETRIEVAL.value, "retrieval")
        self.assertEqual(Route.TOOL_CALL.value, "tool_call")
        self.assertEqual(Route.ESCALATE.value, "escalate")

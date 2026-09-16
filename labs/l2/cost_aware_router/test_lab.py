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

import unittest

from .agent_top_labs_l5_multilingual_pattern_lab import (
    assert_blocked_plan,
    assert_ready_plan,
    run_python_pattern,
)


class MultilingualPatternLabTest(unittest.TestCase):
    def test_python_safe_request_gets_three_step_plan(self) -> None:
        stop_reason, steps = run_python_pattern("update profile")
        assert_ready_plan(stop_reason, steps)

    def test_python_safety_rule_stops_before_execution(self) -> None:
        stop_reason, steps = run_python_pattern("delete_all")
        assert_blocked_plan(stop_reason, steps)

from __future__ import annotations

import unittest

from .agent_top_labs_l4_regression_gate import ReleaseProfile, evaluate_release


class RegressionGateTest(unittest.TestCase):
    def test_green_release_passes(self) -> None:
        profile = ReleaseProfile(0, 0, True, 0.8, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertTrue(should_ship)
        self.assertEqual(failures, [])

    def test_safety_failure_blocks_release(self) -> None:
        profile = ReleaseProfile(1, 0, True, 0.8, 1.0)
        should_ship, failures = evaluate_release(profile)
        self.assertFalse(should_ship)
        self.assertIn("critical_safety_failures", failures)

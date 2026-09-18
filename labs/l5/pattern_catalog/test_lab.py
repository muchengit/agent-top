from __future__ import annotations

import unittest

from .agent_top_labs_l5_pattern_catalog import ready_pattern


class PatternCatalogTest(unittest.TestCase):
    def test_catalog_contains_ready_pattern(self) -> None:
        self.assertTrue(ready_pattern("verifiable-action"))

    def test_unknown_pattern_is_not_ready(self) -> None:
        self.assertFalse(ready_pattern("unknown-pattern"))

from __future__ import annotations

import unittest

from .agent_top_labs_l5_pattern_catalog import PATTERN_CATALOG, PatternEntry, ready_pattern


class PatternCatalogTest(unittest.TestCase):
    def test_catalog_contains_ready_pattern(self) -> None:
        self.assertTrue(ready_pattern("verifiable-action"))

    def test_unknown_pattern_is_not_ready(self) -> None:
        self.assertFalse(ready_pattern("unknown-pattern"))

    def test_both_catalog_patterns_are_ready(self) -> None:
        for name in ("verifiable-action", "safe-tool-routing"):
            self.assertTrue(ready_pattern(name), name)

    def test_missing_name_key_is_not_ready(self) -> None:
        self.assertFalse(ready_pattern(""))
        self.assertFalse(ready_pattern(" "))

    def test_case_sensitive_lookup_fails_closed(self) -> None:
        self.assertFalse(ready_pattern("Verifiable-Action"))
        self.assertFalse(ready_pattern("VERIFIABLE-ACTION"))

    def test_entry_has_all_contract_fields(self) -> None:
        entry = PATTERN_CATALOG["verifiable-action"]
        self.assertEqual(entry.name, "verifiable-action")
        self.assertIn("request", entry.inputs)
        self.assertIn("safety_rules", entry.inputs)
        self.assertIn("plan", entry.outputs)
        self.assertIn("stop_reason", entry.outputs)
        self.assertEqual(entry.safety_checks, ("block_on_rule",))
        self.assertEqual(entry.verification, ("eval_probe",))

    def test_safe_tool_routing_contract_fields(self) -> None:
        entry = PATTERN_CATALOG["safe-tool-routing"]
        self.assertEqual(entry.inputs, ("request", "tool_policy", "role"))
        self.assertEqual(entry.outputs, ("route", "outcome"))
        self.assertEqual(entry.safety_checks, ("role_check", "confirmation_check"))
        self.assertEqual(entry.verification, ("tool_audit_log",))

    def test_pattern_entry_is_immutable(self) -> None:
        entry = PATTERN_CATALOG["verifiable-action"]
        with self.assertRaises(Exception):
            entry.name = "renamed"  # type: ignore[misc]
        with self.assertRaises(Exception):
            entry.inputs = ("request",)  # type: ignore[misc]

    def test_unknown_patterns_fail_closed_even_with_partial_name(self) -> None:
        self.assertFalse(ready_pattern("verifiable"))
        self.assertFalse(ready_pattern("-action"))
        self.assertFalse(ready_pattern("pattern"))

    def test_ready_pattern_unknown_name_is_not_ready(self) -> None:
        self.assertFalse(ready_pattern("does-not-exist"))

    def test_ready_pattern_non_string_name_returns_false(self) -> None:
        self.assertFalse(ready_pattern(None))  # type: ignore[arg-type]
        self.assertFalse(ready_pattern(1))  # type: ignore[arg-type]

    def test_entry_missing_verification_is_not_ready(self) -> None:
        incomplete = PatternEntry(
            name="incomplete",
            inputs=("request",),
            outputs=("plan",),
            safety_checks=("block_on_rule",),
            verification=(),
        )
        self.assertFalse(ready_pattern("incomplete"))


if __name__ == "__main__":
    unittest.main()

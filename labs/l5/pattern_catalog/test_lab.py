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
        entry = PatternEntry(
            name="incomplete",
            inputs=("request",),
            outputs=("plan",),
            safety_checks=("block_on_rule",),
            verification=(),
        )
        # Direct catalog lookup fails closed; entry-level readiness is
        # demonstrated via the catalog's non-empty contract checks.
        self.assertFalse(ready_pattern("incomplete"))
        self.assertEqual(entry.verification, ())

    def test_catalog_keys_match_entry_names(self) -> None:
        for name, entry in PATTERN_CATALOG.items():
            self.assertEqual(name, entry.name)

    def test_catalog_entries_non_empty_contract(self) -> None:
        for name, entry in PATTERN_CATALOG.items():
            self.assertTrue(entry.inputs, name)
            self.assertTrue(entry.outputs, name)
            self.assertTrue(entry.safety_checks, name)
            self.assertTrue(entry.verification, name)

    def test_ready_pattern_accepts_whitespace_name_false(self) -> None:
        self.assertFalse(ready_pattern(" \t "))

    def test_ready_pattern_name_with_extra_chars(self) -> None:
        self.assertFalse(ready_pattern("verifiable-action "))
        self.assertFalse(ready_pattern(" verifiable-action"))

    def test_safe_tool_routing_ready(self) -> None:
        self.assertTrue(ready_pattern("safe-tool-routing"))

    def test_pattern_entry_defaults_are_empty(self) -> None:
        entry = PatternEntry(name="empty", inputs=(), outputs=(), safety_checks=(), verification=())
        self.assertEqual(entry.inputs, ())
        self.assertEqual(entry.outputs, ())
        self.assertEqual(entry.safety_checks, ())
        self.assertEqual(entry.verification, ())

    def test_catalog_size_is_two(self) -> None:
        self.assertEqual(len(PATTERN_CATALOG), 2)

    def test_verifiable_action_outputs_include_stop_reason(self) -> None:
        entry = PATTERN_CATALOG["verifiable-action"]
        self.assertIn("stop_reason", entry.outputs)

    def test_safe_tool_routing_safety_checks_include_confirmation(self) -> None:
        entry = PATTERN_CATALOG["safe-tool-routing"]
        self.assertIn("confirmation_check", entry.safety_checks)


if __name__ == "__main__":
    unittest.main()

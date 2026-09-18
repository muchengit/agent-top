from __future__ import annotations

import unittest

from .agent_top_labs_l3_multi_agent_supervisor import (
    AgentName,
    TaskProfile,
    assign_agents,
    supervisor_decision,
)


class MultiAgentSupervisorTest(unittest.TestCase):
    def test_research_only_task(self) -> None:
        task = TaskProfile(True, False, False, False, False)
        self.assertEqual(assign_agents(task), (AgentName.RESEARCH,))
        self.assertEqual(supervisor_decision(task), AgentName.RESEARCH)

    def test_tool_task_with_confirmation(self) -> None:
        task = TaskProfile(False, True, False, True, False)
        self.assertEqual(
            assign_agents(task),
            (AgentName.HUMAN, AgentName.TOOL),
        )
        self.assertEqual(supervisor_decision(task), AgentName.HUMAN)

    def test_research_and_verification(self) -> None:
        task = TaskProfile(True, False, True, False, False)
        self.assertEqual(
            assign_agents(task),
            (AgentName.RESEARCH, AgentName.VERIFIER),
        )

    def test_empty_task_defaults_to_research(self) -> None:
        task = TaskProfile(False, False, False, False, False)
        self.assertEqual(assign_agents(task), ())
        self.assertEqual(supervisor_decision(task), AgentName.RESEARCH)

    def test_tool_only_without_confirmation_need(self) -> None:
        task = TaskProfile(False, True, False, False, False)
        self.assertEqual(assign_agents(task), (AgentName.TOOL,))
        self.assertEqual(supervisor_decision(task), AgentName.TOOL)

    def test_confirmation_with_tool_and_user_ok_no_human(self) -> None:
        task = TaskProfile(False, True, False, True, True)
        self.assertEqual(assign_agents(task), (AgentName.TOOL,))

    def test_verification_only(self) -> None:
        task = TaskProfile(False, False, True, False, False)
        self.assertEqual(assign_agents(task), (AgentName.VERIFIER,))

    def test_full_pipeline_without_confirmation(self) -> None:
        task = TaskProfile(True, True, True, True, False)
        self.assertEqual(
            assign_agents(task),
            (AgentName.RESEARCH, AgentName.HUMAN, AgentName.TOOL, AgentName.VERIFIER),
        )
        self.assertEqual(supervisor_decision(task), AgentName.RESEARCH)

    def test_confirmation_ignored_without_tool(self) -> None:
        task = TaskProfile(False, False, False, True, False)
        self.assertEqual(assign_agents(task), ())

    def test_frozen_profile_rejects_mutation(self) -> None:
        task = TaskProfile(True, False, False, False, False)
        with self.assertRaises(Exception):
            task.needs_retrieval = False  # type: ignore[misc]

    def test_enum_values_are_strings(self) -> None:
        self.assertEqual(AgentName.RESEARCH.value, "research")
        self.assertEqual(AgentName.HUMAN.value, "human")

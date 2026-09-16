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

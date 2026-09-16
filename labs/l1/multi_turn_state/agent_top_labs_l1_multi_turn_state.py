"""L1 deterministic multi-turn state lab."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TurnMessage:
    role: str
    content: str


class MultiTurnState:
    def __init__(self, summary_limit: int = 2) -> None:
        self.messages: list[TurnMessage] = []
        self.summary_limit = summary_limit

    def add(self, message: TurnMessage) -> None:
        self.messages.append(message)

    def recent_messages(self, count: int) -> list[TurnMessage]:
        return self.messages[-count:]

    def needs_summary(self) -> bool:
        return len(self.messages) > self.summary_limit

    def build_prompt_context(self) -> list[str]:
        context = []
        if self.needs_summary():
            context.append(f"summary_of_{len(self.messages) - self.summary_limit}_older_messages")
        recent_messages = self.recent_messages(self.summary_limit)
        context.extend(f"{msg.role}: {msg.content}" for msg in recent_messages)
        return context

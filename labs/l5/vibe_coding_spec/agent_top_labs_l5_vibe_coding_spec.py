"""L5 deterministic spec checker for the Vibe Coding workflow.

A spec is "ready to prompt" only when goal, interface, and acceptance are
all present. This mirrors the Vibe Coding one-sentence rule: if you cannot
state goal, interface, and acceptance, you are still exploring.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Spec:
    goal: str
    interface: str
    acceptance: str
    scope: str = ""
    constraints: str = ""
    missing: tuple[str, ...] = field(default=(), init=False)

    def __post_init__(self) -> None:
        missing = []
        for field_name in ("goal", "interface", "acceptance"):
            value = getattr(self, field_name)
            if not value.strip():
                missing.append(field_name)
        object.__setattr__(self, "missing", tuple(missing))

    @property
    def is_ready(self) -> bool:
        return not self.missing

    def one_sentence(self) -> str:
        return " ".join(
            part.strip()
            for part in (self.goal, self.interface, self.acceptance)
            if part.strip()
        )


def check_spec(goal: str, interface: str, acceptance: str) -> Spec:
    return Spec(goal=goal, interface=interface, acceptance=acceptance)


def ready_to_prompt(spec: Spec) -> bool:
    """A spec is prompt-ready when goal, interface, and acceptance exist."""
    return spec.is_ready


def acceptance_command_present(spec: Spec, commands: tuple[str, ...]) -> bool:
    """True when the acceptance text mentions at least one runnable command."""
    if not spec.is_ready:
        return False
    lowered = spec.acceptance.lower()
    return any(command.lower() in lowered for command in commands)

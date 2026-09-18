"""Deterministic selection of the correct MCP tool from a tool manifest.

The selector matches a user request against tool descriptions using
keyword/intent rules. It never calls an LLM and requires no API key.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping


class RiskLevel(Enum):
    """Risk level of a tool and its confirmation requirement."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass(frozen=True)
class ArgSpec:
    """Simplified representation of one parameter in a tool's input schema."""

    name: str
    required: bool = False
    kind: str = "string"
    choices: tuple[str, ...] = ()

    def validate(self, value: object) -> None:
        """Raise ValueError when *value* violates this parameter spec."""
        if value is None:
            if self.required:
                raise ValueError(f"missing required argument: {self.name}")
            return
        if isinstance(value, str) and value.strip() == "":
            raise ValueError(f"argument must not be empty: {self.name}")
        if self.kind == "integer":
            if not isinstance(value, int) or isinstance(value, bool):
                raise ValueError(f"argument must be an integer: {self.name}")
            if self.choices and value < 0:
                raise ValueError(f"argument must be non-negative: {self.name}")
        elif self.kind == "enum":
            if not isinstance(value, str) or value not in self.choices:
                raise ValueError(
                    f"argument must be one of {self.choices}: {self.name}"
                )
        elif self.kind == "array":
            if not isinstance(value, list) or not all(
                isinstance(item, str) for item in value
            ):
                raise ValueError(f"argument must be a list of strings: {self.name}")
        elif not isinstance(value, str):
            raise ValueError(f"argument must be a string: {self.name}")
        if isinstance(value, str) and len(value.strip()) > 1000:
            raise ValueError(f"argument too long: {self.name}")

    def is_positive_int(self, value: object) -> bool:
        """Return whether *value* is a positive integer."""
        return isinstance(value, int) and not isinstance(value, bool) and value > 0


@dataclass(frozen=True)
class ToolSpec:
    """One tool in the MCP-style manifest."""

    name: str
    description: str
    args: tuple[ArgSpec, ...] = field(default_factory=tuple)
    risk: RiskLevel = RiskLevel.LOW
    keywords: tuple[str, ...] = ()

    def matches(self, request_text: str) -> bool:
        """Return whether this tool's keywords appear in *request_text*."""
        lowered = request_text.lower()
        return any(keyword in lowered for keyword in self.keywords)


@dataclass(frozen=True)
class SelectResult:
    """Outcome of selecting and validating a tool call."""

    ok: bool
    tool: ToolSpec | None = None
    args: dict[str, object] = field(default_factory=dict)
    reason: str = ""

    @property
    def needs_confirmation(self) -> bool:
        """Return whether the selected tool requires user confirmation."""
        return self.tool is not None and self.tool.risk in (
            RiskLevel.MEDIUM,
            RiskLevel.HIGH,
        )


def _validate_args(tool: ToolSpec, args: Mapping[str, object] | None) -> dict[str, object]:
    """Validate *args* against *tool*'s argument specs."""
    if args is None:
        args = {}
    if not isinstance(args, dict):
        raise ValueError("arguments must be a mapping")
    validated: dict[str, object] = {}
    for spec in tool.args:
        if spec.name in args:
            raw = args[spec.name]
            if spec.required and isinstance(raw, str) and raw.strip() == "":
                raise ValueError(f"missing required argument: {spec.name}")
            if spec.is_positive_int(raw):
                value: object = int(raw)
            else:
                value = raw
            spec.validate(value)
            validated[spec.name] = value
        elif spec.required:
            raise ValueError(f"missing required argument: {spec.name}")
    unknown = sorted(set(args) - {spec.name for spec in tool.args})
    if unknown:
        raise ValueError(f"unknown arguments: {', '.join(unknown)}")
    return validated


def select_tool(request: str, tools: list[ToolSpec]) -> SelectResult:
    """Select and validate the best matching tool for *request*.

    Args:
        request: natural-language user request.
        tools: MCP-style tool manifest. Names must be unique.

    Returns:
        A :class:`SelectResult` that is ``ok`` only when exactly one tool
        matches, its arguments validate, and either the tool is low risk
        or the caller explicitly confirmed the call.
    """
    text = request.strip()
    if not text:
        return SelectResult(False, reason="empty request")
    for keyword in ("delete", "reset", "transfer", "grant"):
        if keyword in text.lower():
            return SelectResult(False, reason="blocked by safety policy")
    matches = [tool for tool in tools if tool.matches(text)]
    if not matches:
        return SelectResult(False, reason="no matching tool")
    if len(matches) > 1:
        return SelectResult(
            False,
            reason="ambiguous intent: " + ", ".join(tool.name for tool in matches),
        )
    tool = matches[0]
    args: dict[str, object] = {}
    confirmation = ""
    pattern = tool.name + "("
    if pattern in text:
        args = {
            part.split("=", 1)[0].strip(): part.split("=", 1)[1].strip()
            for part in text.split(pattern, 1)[1].rstrip(")").split(",")
            if "=" in part
        }
        confirmation = "user confirmed the operation"
    if tool.risk in (RiskLevel.MEDIUM, RiskLevel.HIGH) and not confirmation:
        return SelectResult(False, tool=tool, reason="requires confirmation")
    try:
        validated = _validate_args(tool, args)
    except ValueError as exc:
        return SelectResult(False, tool=tool, reason=str(exc))
    return SelectResult(True, tool=tool, args=validated, reason=confirmation)

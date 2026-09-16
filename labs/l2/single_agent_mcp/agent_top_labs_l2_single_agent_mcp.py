"""L2 single-agent MCP-style tool boundary example."""

from __future__ import annotations

import json


class ToolServer:
    def list_tools(self) -> list[str]:
        return ["search_docs"]

    def call_tool(self, name: str, payload: dict[str, str]) -> str:
        if name != "search_docs":
            raise ValueError(f"Unknown tool: {name}")
        query = payload.get("query", "").strip()
        if not query:
            raise ValueError("query is required")
        return json.dumps({"hits": [f"synthetic result for {query}"]})


class Guardrail:
    def allow(self, query: str) -> bool:
        trimmed = query.strip()
        return bool(trimmed) and len(trimmed) <= 200


def run_single_agent(query: str) -> dict[str, object]:
    guardrail = Guardrail()
    if not guardrail.allow(query):
        return {"ok": False, "reason": "guardrail rejected query"}
    server = ToolServer()
    result = server.call_tool("search_docs", {"query": query.strip()})
    return {"ok": True, "result": result}

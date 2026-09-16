"""L0 example for first LLM call concepts.

This Lab uses a local fake model so it runs without an API key.
"""

from __future__ import annotations


class FakeModel:
    """Deterministic fake model used for learning the request shape."""

    def complete(self, system_prompt: str, prompt: str) -> str:
        if not prompt:
            return "No user prompt provided."
        return f"[{system_prompt}] I received {len(prompt.split())} prompt tokens: {prompt}"


def first_llm_call(system_prompt: str = "You are helpful.", prompt: str = "Explain agents simply.") -> str:
    model = FakeModel()
    return model.complete(system_prompt, prompt)


if __name__ == "__main__":
    print(first_llm_call())

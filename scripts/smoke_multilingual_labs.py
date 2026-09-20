#!/usr/bin/env python3
"""Optional cross-language smoke checks for L5 pattern references."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "labs" / "l5" / "multilingual_pattern_lab"
# Build artifacts go to dist/ (gitignored), not a tool configuration directory.
RUST_BINARY = ROOT / "dist" / "smoke" / "rust_verifiable_action"


def run(name: str, command: list[str], cwd: Path = ROOT) -> None:
    print(f"smoke: {name}")
    subprocess.run(command, cwd=cwd, check=True)


def run_if_available(
    name: str,
    binary: str,
    command: list[str],
    cwd: Path = ROOT,
) -> None:
    if shutil.which(binary) is None:
        print(f"skip: {name} ({binary} not installed)")
        return
    run(name, command, cwd)


def compile_and_run(name: str, compiler: str, build_command: list[str]) -> None:
    """Compile a native target, then execute it so its own asserts are verified."""
    if shutil.which(compiler) is None:
        print(f"skip: {name} ({compiler} not installed)")
        return
    run(f"{name} build", build_command)
    run(name, [build_command[-1]])


def main() -> int:
    python_command = [sys.executable, "-m", "unittest", "labs.l5.multilingual_pattern_lab.test_lab"]
    run("python", python_command)

    node_command = ["node", str(LAB / "node" / "verifiable_action.mjs")]
    run_if_available("node", "node", node_command)

    RUST_BINARY.parent.mkdir(parents=True, exist_ok=True)
    rust_command = ["rustc", "--edition", "2021"]
    rust_command.extend([str(LAB / "rust" / "verifiable_action.rs"), "-o", str(RUST_BINARY)])
    compile_and_run("rust", "rustc", rust_command)

    go_command = ["go", "test", "./...", "-run", "Verifiable"]
    run_if_available("go", "go", go_command, LAB / "go")

    local_tsc = ROOT / "node_modules" / ".bin" / "tsc"
    if local_tsc.exists():
        ts_command = [str(local_tsc), "--project", str(LAB / "typescript" / "tsconfig.json")]
        run("typescript", ts_command)
    elif shutil.which("tsc"):
        ts_command = ["tsc", "--project", str(LAB / "typescript" / "tsconfig.json")]
        run("typescript", ts_command)
    else:
        print("skip: typescript (tsc not installed; run npm install first)")

    print("multilingual smoke ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Run the Wordle reference solutions and compare their scripted transcripts."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGES = [
    "01-environment-configuration",
    "02-variables-and-data-types",
    "03-data-structures",
    "04-control-flow",
    "05-functions",
    "06-modules",
    "07-comprehensions",
    "08-exception-handling",
    "09-python-io",
    "10-database-access",
    "11-python-classes",
    "12-type-hinting",
    "13-python-libraries",
]


def run(
    command: list[str],
    stage: Path,
    stdin: str = "",
    env_extra: dict[str, str] | None = None,
) -> str:
    """Run a command in a stage and return its standard output."""
    environment = os.environ.copy()
    environment.pop("VIRTUAL_ENV", None)
    if env_extra:
        environment.update(env_extra)
    result = subprocess.run(
        command,
        cwd=stage,
        input=stdin,
        text=True,
        encoding="utf-8",
        capture_output=True,
        env=environment,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"{stage.name}: {' '.join(command)} exited {result.returncode}\n"
            f"{result.stdout}{result.stderr}"
        )
    return result.stdout


def clean_runtime_files(stage: Path) -> None:
    """Remove generated state so every scripted run starts from the same point."""
    for name in ("history.txt", "wordle.db", "save.json"):
        (stage / name).unlink(missing_ok=True)


def transcript_for(name: str) -> tuple[list[str], str]:
    """Choose the fixed command and input sequence for one exercise stage."""
    number = int(name[:2])
    if number == 1:
        return ["uv", "run", "python", "wordle.py"], ""
    if number in (2, 3):
        return ["uv", "run", "python", "wordle.py"], "react\n"
    if number <= 5:
        return ["uv", "run", "python", "wordle.py"], "slate\ncrane\n"
    return ["uv", "run", "python", "-m", "wordle"], "slate\ncrane\n"


def main() -> int:
    """Run tests, type checks and deterministic play-throughs for every stage."""
    record = "--record" in sys.argv
    transcripts = ROOT / "build" / "transcripts"
    transcripts.mkdir(parents=True, exist_ok=True)
    failures = 0
    for name in STAGES:
        stage = ROOT / "solutions" / name
        if not stage.is_dir():
            print(f"missing solution: {stage.relative_to(ROOT)}")
            failures += 1
            continue
        number = int(name[:2])
        if number == 13:
            test_files = [
                path
                for path in stage.rglob("test_*.py")
                if ".venv" not in path.parts and "__pycache__" not in path.parts
            ]
            if test_files:
                try:
                    test_output = run(["uv", "run", "pytest", "-q"], stage)
                    match = re.search(r"(\d+) passed", test_output)
                    count = match.group(1) if match else "unknown number of"
                    print(f"{name}: pytest passed ({count} tests)")
                except RuntimeError as error:
                    print(error)
                    failures += 1
        else:
            test_dir = ROOT / "build" / "solution-tests" / name
            if test_dir.is_dir():
                try:
                    test_output = run(
                        [
                            sys.executable,
                            "-m",
                            "pytest",
                            "-q",
                            str(test_dir),
                            "--rootdir",
                            str(stage),
                            "-o",
                            f"pythonpath={stage}",
                        ],
                        stage,
                        env_extra={"PYTHONPATH": str(stage)},
                    )
                    match = re.search(r"(\d+) passed", test_output)
                    count = match.group(1) if match else "unknown number of"
                    print(f"{name}: pytest passed ({count} tests)")
                except RuntimeError as error:
                    print(error)
                    failures += 1
        if number >= 12:
            try:
                run(["uv", "run", "mypy", "wordle"], stage)
                print(f"{name}: mypy passed")
            except RuntimeError as error:
                print(error)
                failures += 1
        clean_runtime_files(stage)
        command, guesses = transcript_for(name)
        try:
            output = run(command, stage, guesses)
            expected_path = transcripts / f"{name}.txt"
            if record:
                expected_path.write_text(output, encoding="utf-8")
                print(f"{name}: recorded {expected_path.relative_to(ROOT)}")
            elif not expected_path.exists():
                print(f"missing transcript: {expected_path.relative_to(ROOT)}")
                failures += 1
            else:
                expected = expected_path.read_text(encoding="utf-8")
                if output != expected:
                    print(f"{name}: transcript differs from {expected_path.relative_to(ROOT)}")
                    print("--- expected ---")
                    print(expected, end="" if expected.endswith("\n") else "\n")
                    print("--- actual ---")
                    print(output, end="" if output.endswith("\n") else "\n")
                    failures += 1
                else:
                    print(f"{name}: scripted output matches transcript")
        except RuntimeError as error:
            print(error)
            failures += 1
        clean_runtime_files(stage)
    if failures:
        print(f"{failures} solution check(s) failed.")
        return 1
    print(f"All {len(STAGES)} solution stages passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Run every executable quiz example and compare it with its keyed answer."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

QUIZ_FILE = Path(__file__).with_name("quiz.json")


def main() -> int:
    questions = json.loads(QUIZ_FILE.read_text(encoding="utf-8"))
    failures = []
    checked = 0
    for number, question in enumerate(questions, start=1):
        options = question["options"]
        if len(options) != 3 or len(set(options)) != 3:
            failures.append(f"Question {number}: options must be three distinct answers")
            continue
        if "code" not in question:
            continue
        checked += 1
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, "-c", question["code"]],
                cwd=directory,
                capture_output=True,
                text=True,
                check=False,
            )
        actual = result.stdout.rstrip("\r\n")
        expected_exception = question.get("raises")
        exception_matches = expected_exception and expected_exception in result.stderr
        output_matches = not result.returncode and actual == options[0]
        if not (exception_matches or output_matches):
            failures.append(
                f"Question {number}: expected {options[0]!r}, "
                f"got {actual!r}; stderr={result.stderr.strip()!r}"
            )
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Checked {len(questions)} questions and ran {checked} code examples.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

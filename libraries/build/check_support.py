"""Run course examples in a disposable copy with Python networking blocked."""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Iterator, Sequence
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "build" / "demo-baseline"
NETWORK_GUARD = '''import os
import sys
from pathlib import Path

def deny_network(event, args):
    if event in {"socket.connect", "socket.getaddrinfo", "socket.sendto"}:
        with Path(os.environ["COURSE_NETWORK_LOG"]).open("a", encoding="utf-8") as log:
            log.write(f"{event}: {args!r}\\n")
        raise RuntimeError("Course check blocked network access")

sys.addaudithook(deny_network)
'''


@contextmanager
def workspace() -> Iterator[tuple[Path, dict[str, str]]]:
    """Keep generated databases, reports and plots out of the working tree."""
    with tempfile.TemporaryDirectory(prefix="libraries-check-") as directory:
        temporary = Path(directory)
        course = temporary / "libraries"
        shutil.copytree(
            ROOT, course,
            ignore=shutil.ignore_patterns(".venv", "build", "__pycache__", "*.db"),
        )
        guard = temporary / "guard"
        guard.mkdir()
        (guard / "sitecustomize.py").write_text(NETWORK_GUARD, encoding="utf-8")
        environment = os.environ | {
            "PYTHONPATH": str(guard), "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8",
            "MPLBACKEND": "Agg", "NO_COLOR": "1", "COLUMNS": "100",
            "COURSE_NETWORK_LOG": str(temporary / "network.log"),
        }
        yield course, environment


def run_case(
    course: Path, environment: dict[str, str], relative: str,
    arguments: Sequence[str] = (), expected: int = 0, label: str = "", stdin: str = "",
    quoted: str = "", stderr_contains: str = "", stdout_empty: bool = False,
    timeout: float = 45,
) -> bool:
    """Record actual output and status; attempted networking fails even when caught."""
    script = course / relative
    network = Path(environment["COURSE_NETWORK_LOG"])
    network.write_text("", encoding="utf-8")
    try:
        result = subprocess.run(
            [sys.executable, str(script), *arguments], cwd=script.parent,
            env=environment, input=stdin, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=timeout, check=False,
        )
        status, stdout, stderr = result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired as error:
        status, stdout, stderr = -1, "", f"Timeout after {error.timeout} seconds"
    attempted = network.read_text(encoding="utf-8")
    # Quoted output may be an excerpt and may wrap differently on a slide.
    # Preserve token order and values while allowing omitted surrounding lines.
    tokens = iter(stdout.split())
    output_matches = all(any(token == wanted for token in tokens) for wanted in quoted.split())
    streams_match = stderr_contains in stderr and (not stdout_empty or not stdout)
    record = {
        "script": relative, "arguments": list(arguments), "expected_status": expected,
        "status": status, "stdout": stdout, "stderr": stderr, "network": attempted,
        "quoted_output_matches": output_matches,
        "streams_match": streams_match,
    }
    destination = BASELINE / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.with_suffix(f".{label or 'default'}.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8",
    )
    passed = status == expected and not attempted and output_matches and streams_match
    print(f"{'PASS' if passed else 'FAIL'} {relative} {label} (exit {status})", flush=True)
    if not passed:
        if not output_matches:
            print(f"Quoted output does not match:\n{quoted}")
        print((attempted or stderr or stdout)[-1200:])
    return passed

"""Check the native Slidev snapshots against their demos and displayed states."""

import contextlib
import io
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def snapshots(name: str, demo: str) -> tuple[str, list[dict[str, object]]]:
    source = (ROOT / "src" / "slidev" / name).read_text(encoding="utf-8")
    demo_lines = (
        (ROOT / "demos" / "03-datastructures" / demo).read_text(encoding="utf-8").splitlines()
    )
    states = []
    for code in re.findall(r"^```python\n(.*?)^```\s*$", source, re.MULTILINE | re.DOTALL):
        for line in code.splitlines():
            if line.strip() and line not in demo_lines:
                raise AssertionError(f"{name}: code line absent from {demo}: {line}")
        namespace: dict[str, object] = {}
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec(compile(code, name, "exec"), namespace)
        namespace["__captured_output__"] = output.getvalue()
        states.append(namespace)
    if not states:
        raise AssertionError(f"{name}: no Python snapshots")
    return source, states


def main() -> None:
    source, states = snapshots("list-mutation.md", "02_updatinglists.py")
    match = re.search(r':states="(\[.*\])"', source)
    assert match is not None
    displayed = json.loads(match[1])
    assert [state["li2"] for state in states] == displayed
    _, states = snapshots("tuple-unpacking.md", "08_destructurewithtuples.py")
    assert (states[-1]["primary"], states[-1]["backup"]) == ("Toxic", "Imagine")
    assert states[-1]["__captured_output__"] == "Toxic\nImagine\n"
    print(
        f"Slidev examples: {len(displayed)} list states and {len(states)} tuple states "
        "match their demos."
    )
    for check in sorted((ROOT / "tests" / "animations" / "probes").glob("check_*.py")):
        subprocess.run([sys.executable, str(check)], check=True)


if __name__ == "__main__":
    main()

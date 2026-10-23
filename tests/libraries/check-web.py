"""Test the web demos, the web solution and its copy of the Wordle package offline."""

import filecmp
import importlib.util
import subprocess
import sys
from pathlib import Path
from types import ModuleType

from check_support import ROOT, workspace
from fastapi.testclient import TestClient

DEMOS = ROOT / "demos" / "09-web-apps"
WORDLE = ROOT.parent / "solutions" / "13-python-libraries" / "wordle"
COPIES = [
    ROOT / "solutions" / "solution09-web-apps" / "wordle",
    ROOT / "exercises" / "starters" / "09-web-apps" / "wordle",
]


def load(name: str) -> ModuleType:
    """Import a demo whose file name starts with a digit."""
    spec = importlib.util.spec_from_file_location(f"demo_{name}", DEMOS / f"{name}.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def same_tree(left: Path, right: Path) -> bool:
    compared = filecmp.dircmp(left, right, ignore=["__pycache__"])
    _, mismatch, errors = filecmp.cmpfiles(left, right, compared.common_files, shallow=False)
    return (
        not compared.left_only and not compared.right_only and not mismatch and not errors
        and all(same_tree(left / name, right / name) for name in compared.common_dirs)
    )


def demo_cases() -> list[tuple[str, str, str, dict[str, str] | None, int, str]]:
    """Each case is a demo, a method, a path, form data, the status and quoted output."""
    return [
        ("01_first_app", "get", "/", None, 200, '{"message":"Hello from the playlist"}'),
        ("04_path_parameters", "get", "/tracks/3", None, 200,
         '{"title":"Respect","artist":"Aretha Franklin"}'),
        ("04_path_parameters", "get", "/tracks/99", None, 404, '{"detail":"No track 99"}'),
        ("04_path_parameters", "get", "/tracks/abc", None, 422, "int_parsing"),
        ("05_query_parameters", "get", "/tracks", None, 200,
         '["Imagine","Yesterday","Respect","Toxic","Thriller"]'),
        ("05_query_parameters", "get", "/tracks?genre=Soul", None, 200,
         '["Respect","Think","Chain of Fools","I Say a Little Prayer"]'),
        ("05_query_parameters", "get", "/tracks?genre=Pop&limit=2", None, 200,
         '["Toxic","Thriller"]'),
        ("02_templates", "get", "/", None, 200, "<li>Jolene by Dolly Parton</li>"),
        ("03_forms", "post", "/", {"title": "Hello", "artist": "Adele"}, 200,
         "<li>Hello by Adele</li>"),
    ]


def main() -> int:
    failed = 0
    for copy in COPIES:
        if not same_tree(WORDLE, copy):
            print(f"FAIL {copy} differs from {WORDLE}")
            failed += 1
    for name, method, path, data, status, quoted in demo_cases():
        client = TestClient(load(name).app)
        response = client.post(path, data=data) if method == "post" else client.get(path)
        passed = response.status_code == status and quoted in response.text
        print(f"{'PASS' if passed else 'FAIL'} {name} {method.upper()} {path}")
        if not passed:
            print(response.status_code, response.text[:400])
        failed += not passed
    with workspace() as (course, environment):
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
             "demos/09-web-apps/06_test_client.py", "solutions/solution09-web-apps"],
            cwd=course, env=environment, check=False,
        )
        failed += result.returncode != 0
    print(f"web checks: {failed} failed")
    return int(failed > 0)


if __name__ == "__main__":
    sys.exit(main())

"""What `uv run` gives you that a bare `python` call does not.

Run this two ways from inside a uv project and compare the output :

    uv run python 01_uv_project.py
    python 01_uv_project.py

The first uses the interpreter in the project's .venv, the second uses
whatever `python` happens to mean on this machine.
"""

import sys
from pathlib import Path

print("interpreter :", sys.executable)
print("version     :", sys.version.split()[0])

# A virtual environment puts its own site-packages first on the import path,
# so this is where `uv add` installs into.
in_venv = sys.prefix != sys.base_prefix
print("in a venv   :", in_venv)
if in_venv:
    print("venv root   :", Path(sys.prefix).name)

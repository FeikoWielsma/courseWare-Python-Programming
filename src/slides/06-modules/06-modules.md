---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Modules
---

# Modules

- A module is a Python file containing related functions and variables
- Other files import the module to reuse those definitions
- `timing.py` holds the duration formatter used by a music player :

```python
SECONDS_PER_MINUTE: int = 60


def format_duration(seconds: int) -> str:
    minutes = seconds // SECONDS_PER_MINUTE
    remainder = seconds % SECONDS_PER_MINUTE
    return f"{minutes}:{remainder:02d}"
```

- The module name is the filename without `.py`
- Keep `timing.py` beside the script that imports it

---

# import Statement

- `import timing` loads the module and binds the name `timing`.
- The module prefix identifies where a function or constant comes from.
- `as` gives a module an alternative name in the calling file.

```python
import timing

print(timing.format_duration(222))  # 3:42
print(timing.format_duration(65))  # 1:05

import timing as clock

print(clock.SECONDS_PER_MINUTE)  # 60
```

> `demo01 · importmodule`

---

# from...import Statement

- `from ... import` binds selected names directly in the calling file.
- Call the function without the module prefix.
- Both import forms load the same module; they differ in the names they bind.
- Explicit names keep dependencies visible; avoid `from timing import *`.

```python
from timing import SECONDS_PER_MINUTE, format_duration

print(format_duration(222))  # 3:42
print(SECONDS_PER_MINUTE)  # 60
```

> `demo02 · usingfromimport`

---

# Locating Modules

- Python searches the directories in `sys.path` for local modules.
- A script's directory is searched before installed packages.
- With `python -m`, the current directory is searched first.
- Keep `timing.py` beside the script that imports it.
- A file named `json.py` can hide the standard library's `json` module.
- `ModuleNotFoundError` means the requested module could not be found.

```python
import sys

print(sys.path[0])
print(sys.executable)
```

> `demo03 · pythonpath`

---

# Using Modules

- A playlist display reuses the formatter without copying its calculation :
  - The calling script supplies track titles and lengths
  - The module formats each length consistently

```python
from timing import format_duration

tracks = {"Imagine": 183, "Yesterday": 125}
for title, seconds in tracks.items():
    label = format_duration(seconds)
    print(f"{title}: {label}")
```

```text
Imagine: 3:03
Yesterday: 2:05
```

- Updating the formatter in one module updates every caller

> `demo04 · usingmodules`

---

# dir Function

- `dir(module)` lists the names available on a module.
- Explore a module in the REPL before calling an unfamiliar function.
- Names starting and ending with double underscores include module metadata.

```python
import timing

print("format_duration" in dir(timing))  # True
print("SECONDS_PER_MINUTE" in dir(timing))  # True
```

> `demo05 · usingdir`

---

# Packages in Python

- A package groups related modules in one directory.
- A regular package contains an `__init__.py` file; it may be empty.

```text
player/
├── __init__.py
├── timing.py     the format_duration function
└── __main__.py     the command-line entry point
```

- Move the existing `timing.py` into `player/` to group reporting code.
- `__init__.py` runs when the package is first imported.
- A module's top-level code runs on its first import in a Python process.

---

# Explicit Import of Package Modules

- Dots in an import follow directories in the package.
- `player.timing` refers to `player/timing.py`.
- The full call is `package.module.function()`.

```python
import player.timing

print(player.timing.format_duration(222))  # 3:42
```

> `demo06 · explicitimport`

---

# Importing Names from a Package

- A package can expose selected functions from its internal modules.
- `player/__init__.py` contains this import :

```python
from player.timing import format_duration
```

- Callers can then use the shorter package-level name.

```python
import player

print(player.format_duration(222))  # 3:42

from player import format_duration

print(format_duration(65))  # 1:05
```

> `demo07 · implicitimport`

---

# Running a Module Directly

- `__name__` is `"__main__"` when a file runs directly.
- When imported, `__name__` is the module's name.
- The guard runs `main()` only for direct execution.
- Importing defines `main` without printing the playlist display.

```python
from timing import format_duration


def main() -> None:
    print(f"Duration: {format_duration(222)}")


if __name__ == "__main__":
    main()
```

> `demo08 · testharness`

---

# Running Packages with python -m

- A package's `__main__.py` is its entry point.
- The following code belongs in `player/__main__.py`.
- Run from the directory containing `player/` :

```bash
uv run python -m player
```


```python
from player.timing import format_duration


def main() -> None:
    print(f"Duration: {format_duration(222)}")


if __name__ == "__main__":
    main()
```

> `demo09 · package_main`

---

# Installing Packages

- Third-party packages are hosted on PyPI and installed with `uv add` :
  - `uv add package` installs a package and records it in `pyproject.toml`
  - `uv add --dev package` adds a development tool, such as `pytest`
  - `uv remove package` uninstalls a dependency
- Two files track dependencies and belong in version control :
  - `pyproject.toml` declares the project's direct requirements
  - `uv.lock` records the exact resolved versions for reproducibility
- Anyone with the project can reproduce the exact environment :

```bash
uv add requests
uv add "requests>=2.28,<3"
uv add --dev pytest
uv sync          # install exactly what uv.lock says
uv remove requests
```

---

# Virtual Environments

- Virtual environments isolate dependencies per project :
  - Each project has its own libraries and Python executable
  - Different projects can require different versions without conflict
- `uv` manages virtual environments automatically :
  - `.venv/` is created on the first `uv run` or `uv add`
  - Packages are installed into `.venv/` without touching system Python
- There is no environment to activate manually :
  - `uv run` puts the project's `.venv` in front for the command

```text
myproject/
├── pyproject.toml   dependencies declared for this project
├── uv.lock          pinned versions of all installed packages
└── .venv/           created on the first uv run or uv add
```

- Run code through `uv run`, which uses the project's interpreter :

```bash
uv run python app.py
```

- Without `uv`, environments are made by `python -m venv .venv` and activated by hand

---

# Summary : Modules

- Modules organize code into reusable files :
  - A module is a `.py` file defining functions, classes and variables
  - `import` and `from ... import` bring names into the calling file
- Python locates modules using `sys.path` :
  - Script directory (current directory for REPL or `-m`), then `PYTHONPATH` and defaults
  - `dir()` lists the names defined or imported in a module
- Packages group modules into directories with `__init__.py` :
  - Modules inside packages use dotted import paths
  - `python -m package` runs a package via its `__main__.py`
- Executing versus importing :
  - `if __name__ == "__main__":` guards code that only runs when executed directly
- Dependency and environment management :
  - `uv add` installs packages into an automatic `.venv`
  - `uv run` executes commands with the project's environment active

> `exercise06 · Modules`

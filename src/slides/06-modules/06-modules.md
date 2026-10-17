---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Modules
---

# Modules

- A module is a Python file containing related functions and variables.
- Other files import the module to reuse those definitions.
- `shipping.py` holds the delivery rule for an order :

```python
FREE_SHIPPING: float = 50.0


def delivery_cost(total: float) -> float:
    if total >= FREE_SHIPPING:
        return 0.0
    return 4.95
```

- The module name is the file name without `.py`.
- Put `shipping.py` and the script that imports it in the same directory.

---

# import Statement

- `import shipping` loads the module and binds the name `shipping`.
- The module prefix identifies where a function or constant comes from.
- `as` gives a module an alternative name in the calling file.

```python
import shipping

print(shipping.delivery_cost(35.0))  # 4.95
print(shipping.delivery_cost(75.0))  # 0.0

import shipping as delivery

print(delivery.FREE_SHIPPING)  # 50.0
```

> `demo01 · importmodule`

---

# from...import Statement

- `from ... import` binds selected names directly in the calling file.
- Call the function without the module prefix.
- Both import forms load the same module; they differ in the names they bind.
- Explicit names keep dependencies visible; avoid `from shipping import *`.

```python
from shipping import FREE_SHIPPING, delivery_cost

print(delivery_cost(35.0))  # 4.95
print(FREE_SHIPPING)  # 50.0
```

> `demo02 · usingfromimport`

---

# Locating Modules

- Python searches the directories in `sys.path` for local modules.
- A script's directory is searched before installed packages.
- With `python -m`, the current directory is searched first.
- Keep `shipping.py` beside the script that imports it.
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

- Several programs can reuse `shipping.py` without copying the function.
- The order report supplies the data; the shipping module applies the rule.
- Changing the delivery rule in one module updates every caller.

```python
from shipping import delivery_cost

order_totals = [35.0, 75.0]
for total in order_totals:
    fee = delivery_cost(total)
    print(f"Order {total:.2f}: delivery {fee:.2f}")
```

> `demo04 · usingmodules`

---

# dir Function

- `dir(module)` lists the names available on a module.
- Explore a module in the REPL before calling an unfamiliar function.
- Names starting and ending with double underscores include module metadata.

```python
import shipping

print("delivery_cost" in dir(shipping))  # True
print("FREE_SHIPPING" in dir(shipping))  # True
```

> `demo05 · usingdir`

---

# Packages in Python

- A package groups related modules in one directory.
- A regular package contains an `__init__.py` file; it may be empty.

```text
reports/
├── __init__.py
├── shipping.py     the delivery_cost function
└── __main__.py     the command-line entry point
```

- Move the existing `shipping.py` into `reports/` to group reporting code.
- `__init__.py` runs when the package is first imported.
- A module's top-level code runs on its first import in a Python process.

---

# Explicit Import of Package Modules

- Dots in an import follow directories in the package.
- `reports.shipping` refers to `reports/shipping.py`.
- The full call is `package.module.function()`.

```python
import reports.shipping

print(reports.shipping.delivery_cost(35.0))  # 4.95
```

> `demo06 · explicitimport`

---

# Importing Names from a Package

- A package can expose selected functions from its internal modules.
- `reports/__init__.py` contains this import :

```python
from reports.shipping import delivery_cost
```

- Callers can then use the shorter package-level name.

```python
import reports

print(reports.delivery_cost(35.0))  # 4.95

from reports import delivery_cost

print(delivery_cost(75.0))  # 0.0
```

> `demo07 · implicitimport`

---

# Running a Module Directly

- `__name__` is `"__main__"` when a file runs directly.
- When imported, `__name__` is the module's name.
- The guard runs `main()` only for direct execution.
- Importing defines `main` without printing the delivery report.

```python
from shipping import delivery_cost


def main() -> None:
    print(f"Delivery: {delivery_cost(35.0):.2f}")


if __name__ == "__main__":
    main()
```

> `demo08 · testharness`

---

# Running Packages with python -m

- A package's `__main__.py` is its entry point.
- The following code belongs in `reports/__main__.py`.
- Run from the directory containing `reports/` :

```bash
uv run python -m reports
```


```python
from reports.shipping import delivery_cost


def main() -> None:
    print(f"Delivery: {delivery_cost(35.0):.2f}")


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

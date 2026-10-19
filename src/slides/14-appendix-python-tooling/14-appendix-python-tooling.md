---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Python Tooling and Reference
appendix: true
---

# Python Tooling and Reference

- `uv` manages Python versions, project environments and installed packages
- Ruff checks source code and applies consistent formatting
- Project files record Python versions and package requirements
- The syntax reference covers names, blocks and multiline statements
- Tool documentation :
  - `https://docs.astral.sh/uv/`
  - `https://docs.astral.sh/ruff/`

---

# Python Features

- Broad standard library :
  - Files, paths, dates, JSON, CSV, regular expressions, SQLite and testing out of the box
- Portable :
  - The same code runs on Linux, Windows and macOS
- Large ecosystem :
  - Hundreds of thousands of packages on PyPI, installed with `uv add`
- Used across many fields :
  - Automation and scripting, web back ends, data analysis, machine learning, testing
- Extendable :
  - Performance-critical parts can be written in C or Rust and called from Python
- Automatic memory management :
  - Objects are freed by reference counting and a garbage collector, not by hand

---

# History of Python

- Python was developed by Guido van Rossum around 1990 at :
  - National Research Institute for Mathematics and Computer Science in Netherlands
- Python is derived from many other languages :
  - Including Modula-3, C, C++, Smalltalk, Unix shell and other scripting languages
- Python is usable as :
  - Scripting language or compiled to byte-code for building large applications
- Python is copyrighted and the source is open :
  - Released under the PSF License, a permissive licence that allows commercial use
- Python is developed in the open by a community of core developers :
  - The Python Software Foundation holds the rights, the Steering Council decides
- Python supports :
  - Functional and structured programming methods as well as OOP
  - Very high-level dynamic data types and dynamic type checking

---

# Modern Python Tooling

- Python needs an interpreter, an environment and a set of packages :
  - Historically each of these was installed and managed by a separate tool
  - The result was hard to reproduce on a second machine
- Two tools now cover almost all of it :
  - `uv` installs Python, creates the environment and resolves the packages
  - `ruff` checks style and catches a large class of mistakes before you run
- Both are single binaries with no Python of their own to bootstrap :

| Older tool | Replaced by |
|---|---|
| `python.org` installer, `pyenv` | `uv python install` |
| `venv`, `virtualenv` | `uv` creates `.venv` for you |
| `pip`, `pip-tools`, `requirements.txt` | `uv add` and `uv.lock` |
| `flake8`, `isort`, `black`, `pylint` | `ruff check` and `ruff format` |

---

# Getting Started

- Install `uv` once, and let it install Python for you :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

- On macOS or Linux use the shell installer :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Close and reopen the terminal, then fetch the interpreter :

```bash
uv python install 3.14
```

- This needs no administrator rights :
  - Any Python already on the machine is left alone, and versions live side by side
- The traditional route is the installer from `https://www.python.org/` :
  - Tick `Add python.exe to PATH` on the first page of the Windows wizard
  - Python 2 reached its end of life in 2020, so Python 3 is the only choice
- Documentation lives at `https://docs.python.org/3/`

---

# Setting up PATH

- Only needed when Python was installed by hand :
  - `uv run` finds its managed Python; the `uv` command itself must be on PATH
- PATH is an environment variable :
  - Provides a search path that lists directories that OS searches for executables
  - Named PATH in Unix or Path in Windows, and Unix is case-sensitive
- Setting PATH in Linux :

```bash
export PATH="$PATH:/usr/local/bin"
```

- Setting PATH in Windows :

```powershell
$env:Path += ";C:\Python"
```

  - Or use the environment variables tab under System Properties
- PYTHONPATH is a separate variable :
  - It tells the interpreter where to find modules you import, not where Python is

---

# Project Files

- A project is a directory with a `pyproject.toml` in it :

```bash
uv init course-work
cd course-work
```

- `uv init` writes three things :
  - `pyproject.toml` , the file that names the project and its dependencies
  - `.python-version` , the interpreter this project is pinned to
  - `main.py` , a placeholder to delete or edit

```text
course-work/
├─ pyproject.toml
├─ .python-version
├─ main.py
└─ .venv/            created on the first uv run or uv add
```

- Run code through `uv run`, which uses the project's own interpreter :

```bash
uv run python main.py
```

---

# Adding Dependencies

- `uv add` installs a package and records it in `pyproject.toml` :

```bash
uv add requests
uv add "requests>=2.28,<3"
uv add --dev pytest
```

- Two files describe the dependencies, and both belong in version control :
  - `pyproject.toml` states what the project asks for
  - `uv.lock` states the exact versions that were resolved
- Anyone can then reproduce the environment exactly :

```bash
uv sync          # install exactly what uv.lock says
uv remove requests
```

- `--dev` marks a tool used while developing, not by the running program :
  - `ruff` is such a tool; so is the test runner `pytest`, which the libraries appendix covers
- There is no environment to activate :
  - `uv run` puts the project's `.venv` in front for the length of one command

> `demo01 · uv_project`

---

# Linting with ruff

- A linter reads code without running it and reports what looks wrong :
  - Unused imports and variables, shadowed built-ins, unreachable code
  - Style that departs from the conventions the rest of Python follows
- Two commands cover the daily use :

```bash
uv run ruff check .          # report problems
uv run ruff check . --fix    # fix the ones that are safe to fix
uv run ruff format .         # lay the code out consistently
```

- Rules are configured in `ruff.toml`, which ships with this course :
  - It selects the rule set the course material is written against
  - Without it the editor would flag patterns the course uses on purpose

> `demo02 · ruff_findings`

---

# Editor Integration

- The course demonstrates Visual Studio Code :
  - Any editor works, but the slides assume this one
- Install two extensions from the Extensions panel :
  - `Python` , published by Microsoft
  - `Ruff` , published by Astral
- With both installed the editor will :
  - Underline the problems `ruff check` would report, as you type
  - Offer the same fixes, and format on save if you ask it to
  - Resolve imports against the project's `.venv` rather than a global Python
- Point the editor at the project interpreter :
  - Command Palette, `Python: Select Interpreter`, choose the one in `.venv`

---

# Python Identifiers

- Identifiers are the names of variables, functions, classes and modules :
  - Start with a letter or an underscore, followed by letters, digits and underscores
  - Punctuation such as `@`, `$` and `%` is not allowed in a name
- Python is case sensitive :
  - `total` and `Total` are two different names
- The naming conventions of PEP 8, the Python style guide :
  - `snake_case` for variables, functions and modules
  - `CapWords` for classes, `UPPER_CASE` for values meant as constants
- Underscores carry meaning :
  - A leading underscore, as in `_cache`, marks a name as internal to its module
  - Names such as `__init__` with two underscores on both sides are defined by Python

---

# Python Reserved Words

- Keywords may not be used as a variable, function or other name :

```text
False    None     True     and      as       assert   async
await    break    class    continue def      del      elif
else     except   finally  for      from     global   if
import   in       is       lambda   nonlocal not      or
pass     raise    return   try      while    with     yield
```

- `match`, `case`, `type` and `_` are soft keywords :
  - Reserved only inside the statement they belong to, and usable as names elsewhere
- The interpreter can list them : `import keyword` and print `keyword.kwlist`

---

# Lines and Indentation

- Indentation groups statements into a block :
  - Use four spaces for each level
  - Statements in the same block have the same indentation

```python
if True:  # The indented block runs.
    print("Photo ready")
else:
    print("Photo missing")
```

- An unindented statement runs after the block :

```python
photos = 5
# This comment does not change the photo count.
print("Photos selected:", photos)
```

- Inconsistent indentation raises an error before the script runs
- `end=" "` makes the next output continue on the same line

> `demo03 · lines_and_identation`

---

# Multi Line Statements

- Parentheses allow a calculation to continue across lines :

```python
thriller = 357
imagine = 183
yesterday = 125

total = (
    thriller + imagine + yesterday
)
print(total)  # 665
```

- Lists, dictionaries and calls can also span lines inside their brackets :

```python
playlist = [
    "Thriller", "Imagine", "Yesterday",
]
print(playlist)
```

- A backslash also continues a line :
  - Prefer brackets when they fit the statement
  - A semicolon separates statements on one line; separate lines are clearer

> `demo04 · multilinestatements`

---

# String Quote Forms

- Matching quotes mark the start and end of a string :
  - Single and double quotes produce the same string type
  - Triple quotes allow the text to span lines

```python
title = "Imagine"
filename = 'cover.jpg'
caption = """Friday night
Live at the observatory"""
```

- Choose double quotes when the text contains an apostrophe :

```python
print("Tonight's playlist")
print('Tonight\'s playlist')
```

> `demo05 · quotesandescapes`

---

# Python Execution

- The interpreter processes Python source code when a program runs :
  - Python checks the syntax before executing a script
  - CPython compiles source code to bytecode internally
  - Its virtual machine executes the bytecode
- Imported modules can have cached bytecode in `__pycache__` :
  - The cache avoids recompiling unchanged source on a later import
  - A separate compile command is unnecessary for running a `.py` file

---

# Formatting Text Columns

- A format specification can choose a fill character, alignment and width :
  - `*^20` centres text in twenty characters, filling the remaining space with `*`

```python
title = "Imagine"
print(f"{title:*^20}")
```

- `!s` converts a value to text before applying its display format :
  - A Boolean with a width otherwise displays as `1` or `0`

```python
selected = True
print(f"{selected:^8}")
print(f"{selected!s:^8}")
```

- `!s:^8` first produces `"True"`, then centres it in eight characters

> `demo06 · text_columns`

---

# Environment Variables

- An environment variable is a named text setting passed to a running program
- `os.environ` gives access to those settings :
  - `get` returns the setting, or its default when the name is absent

```python
import os

title = os.environ.get("TRACK_TITLE", "Imagine")
print(title)
```

- PowerShell sets a variable for subsequent commands in the same terminal :

```powershell
$env:TRACK_TITLE = "Yesterday"
```

- Bash can set a variable for one run :

```bash
TRACK_TITLE=Yesterday uv run python 07_environment.py
```

> `demo07 · environment`

---

# Summary : Python Tooling

- `uv run` uses the project's Python environment
- `uv add` records packages in `pyproject.toml`
- `uv.lock` records resolved package versions
- Ruff checks code without running it and can format files
- Python names are case sensitive and follow naming conventions
- Indentation groups statements; brackets allow multiline statements

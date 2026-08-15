---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Python Tooling
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

# Installing uv

- Install `uv` once, and let it install everything else :

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

- On macOS or Linux use the shell installer :

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Close and reopen the terminal so that `uv` is on the `PATH`
- Let `uv` fetch the interpreter this course uses :

```bash
uv python install 3.14
```

- This needs no administrator rights :
  - Any Python already on the machine is left alone
  - Several versions can live side by side

---

# Creating a Project

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

# Editor Setup

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

# Summary : Python Tooling

- `uv` manages the interpreter, the environment and the packages :
  - `uv python install` installs an interpreter without administrator rights
  - `uv init` creates the project, `uv add` records a dependency
  - `uv sync` reproduces the environment from `uv.lock`
  - `uv run` uses the project's own interpreter, so nothing is ever activated
- `pyproject.toml` states what the project asks for :
  - `uv.lock` states the exact versions that were resolved
  - Both belong in version control
- `ruff` reports style and correctness problems without running the code :
  - `ruff check .` reports, `ruff check . --fix` repairs what is safe to repair
  - `ruff format .` lays the code out consistently
  - Rules come from `ruff.toml`, which ships with this course
- The editor reads the same configuration :
  - VS Code with the Microsoft `Python` and Astral `Ruff` extensions

> `exercise01 · Python Tooling`

---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Modern Python
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

# Why Type Hints

- Python is dynamically typed and stays that way :
  - A name refers to an object, and the object carries the type
  - Nothing forces a parameter to be the type the author had in mind
- A type hint records that intent in the signature :

```python
def apply_discount(price: float, percent: float) -> float:
    return price * (1 - percent / 100)
```

- The value is that the intent cannot drift away from the code :
  - A comment saying "price is a float" goes stale, a hint does not
  - The editor can complete, rename and navigate with far more confidence
  - A checker can read the whole program and find the mismatches

---

# Basic Type Syntax

- A variable is annotated with a colon and the intended type :

```python
age: int = 25
height: float = 1.87
name: str = "Alice"
is_student: bool = True
```

- A function states its parameters and its result :
  - Each parameter takes a colon, the result takes an arrow

```python
def area(width: float, height: float) -> float:
    return width * height
```

- A function that returns nothing is annotated `None` :

```python
def log_message(message: str) -> None:
    print(message)
```

> `demo03 · annotations`

---

# Typing Collections

- The built-in container types are written with the element type in brackets :

```python
scores: list[int] = [10, 20, 30]
names: set[str] = {"Alice", "Bob"}
ages: dict[str, int] = {"Alice": 30, "Bob": 25}
```

- A tuple states the type of every position it has :

```python
point: tuple[int, int] = (3, 4)
row: tuple[str, int, float] = ("Audi", 2019, 52643.0)
```

- A tuple of unknown length repeats one type with an ellipsis :

```python
readings: tuple[float, ...] = (1.5, 2.5, 3.5, 4.5)
```

> `demo04 · collections`

---

# Optional Values

- A parameter that may be absent is typed with `| None` :

```python
def greet(name: str | None = None) -> str:
    if name is None:
        return "Hello, stranger"
    return f"Hello, {name}"
```

- The default `None` is what makes the annotation necessary :
  - Writing `name: str = None` claims a type the default violates
- The same notation describes a value of either of two types :

```python
def parse(value: str | int) -> int:
    return int(value)
```

> `demo05 · optional`

---

# Hints Are Not Enforced

- The interpreter ignores annotations while the program runs :
  - No conversion happens, and no check happens
  - A wrong type is passed just as happily as a right one

```python
def double(n: int) -> int:
    return n * 2

print(double("ab"))   # prints abab, no error is raised
```

- Annotations are stored, and can be read at runtime :

```python
print(double.__annotations__)   # {'n': <class 'int'>, 'return': <class 'int'>}
```

- So a hint is worth exactly as much as the tooling that reads it :
  - Which is why the next slide runs a checker over it

> `demo06 · not_enforced`

---

# Checking with mypy

- `mypy` reads the annotations and reports what does not agree :

```bash
uv add --dev mypy
uv run mypy 07_mypy_error.py
```

- Given a call that contradicts the signature :

```python
def double(n: int) -> int:
    return n * 2

result: int = double("ab")
```

- The checker reports it without the program ever running :

```text
error: Argument 1 to "double" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

> `demo07 · mypy_error`

---

# Summary : Modern Python

- `uv` manages the interpreter, the environment and the packages :
  - `uv python install` , `uv init` , `uv add` , `uv sync` , `uv run`
  - `pyproject.toml` states what is wanted, `uv.lock` pins what was resolved
- `ruff` reports style and correctness problems without running the code :
  - `ruff check .` and `ruff check . --fix` , configured in `ruff.toml`
- Type hints record in the signature what a function expects and returns :
  - `age: int` for a variable, `def f(a: int) -> str` for a function
  - `list[int]` , `dict[str, int]` and `tuple[int, int]` for containers
  - `str | None` for a value that may be absent
- Annotations are ignored at runtime :
  - Their value comes from the editor and from a checker such as `mypy`

> `exercise01 · Modern Python`

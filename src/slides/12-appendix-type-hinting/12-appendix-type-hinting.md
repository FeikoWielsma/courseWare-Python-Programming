---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Type Hinting
appendix: true
---

# Type Hinting Recap

- Annotations have appeared throughout the course, module by module :
  - Variables in Variables and Data Types, `age: int = 25`
  - Collections in Data Structures, `list[int]` and `dict[str, int]`
  - Signatures in Functions, `def area(w: float, h: float) -> float`
  - Constructors and methods in Classes, `def __init__(self, name: str) -> None`
- This appendix gathers them up and adds the three things left over :
  - A value that may be absent, a closed set of literal values, and a checker
- Python is dynamically typed and stays that way :
  - A name refers to an object, and the object carries the type
  - Nothing forces a parameter to be the type the author had in mind
- What an annotation buys is that the intent cannot drift from the code :
  - A comment saying "price is a float" goes stale, an annotation does not
  - The editor completes, renames and navigates with far more confidence
  - A checker reads the whole program and finds the mismatches

---

# Basic Type Syntax

- To recap, a variable is annotated with a colon and the intended type :

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

> `demo01 · annotations`

---

# Typing Collections

- And a container is written with the type of what it holds in brackets :

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

> `demo02 · collections`

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

> `demo03 · optional`

---

# Hints Are Not Enforced

- The interpreter ignores annotations while the program runs :
  - No conversion happens, and no check happens
  - A wrong type is passed just as happily as a right one

```python
def double(n: int) -> int:
    return n * 2


print(double("ab"))  # prints abab, no error is raised
```

- Annotations are stored, and can be read at runtime :

```python
print(double.__annotations__)  # {'n': <class 'int'>, 'return': <class 'int'>}
```

- So a hint is worth exactly as much as the tooling that reads it :
  - Which is why the next slide runs a checker over it

> `demo04 · not_enforced`

---

# Checking with mypy

- `mypy` reads the annotations and reports what does not agree :

```bash
uv add --dev mypy
uv run mypy 05_mypy_error.py
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

> `demo05 · mypy_error`

---

# Closed Sets with Literal

- `typing.Literal` restricts a type to an exact set of allowed values :
  - A plain `str` accepts any text, whereas `Literal` rejects any value outside the declared options

```python
from typing import Literal

type TrafficLight = Literal["red", "amber", "green"]


def change_light(color: TrafficLight) -> None:
    print(f"Traffic light is now {color}")


change_light("green")
change_light("blue")
```

- When checked with `mypy`, a value outside the set is flagged immediately :

```text
06_literal.py:23: error: Argument 1 to "change_light" has incompatible type "Literal['blue']"; expected "Literal['red', 'amber', 'green']"
Found 1 error in 1 file (checked 1 source file)
```

> `demo06 · literal`

---

# Summary : Type Hinting

- `uv` manages the interpreter, the environment and the packages :
  - `uv python install` , `uv init` , `uv add` , `uv sync` , `uv run`
  - `pyproject.toml` states what is wanted, `uv.lock` pins what was resolved
- `ruff` reports style and correctness problems without running the code :
  - `ruff check .` and `ruff check . --fix` , configured in `ruff.toml`
- Type hints record in the signature what a function expects and returns :
  - `age: int` for a variable, `def f(a: int) -> str` for a function
  - `list[int]` , `dict[str, int]` and `tuple[int, int]` for containers
  - `str | None` for a value that may be absent
  - `Literal["red", "amber", "green"]` for a closed set of literal values
- Annotations are ignored at runtime :
  - Their value comes from the editor and from a checker such as `mypy`

> `exercise12 · Type Hinting`

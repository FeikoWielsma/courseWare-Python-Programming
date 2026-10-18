---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Type Hinting
appendix: true
---

# Type Hinting Recap

- Type hints have appeared alongside the examples throughout the course :
  - Values such as `seconds: int = 222`
  - Collections such as `list[str]` and `dict[str, int]`
  - Functions such as `format_duration(seconds: int) -> str`
  - Constructors and methods in Classes
- An annotation records the intended type :
  - Editors use it for completion and navigation
  - A checker finds code that contradicts it
  - Python does not enforce it while the program runs
- This appendix adds optional values, closed sets and a checker

---

# Basic Type Syntax

- A colon introduces a variable or parameter type; an arrow introduces the result :

```python
def format_duration(seconds: int) -> str:
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder:02d}"
```

- `None` describes a function without a useful returned result :

```python
def print_playlist(name: str, tracks: list[str]) -> None:
    print(f"Playlist: {name}")
    for number, title in enumerate(tracks, start=1):
        print(f"{number}. {title}")
```

- Variable annotations use the same types : `seconds: int = 222`

> `demo01 · annotations`

---

# Typing Collections

- Collections state the types of their contents :

```python
tracks: list[str] = ["Imagine", "Yesterday", "Respect"]
favourites: set[str] = {"Imagine", "Yesterday"}
durations: dict[str, int] = {"Imagine": 183, "Yesterday": 125}
```

- A tuple describes each position; an ellipsis allows any length of one type :

```python
photo_size: tuple[int, int] = (1920, 1080)
track: tuple[str, int] = ("Imagine", 183)
album_lengths: tuple[int, ...] = (183, 125, 149)
```

- The dictionary type gives the key type first, then the value type

> `demo02 · collections`

---

# Optional Values

- A lookup may return a duration or no value :

```python
def find_duration(title: str, durations: dict[str, int]) -> int | None:
    return durations.get(title)
```

- Test for `None` before using the duration :

```python
durations = {"Imagine": 183, "Yesterday": 125}
seconds = find_duration("Wonderwall", durations)
if seconds is None:
    print("Track not found")
else:
    print(f"Track length: {seconds} seconds")
print(parse_seconds("222"))
```

- `str | int` similarly accepts either a string or an integer
- A default value is separate from the type; `| None` does not make an argument optional to pass

> `demo03 · optional`

---

# Hints Are Not Enforced

- A wrong type can reach the function without an immediate runtime error :

```python
def repeat_track(title: str, count: int) -> list[str]:
    return [title] * count


print(repeat_track(222, 2))  # [222, 222], despite the str annotation.
```

- The result contains numbers even though the return type says `list[str]`
- Annotations do not convert or validate incoming values
- Annotations remain available through `repeat_track.__annotations__`
- A checker can report the mismatch before this program runs

> `demo04 · not_enforced`

---

# Checking with mypy

- `mypy` checks calls against the declared parameter types :

```python
def repeat_track(title: str, count: int) -> list[str]:
    return [title] * count


queue: list[str] = repeat_track(222, 2)
```

```bash
uv add --dev mypy
uv run mypy 05_mypy_error.py
```

```text
error: Argument 1 to "repeat_track" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
```

> `demo05 · mypy_error`

---

# Closed Sets with Literal

- `Literal` lets a checker restrict a value to specific options :
  - This player implements normal playback and repeating the current track

```python
from typing import Literal

type PlaybackMode = Literal["normal", "repeat"]


def next_index(index: int, mode: PlaybackMode) -> int:
    if mode == "repeat":
        return index
    return index + 1


print(next_index(0, "repeat"))
print(next_index(0, "shuffle"))  # Deliberate checker error.
```

- `mypy` flags `"shuffle"` because it is outside the declared options
- Runtime validation still needs ordinary Python checks

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
  - `Literal["normal", "repeat"]` for a closed set of literal values
- Annotations are ignored at runtime :
  - Their value comes from the editor and from a checker such as `mypy`

> `exercise12 · Type Hinting`

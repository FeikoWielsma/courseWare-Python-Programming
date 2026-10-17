---
marp: true
theme: spiraltrain
size: 16:10
paginate: true
footer: Python Libraries
appendix: true
---

# Standard Library Overview

- Python ships with a large standard library :
  - Available on every installation, with nothing to add and nothing to pin
  - Reach for it before reaching for a third party package
- The modules this appendix covers :
  - `datetime` , dates, times and the arithmetic between them
  - `json` , reading and writing the interchange format of the web
  - `re` , regular expressions for searching and rewriting text
  - `sys.argv` , inspecting command-line arguments passed to a script
- `pytest` is third-party software for testing with plain assertions :
  - Exercise 5 installs it with `uv add --dev pytest`
- Others worth knowing about :
  - `pathlib` for filesystem paths, `csv` for tabular files
  - `collections` for counters, deques and default dictionaries
  - `itertools` for combinations, grouping and infinite sequences
  - `argparse` for flags, options and generated help messages
- Full reference at `https://docs.python.org/3/library/`

---

# The datetime Module

- Three types cover almost every need :
  - `date` is a calendar day with no time on it
  - `time` is a time of day with no date on it
  - `datetime` is both together

```python
from datetime import date, datetime, time

today = date(2026, 8, 15)
midday = time(12, 30, 0)
launch = datetime(2026, 8, 15, 12, 30, 0)

print(launch.year, launch.month, launch.day)
print(launch.weekday())  # Monday is 0, so this prints 5
```

- The current moment comes from the class itself :
  - `date.today()` and `datetime.now()`

> `demo01 Â· datetime_basics`

---

# Formatting and Parsing Dates

- `strftime` formats a datetime as text, `strptime` reads text back :
  - The `f` is for format, the `p` is for parse

```python
launch.strftime("%d-%m-%Y %H:%M")  # 15-08-2026 12:30
launch.strftime("%A %d %B %Y")     # Saturday 15 August 2026

datetime.strptime("24-12-2026 18:00", "%d-%m-%Y %H:%M")
```

- Common directives :
  - `%Y` four digit year, `%m` month, `%d` day
  - `%H` hour, `%M` minute, `%S` second
  - `%A` weekday name, `%B` month name
- ISO 8601 needs no format string in either direction :

```python
launch.isoformat()  # 2026-08-15T12:30:00
datetime.fromisoformat("2026-12-24T18:00:00")
```

> `demo02 Â· datetime_format`

---

# Date Arithmetic with timedelta

- Subtracting two dates gives a `timedelta`, a duration :

```python
from datetime import date, timedelta

start = date(2026, 8, 15)
end = date(2026, 12, 24)
span = end - start
print(span.days)  # 131
```

- Adding a `timedelta` to a date gives another date :

```python
start + timedelta(weeks=1)   # 2026-08-22
start + timedelta(days=100)  # 2026-11-23
start - timedelta(days=1)    # 2026-08-14
```

- A `timedelta` is built from any combination of units :
  - `days` , `hours` , `minutes` , `seconds` , `weeks`
  - It normalises itself, so 25 hours becomes one day and one hour

> `demo03 Â· datetime_arithmetic`

---

# The json Module

- JSON is the interchange format most web services speak :
  - Text, language independent, and mapped closely onto Python types
- `dumps` writes a string, `loads` reads one :

```python
import json

book = {"title": "Fluent Python", "pages": 1012, "sequel": None}
text = json.dumps(book, indent=2, sort_keys=True)
restored = json.loads(text)
```

- `indent` and `sort_keys` are for people reading the output :
  - Leave them out and the result is compact, which is what you send

```text
{
  "pages": 1012,
  "sequel": null,
  "title": "Fluent Python"
}
```

> `demo04 Â· json_strings`

---

# Reading and Writing JSON Files

- `dump` and `load` take a file object rather than a string :
  - The names are the same without the trailing `s`

```python
import json
from pathlib import Path

path = Path("book.json")

with path.open("w", encoding="utf-8") as f:
    json.dump(book, f, indent=2)

with path.open(encoding="utf-8") as f:
    restored = json.load(f)
```

- Always give an encoding :
  - JSON is defined as UTF-8, and the platform default may not be
- The four names are worth memorising :
  - `dumps` and `loads` for strings, `dump` and `load` for files

> `demo05 Â· json_files`

---

# JSON and Python Types

- The mapping between the two type systems is not quite one to one :

| Python | JSON |
|---|---|
| `dict` | object |
| `list` , `tuple` | array |
| `str` | string |
| `int` , `float` | number |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

- Note what this costs on a round trip :
  - A `tuple` comes back as a `list`
  - Dictionary keys come back as strings, whatever they went in as
  - `set`, `datetime` and your own classes are not serialisable at all
- For those, convert to a supported type first, or pass `default=`

---

# Regular Expressions with re

- A regular expression is a pattern describing a set of strings :
  - Written as a raw string, `r"..."`, so backslashes reach the engine intact
- The character classes that do most of the work :
  - `\d` digit, `\w` word character, `\s` whitespace
  - `.` any character, `[abc]` one of these, `[^abc]` none of these
- The repetition operators :
  - `*` zero or more, `+` one or more, `?` zero or one
  - `{3}` exactly three, `{2,4}` between two and four
- Anchors tie a pattern to a position :
  - `^` start of the string, `$` end of the string, `\b` word boundary

```python
r"\d{4}-\d{2}-\d{2}"   # a date like 2026-08-15
r"^\w+@\w+\.\w{2,4}$"  # a very rough email address
```

---

# Matching and Searching

- Four functions cover most use, and they differ in where they look :

```python
import re

text = "Order 1234 shipped, order 5678 pending"

re.match(r"Order", text)     # only tries position zero
re.match(r"shipped", text)   # None, even though the word is present
re.search(r"shipped", text)  # scans the whole string, finds it
re.findall(r"\d+", text)     # ['1234', '5678']
print(re.fullmatch(r"[a-z]+", "hello") is not None)  # True; whole string
print(re.fullmatch(r"[a-z]+", "hello!") is not None)  # False
```

- `match`, `fullmatch` and `search` return a match object, or `None` :
  - So the result is tested before it is used
- Flags change how the pattern is applied :
  - `re.IGNORECASE` , `re.MULTILINE` , `re.DOTALL`

> `demo06 Â· regex_search`

---

# Groups and Capturing

- Parentheses capture the part of the match you actually want :

```python
line = "2026-08-15 12:30 ERROR disk full"
m = re.search(r"(\d{4})-(\d{2})-(\d{2}) (\d{2}:\d{2}) (\w+) (.*)", line)

m.group(0)  # the whole match
m.group(1)  # 2026, the first group
m.groups()  # ('2026', '08', '15', '12:30', 'ERROR', 'disk full')
```

- Named groups read better once there are more than two :

```python
named = re.search(r"(?P<level>ERROR|WARN|INFO) (?P<message>.*)", line)
named.group("level")    # ERROR
named.group("message")  # disk full
```

> `demo07 Â· regex_groups`

---

# Substitution and Splitting

- `sub` replaces every match in the string :

```python
text = "Call 020-1234567 or 010-7654321 today"

re.sub(r"\d", "x", text)  # Call xxx-xxxxxxx or xxx-xxxxxxx today
re.sub(r"\d{3}-\d{7}", "[redacted]", text)
```

- A backreference in the replacement reuses a captured group :

```python
re.sub(r"(\d{3})-(\d{7})", r"\2-\1", text)
# Call 1234567-020 or 7654321-010 today
```

- `re.split` accepts a pattern where `str.split` accepts only a literal :

```python
re.split(r"\s+or\s+", text)
# ['Call 020-1234567', '010-7654321 today']
```

> `demo08 Â· regex_sub`

---

# Command-Line Arguments with sys.argv

- `sys.argv` holds the arguments passed to a Python script as a list of strings :
  - `sys.argv[0]` is the name or path of the script itself
  - `sys.argv[1:]` contains any arguments passed after the script name

```python
import sys

print(f"Script name : {sys.argv[0]}")
print(f"Arguments   : {sys.argv[1:]}")
```

- Every argument arrives as a string :
  - Convert numbers explicitly with `int()` or `float()`
  - Inspect `len(sys.argv)` to check how many arguments were supplied
- For option flags, defaults and help messages, `argparse` is the next step :
  - `argparse` handles `--flag` options, generates `--help` and parses types
  - `sys.argv` is the underlying list `argparse` reads from

> `demo09 Â· sys_argv`

---

# Testing with pytest

- In `pytest`, a test is a function whose name starts with `test_` :
  - No test case class to subclass and no special assertion methods
  - Plain `assert` statements check the expected conditions
- `pytest` is installed in the project with `uv add --dev pytest` :

```python
def add(a: int, b: int) -> int:
    return a + b


def test_positive_numbers() -> None:
    assert add(2, 3) == 5


def test_with_zero() -> None:
    assert add(0, 7) == 7
```

- Run all discovered tests with `uv run pytest` (verbose with `-v`) :

```bash
uv run pytest -v
```

> `demo10 Â· pytest_basic`

---

# Reading a Test Failure

- When an `assert` fails, `pytest` explains exactly what went wrong :
  - It reconstructs intermediate expressions and shows where the values diverged
- Running `uv run pytest 11_pytest_failure.py` on a deliberately failing test :

```text
_______________________________ test_wrong_sum ________________________________

    def test_wrong_sum() -> None:
>       assert add(2, 3) == 6
E       assert 5 == 6
E        +  where 5 = add(2, 3)

11_pytest_failure.py:15: AssertionError
=========================== short test summary info ===========================
FAILED 11_pytest_failure.py::test_wrong_sum - assert 5 == 6
```

- The report shows the source line, the evaluated values, and the summary line :
  - No custom assertion methods like `assertEqual` are needed for clear output

> `demo11 Â· pytest_failure`

---

# Exceptions and Parametrized Tests

- `pytest.raises` checks that a block of code raises an expected exception :
  - Used as a context manager; the test passes only if the exception occurs

```python
with pytest.raises(ValueError):
    divide(10, 0)
```

- `@pytest.mark.parametrize` runs one test function across multiple inputs :
  - Each tuple in the list runs as an independent test case

```python
@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (5, 2, 2.5),
    ],
)
def test_divide(a: int, b: int, expected: float) -> None:
    assert divide(a, b) == expected
```

> `demo12 Â· pytest_features`

---

# Summary : Python Libraries

- `datetime` covers dates, times and durations :
  - `date` , `time` , `datetime` and `timedelta`
  - `strftime` formats and `strptime` parses using a pattern
  - `isoformat()` formats; `fromisoformat()` parses, without a format pattern
- `json` converts between Python objects and JSON text :
  - `dumps` and `loads` for strings, `dump` and `load` for files
  - A tuple returns as a list, and keys return as strings
- `re` searches and rewrites text with patterns :
  - `match` at the start, `search` anywhere, `findall` for every hit
  - Parentheses capture, and `sub` replaces using what was captured
- `sys.argv` exposes command-line arguments as a list of strings :
  - `argparse` is the next step for options, flags and automatic help
- `pytest` runs checks over the code automatically :
  - Test functions named `test_` and plain `assert` statements
  - `pytest.raises` for exceptions and `@pytest.mark.parametrize` for tables

> `exercise13 Â· Python Libraries`

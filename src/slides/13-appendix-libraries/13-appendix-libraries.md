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
  - Exercise 13 installs it with `uv add --dev pytest`
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

photo_day = date(2026, 8, 15)
midday = time(12, 30, 0)
taken_at = datetime(2026, 8, 15, 12, 30, 0)

print(taken_at.year, taken_at.month, taken_at.day)
print(taken_at.weekday())  # Monday is 0, so this prints 5
```

- The current moment comes from the class itself :
  - `date.today()` and `datetime.now()`

> `demo01 · datetime_basics`

---

# Formatting and Parsing Dates

- `strftime` formats a datetime as text, `strptime` reads text back :
  - The `f` is for format, the `p` is for parse

```python
taken_at.strftime("%d-%m-%Y %H:%M")  # 15-08-2026 12:30
taken_at.strftime("%A %d %B %Y")     # Saturday 15 August 2026

datetime.strptime("24-12-2026 18:00", "%d-%m-%Y %H:%M")
```

- Common directives :
  - `%Y` four digit year, `%m` month, `%d` day
  - `%H` hour, `%M` minute, `%S` second
  - `%A` weekday name, `%B` month name
- ISO 8601 needs no format string in either direction :

```python
taken_at.isoformat()  # 2026-08-15T12:30:00
datetime.fromisoformat("2026-12-24T18:00:00")
```

> `demo02 · datetime_format`

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

> `demo03 · datetime_arithmetic`

---

# The json Module

- JSON stores structured text exchanged by programs :
  - `dumps` converts a Python value to JSON text; `loads` reads it back

```python
import json

playlist = {"name": "Night drive", "tracks": ["Imagine", "Yesterday"], "cover": None}
text = json.dumps(playlist, indent=2, sort_keys=True)
restored = json.loads(text)
```

```text
{
  "cover": null,
  "name": "Night drive",
  "tracks": [
    "Imagine",
    "Yesterday"
  ]
}
```

- `indent` makes the output easier to read; `sort_keys` orders dictionary keys

> `demo04 · json_strings`

---

# Reading and Writing JSON Files

- `dump` and `load` work with file objects :
  - The names are the string versions without the trailing `s`

```python
import json
from pathlib import Path

playlist = {"name": "Night drive", "tracks": ["Imagine", "Yesterday"], "cover": None}
path = Path("playlist.json")

with path.open("w", encoding="utf-8") as file:
    json.dump(playlist, file, indent=2)

with path.open(encoding="utf-8") as file:
    restored = json.load(file)
print(restored["tracks"])
```

- Explicit UTF-8 keeps playlist files consistent across machines

> `demo05 · json_files`

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
r"^IMG_\d{4}\.jpg$"   # a photo filename like IMG_0421.jpg
```

---

# Matching and Searching

- Regex functions differ in where and how much they match :
  - `match` starts at position zero; `search` scans the whole string
  - `findall` returns all matches; `fullmatch` requires the whole string

```python
import re

text = "Playing Imagine (183s), Yesterday (125s)"
print(re.match(r"Playing", text) is not None)  # True
print(re.match(r"Yesterday", text) is not None)  # False
print(re.search(r"Yesterday", text) is not None)  # True
print(re.findall(r"\d+", text))  # ['183', '125']
print(re.fullmatch(r"IMG_\d{4}\.jpg", "IMG_0421.jpg") is not None)  # True
print(re.fullmatch(r"IMG_\d{4}\.jpg", "notes.txt") is not None)  # False
```

- `match`, `search` and `fullmatch` return a match object or `None`
- Flags include `re.IGNORECASE`, `re.MULTILINE` and `re.DOTALL`

> `demo06 · regex_search`

---

# Groups and Capturing

- Parentheses capture useful parts of a player log entry :

```python
import re

line = "12:30 PLAY Imagine"
match = re.search(r"(\d{2}):(\d{2}) (\w+) (.*)", line)
if match is not None:
    print(match.group(0))  # 12:30 PLAY Imagine
    print(match.groups())  # ('12', '30', 'PLAY', 'Imagine')
```

- Named groups identify captured values without counting positions :

```python
named = re.search(r"(?P<action>PLAY|SKIP) (?P<title>.*)", line)
if named is not None:
    print(named.group("action"))  # PLAY
    print(named.group("title"))  # Imagine
```

> `demo07 · regex_groups`

---

# Substitution and Splitting

- `sub` replaces matching text :
  - A backreference such as `\1` reuses a captured group
- `re.split` uses a pattern to separate items :

```python
import re

text = "IMG_0421.JPG; IMG_0422.JPG"
print(re.sub(r"IMG_\d{4}\.JPG", "[photo]", text))
print(re.sub(r"IMG_(\d{4})\.JPG", r"photo_\1.jpg", text))
print(re.split(r";\s*", text))
```

```text
[photo]; [photo]
photo_0421.jpg; photo_0422.jpg
['IMG_0421.JPG', 'IMG_0422.JPG']
```

- The identifier stays available when a photo filename is reformatted

> `demo08 · regex_sub`

---

# Command-Line Arguments with sys.argv

- `sys.argv` contains the arguments passed to a script :
  - Position `0` is the script path; later positions contain its arguments

```python
import sys

print(f"Script: {sys.argv[0]}")
playlist_file = sys.argv[1] if len(sys.argv) > 1 else "night-drive.json"
print(f"Playlist file: {playlist_file}")
```

```bash
uv run python 09_sys_argv.py warm-up.json
```

- Arguments arrive as strings; convert numeric values explicitly
- `argparse` adds option flags, defaults and generated help

> `demo09 · sys_argv`

---

# Testing with pytest

- Tests can check the duration formatter already used by the player :
  - Each test function starts with `test_`
  - A plain `assert` states the expected result

```python
def format_duration(seconds: int) -> str:
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder:02d}"


def test_minutes_and_seconds() -> None:
    assert format_duration(222) == "3:42"


def test_exact_minute() -> None:
    assert format_duration(60) == "1:00"
```

```bash
uv add --dev pytest
uv run pytest 10_pytest_basic.py
```

> `demo10 · pytest_basic`

---

# Reading a Test Failure

- A missing zero-padding rule is a plausible display bug :

```python
def format_duration(seconds: int) -> str:
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder}"


def test_exact_minute() -> None:
    assert format_duration(60) == "1:00"
```

- Running `uv run pytest 11_pytest_failure.py` exposes the difference :

```text
E       AssertionError: assert '1:0' == '1:00'
```

- Restore `:02d` in the f-string to satisfy the test

> `demo11 · pytest_failure`

---

# Exceptions and Parametrized Tests

- `pytest.raises` checks a failure that the parser must report
- `parametrize` repeats one test with several inputs :

```python
def test_invalid_duration() -> None:
    with pytest.raises(ValueError):
        parse_duration("3:99")


@pytest.mark.parametrize(
    ("seconds", "expected"),
    [(0, "0:00"), (59, "0:59"), (60, "1:00"), (3600, "60:00")],
)
def test_duration_display(seconds: int, expected: str) -> None:
    assert format_duration(seconds) == expected
```

- The demo includes the familiar formatter and duration parser
- Fixtures, mocking and testing in depth belong to Advanced Python

> `demo12 · pytest_features`

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

> `exercise13 · Python Libraries`

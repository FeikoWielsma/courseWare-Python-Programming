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
  - `unittest` , the testing framework built into the language
- Others worth knowing about :
  - `pathlib` for filesystem paths, `csv` for tabular files
  - `collections` for counters, deques and default dictionaries
  - `itertools` for combinations, grouping and infinite sequences
  - `os` and `sys` for the environment the program runs in
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

> `demo01 · datetime_basics`

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

> `demo04 · json_strings`

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
r"^\w+@\w+\.\w{2,4}$"  # a very rough email address
```

---

# Matching and Searching

- Three functions cover most use, and they differ in where they look :

```python
import re

text = "Order 1234 shipped, order 5678 pending"

re.match(r"Order", text)     # only tries position zero
re.match(r"shipped", text)   # None, even though the word is present
re.search(r"shipped", text)  # scans the whole string, finds it
re.findall(r"\d+", text)     # ['1234', '5678']
```

- `match` and `search` return a match object, or `None` :
  - So the result is tested before it is used
- Flags change how the pattern is applied :
  - `re.IGNORECASE` , `re.MULTILINE` , `re.DOTALL`

> `demo06 · regex_search`

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

> `demo07 · regex_groups`

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

> `demo08 · regex_sub`

---

# Unit Testing with unittest

- A unit test checks one unit of behaviour in isolation :
  - Tests are run automatically, so a regression is noticed immediately
- A test case is a class deriving from `unittest.TestCase` :
  - Every method whose name starts with `test` is collected and run

```python
import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test_two_positives(self):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
```

> `demo09 · unittest_basic`

---

# Assertions

- The assertion methods say what is expected, and report clearly when it is not :

| Method | Checks |
|---|---|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` / `assertFalse(x)` | truth of `x` |
| `assertIs(a, b)` / `assertIsNone(x)` | identity |
| `assertIn(a, b)` | `a in b` |
| `assertRaises(Error)` | the block raises that exception |
| `assertAlmostEqual(a, b)` | equal to seven decimal places |

- `assertAlmostEqual` exists because floating point equality is unreliable
- `assertRaises` is used as a context manager :

```python
with self.assertRaises(AttributeError):
    self.basket.remove("apple")
```

---

# Fixtures and Running Tests

- `setUp` runs before every test method, `tearDown` after every one :
  - So no test can be affected by what another test did

```python
class TestBasket(unittest.TestCase):
    def setUp(self):
        self.basket = Basket()

    def test_starts_empty(self):
        self.assertEqual(self.basket.total(), 0)
```

- Tests are run from the command line :

```bash
python -m unittest test_basket.py
python -m unittest discover        # find every test in the tree
python -m unittest -v              # name each test as it runs
```

- Output reports a dot per passing test :

```text
...
Ran 3 tests in 0.000s

OK
```

> `demo10 · unittest_fixtures`

---

# Summary : Python Libraries

- `datetime` covers dates, times and durations :
  - `date` , `time` , `datetime` and `timedelta`
  - `strftime` formats, `strptime` parses, `isoformat` does both without a pattern
- `json` converts between Python objects and JSON text :
  - `dumps` and `loads` for strings, `dump` and `load` for files
  - A tuple returns as a list, and keys return as strings
- `re` searches and rewrites text with patterns :
  - `match` at the start, `search` anywhere, `findall` for every hit
  - Parentheses capture, and `sub` replaces using what was captured
- `unittest` runs checks over the code automatically :
  - A `TestCase` class, methods named `test...` , and the `assert...` family
  - `setUp` gives every test a clean starting point

> `exercise13 · Python Libraries`

<!-- appendix -->

# Exercise 13 : Python Libraries

An optional exercise covering the four standard library modules from the appendix. Each step stands on its own, so take them in whatever order interests you. Work in your `course-work` project.

---

### Step 1 : datetime

Create a module `dates13.py`. Write a function `days_until(target)` that takes a `date` and returns the number of days between today and that date. Use it to print how many days remain until the next New Year's Day.

Then print today's date in three formats :

- `15-08-2026`
- `Saturday 15 August 2026`
- the ISO form, `2026-08-15`

Finally, read the string `"24-12-2026 18:00"` back into a `datetime` with `strptime` and print the weekday it falls on.

### Step 2 : json

Create a module `books13.py` holding a list of at least three dictionaries, each with a `title`, a `pages` count and a list of `tags`.

Write the list to `books.json` with `json.dump`, using `indent=2` so the file is readable. Open the file in your editor and look at it. Then read it back with `json.load` and print the title of every book with more than 500 pages.

Now add a `published` key whose value is a `date` object and try to write the file again. Read the error carefully. Fix it by converting the date to a string with `isoformat()` before writing.

---

### Step 3 : Regular expressions

Create a module `log13.py` with the following lines as a list of strings :

```text
2026-08-15 12:30 ERROR disk full
2026-08-15 12:31 INFO backup started
2026-08-15 12:45 WARN disk at 91 percent
2026-08-16 09:02 ERROR connection refused
```

Write a regular expression with named groups for the date, the time, the level and the message. For each line, print only the entries whose level is `ERROR`, formatted as `date time : message`.

Then use `re.findall` to collect every number that appears in any message, and `re.sub` to replace every date with the word `[date]`.

### Step 4 : unittest

Create a module `calculator13.py` with four functions, `add`, `subtract`, `multiply` and `divide`. Make `divide` raise a `ValueError` when asked to divide by zero.

Create a second module `test_calculator13.py` with a `TestCase` class that tests all four. Include :

- a test per function for the ordinary case
- a test that `divide` raises `ValueError` on a zero divisor, using `assertRaises`
- a `setUp` method that prepares any values the tests share

Run the tests with `python -m unittest test_calculator13.py -v` and read the output. Then break one function on purpose and run the tests again, so that you see what a failure report looks like.

---

**If time permits** : the `appendices/` folder holds reference PDFs on several further libraries, and `demos/13-appendix-libraries/` holds a runnable example for every slide in the appendix module.

# Hints pass : hints that point back, nothing new on the required path

Date: 2026-10-17. Branches: `t3/e52c920d` (Exercises 2 to 8), then `t3/da48ba47` (the rest, and tests out of the main course).

Scope : `src/exercises/*.md`. A step "where the student writes code" is one that asks
for code the student composes (a skeleton, a signature, a description). Steps that give
the code to type verbatim, run-and-observe steps, closers (*If time permits*) and the
test steps are left as they are. A first hint names the slide by its exact title in
italics or the demo by its pill name in backticks.

## Exercise 1

No change. Every step gives the commands or the code; nothing is asked. Step 6 uses
`Path(...).read_text(...)` before module 09, already given as code with a sentence
saying what it does.

## Exercise 2

- Step 2 : new first hint (*String Operations*, *Logical, Membership, Identity
  Operators*). The `!s` conversion was taught in the second hint; the f-Strings slide
  shows only `!r`. Moved into the step : the skeleton now carries `!s` and one
  sentence says what it does. The hint that taught it is gone.
- Step 3 : new first hint (*String Operations*, *Built-in String Methods*).

## Exercise 3

- Intro : removed "It takes about an hour." (no timings).
- Step 2 : *Set Operations* moved from the step text into the first hint.
  `string.ascii_lowercase` was taught in a hint and is on no slide or demo; now given
  in the step with one sentence. Step 1's `random.choice` / `random.seed` are given as
  code with an explanation already.
- Step 3 : new first hint (`demo01 · lists`, *List Functions and Methods*, *Tuples*).
- Step 4 : new first hint (*Dictionaries*, *Accessing Values in Dictionary*); the
  `int(True)` hint now names *Type Conversions*, which says a bool behaves as 0 and 1.

## Exercise 4

- Step 2 : new first hint (*if Statement*, *Logical, Membership, Identity Operators*).
- Step 3 : the step's pointer to *Iterating with enumerate* and *elif Statement*
  moved into a new first hint.
- Step 4 : the step's pointer to *match Statement* moved into a new first hint, which
  also names *break and continue Statements*, *Built-in String Methods* (`join`) and
  *Set Operations* (`sorted`).
- Step 5 : the hint's slide reference (*Loop with else Combination*) moved to the front.
- Nothing missing. Step 1's `os.environ.get` is given as code with an explanation.
  Note : *match Statement* says "no `break` is needed"; in Step 4 `break` inside a
  `case` leaves the `while`. The existing hint says `break` leaves the loop; a line on
  the slide would settle it.

## Exercise 5

- Step 2 : new hint (*Function Syntax*, *return Statement*); it had none.
- Step 3 : new first hint (*Built-in String Methods* for `isalpha`, *return Statement*).
- Step 4 : new first hint (*List Operations* for `['go']*3`, *List Functions and
  Methods* for `append` / `remove`, *Iterating with enumerate*). The pytest part of
  the step is unchanged.
- Step 5 : new first hint (Exercise 4's row, *match Statement*).
- Step 6 : new first hint (*return Statement* : `return` inside the loop ends it).
- Nothing missing.

## Exercise 6

- Step 2 : the slide reference moved out of the end of the hint into a new first hint
  (*from...import Statement*, *Running Packages with python -m*).
- Step 1 gives its code; Step 4 is a test step, left as it is.
- Nothing missing.

## Exercise 7

- Step 1 : new first hint (*Generator Expressions*, *Lambda Functions*).
- Step 3 : the step's *Filtered List Comprehension* pointer moved into a new first
  hint, which also names *Generator Expressions* for `all`.
- Step 4 : the step's three slide pointers moved into a new first hint, with
  *Generator Expressions* for `sum`.
- Step 5 : new first hint (*match Statement*, *List Functions and Methods*).
- Missing : `zip(..., strict=True)` is not on *Zip Function* (the step already says
  what it does, so it stays as given code). Calling a function looked up in a
  dictionary, `symbols[mark](letter)`, is on no slide or demo; the second hint says
  it. The double `for` in one comprehension (`for word in words for letter in word`)
  is not on *Nested List Comprehensions* but the skeleton gives it.

## Exercise 8

- Step 2 : the step's *Raising Exceptions* pointer moved into a new first hint, with
  *Typed Exception Handling* for the wrapper.
- Step 3 : new first hint (*Example Argument of an Exception*, *Exception
  Arguments*); the old hint's "See *Typed Exception Handling*" dropped, since the
  step needs `as error`, which the new first hint names.
- Step 4 : new first hint (*Typed Exception Handling*, *except Clause Multiple
  Exceptions*).
- Step 5 (the student's own tests) left as it is.
- Missing : `EOFError` is on no slide or demo, and `KeyboardInterrupt` appears only
  as output on *Infinite while Loop*. The skeleton gives both and the step says when
  each happens, so nothing is required of the student.

## Exercise 9

- Step 1 : the handed-out `tests/test_words.py` replaced by two `clean_words` calls with
  their results. `str.isascii()` was taught in a hint and is on no slide; now said in the
  step. New first hint (*Built-in String Methods*, *Set Operations*).
- Step 2 : `splitlines()` is on no slide; one sentence added beside the given code.
- Step 3 : `os.chdir("tests")` became `os.chdir("wordle")`, since the project has no
  `tests/` folder any more. Output re-run.
- Step 4 : new first hint (*Paths with pathlib*). Step 5 : new first hint (*The csv
  Module*, *File Open Modes*).
- Step 6 : removed "within the hour" (a timing).

## Exercise 10

- Steps 3 to 5 : the student-written statistics tests replaced by a Python session on
  `connect(":memory:")` (on *Last inserted row id*) with four recorded games; results
  re-run against `solutions/10-database-access/`.
- Step 3 : the conditional expression `x if c else y` is on no slide and was in a hint;
  now given as code in the step with one sentence. New first hint (*Retrieving Data*,
  *Dictionaries*).
- Step 4 : new first hint (*Dictionary Construction with zip*).
- Step 5 : `for (game_won,) in cursor` (one-item tuple unpacking in a `for`) was in a
  hint; now given as code in the step. New first hint (*break and continue Statements*).
- Steps 2 and 6 : new first hints (*Parameterized Queries*; *String Operators*,
  *Format Specifications*, *Generator Expressions*).

## Exercise 11

- Handed-out `tests/test_game.py` and every pytest run removed; Step 4's validation test
  became a session with the two `ValueError`s, re-run.
- New first hints : Step 2 (*Class Members*), Step 3 (*A Computed Attribute*), Step 4
  (*When a Plain Attribute Is Not Enough*, `demo07 · validatingsetter`), Step 5
  (*`__str__` and `__repr__`*, *Generator Expressions*). Removed a muddled sentence that
  pointed at *Class Attributes and Instance Attributes* for `__str__`.

## Exercise 12

- "the way you added `pytest`" became `ruff` in Exercise 1; the two `uv run pytest`
  checks became "play a game".
- New first hints : Step 2 (*Closed Sets with Literal*), Step 3 (*Optional Values*).

## Exercise 13

- Step 3 now introduces `uv add --dev pytest` and the `[tool.pytest.ini_options]
  pythonpath = ['.']` section that Exercise 6 used to give, and its output block is the
  real tail of `uv run pytest` on a project whose only test file is `test_ex13.py`.
- Step 5 no longer relies on Exercise 8's tests; Step 6 no longer says the student wrote
  tests in Exercise 8.
- New first hints : Steps 2 to 6.

## Tests out of the main course

Exercises 5 to 11 use the interactive interpreter (*Python in Interactive Mode*, module
01) where they used tests : the step gives two or three calls with their results.
Exercise 5 explains `from wordle import score_guess` in one sentence and says the
interpreter must be restarted after a change. Exercise 8's student-written tests step
is gone. Exercises 2 to 4 and 9 to 13 no longer promise "only the tests to pass".

## Gaps still open (recommended fixes)

- `x if c else y` (Ex 10 Step 3, Ex 13 Step 2) : given in Ex 10 now; better on a slide,
  for example a line on *if Statement* or *Logical, Membership, Identity Operators*.
- `str.isascii()` (Ex 9) and `str.splitlines()` (Ex 9) : add rows to *Built-in String
  Methods*.
- `for (x,) in rows` and `for i, (a, b) in enumerate(zip(...))` (Ex 10 Step 5, Ex 13
  Step 3) : add a nested-unpacking line to *Usage of Tuples* or *Iterating with
  enumerate*. Ex 13 can also be solved with `range` and indexing.
- `chart or 'none'` (Ex 10 Step 6 hint) and `bool(history and ...)` (Ex 11 Step 3 hint) :
  `and`/`or` returning an operand is on no slide. Both are in hints for an optional
  refinement; either add a line to *Logical, Membership, Identity Operators* or reword
  the hints.
- `Path.open(...)` (Ex 9 Step 5 skeleton), `Path(__file__)`, `.resolve().parents[1]`,
  `os.chdir`, `contextlib.closing`, `connection.execute` without a cursor : all given as
  code with a sentence; a line on *Paths with pathlib* for `__file__` and `.open` would
  make them taught.

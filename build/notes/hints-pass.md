# Hints pass : hints that point back, nothing new on the required path

Date: 2026-10-17. Branch: `t3/e52c920d`.

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

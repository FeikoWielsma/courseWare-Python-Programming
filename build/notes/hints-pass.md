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

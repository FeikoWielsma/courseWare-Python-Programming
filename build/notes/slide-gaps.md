> Historical record (2026-10-17). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# Slide gaps : what the slides now teach for the exercises

Date: 2026-10-17. Branch `t3/aca89c91`. Closes the "Missing" lines of
`build/notes/hints-pass.md` for Exercises 7 to 10 and 13, where the gap was on no
slide or demo.

| Used in | What | Slide (module) | Demo |
|---|---|---|---|
| Ex 10, 13 | `x if c else y` | *Logical, Membership, Identity Operators* (02) | `demo09 · booleanoperators` |
| Ex 10, 11 | `and` / `or` return an operand | same slide (02), `and` added beside `or` | `demo09 · booleanoperators` |
| Ex 9 | `str.isascii()`, `str.splitlines()` | *Built-in String Methods* (02), two table rows | `demo15 · stringfunctions` |
| Ex 10, 13 | nested unpacking, `for (x,) in rows` | *Usage of Tuples* (03) | `demo08 · destructurewithtuples` |
| Ex 7 | `zip(..., strict=True)` | *Zip Function* (07) | `demo05 · zip_function` |
| Ex 7 | two `for` clauses in one comprehension | *Nested List Comprehensions* (07) | `demo03 · nested_comprehensions` |
| Ex 8 | `EOFError`, `KeyboardInterrupt` | *Python Standard Exceptions* (08), two table rows | none on this slide |
| Ex 9, 10 | `Path(__file__).parent`, `resolve()`, `Path.open` | *Paths with pathlib* (09) | none on this slide |
| Ex 10 | `contextlib.closing` | *Using with* (10) | `demo02 · usingwith` |

## Still open

- `symbols[mark](letter)`, calling a function looked up in a dictionary (Exercise 7):
  on no slide or demo. Not in this pass's list; the step still relies on its hint.
- Exercise 4's `break` inside a `match` case: the *match Statement* slide says no
  `break` is needed. Module 04 is outside this pass.

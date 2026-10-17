# WP2c notes : exercise texts 9 to 13

Branch `t3/wp2c-wordle-exercises-9-13`. All five texts written, verified against the
solutions (run in copies under `C:/tmp/wp2c/`), built (PDF and site) and checked on the site.

## Done

| Ex | Steps (tier) |
|---|---|
| 9 | 1 clean_words ★★, 2 write the clean list ★, 3 path from `__file__` ★, 4 answers + allowed lists ★★, 5 history.txt (csv append) ★★, 6 `stats` command ★★, if time : `last` |
| 10 | 1 connect ★, 2 record_game ★★, 3 summary totals ★★, 4 distribution ★★★, 5 streak ★★★, 6 use it in the game ★★, if time : import history, fixed db path |
| 11 | 1 Game with plain attributes ★, 2 guess() ★★, 3 read-only properties ★★, 4 validating max_guesses ★★★, 5 `__str__` + shrink play ★★, if time : board command, Stats class |
| 12 | 1 mypy ★, 2 `type Mark = Literal[...]` ★★, 3 `str \| None` from best_guess ★★★, if time : strict |
| 13 | 1 datetime daily ★, 2 sys.argv flags ★★, 3 hard mode `follows_hints` ★★★, 4 JSON save/resume ★★, 5 `re` ★★, 6 own tests (assert, raises) ★★, 7 parametrize ★, if time : argparse |

## Decisions

- Ex 10 tests are written inside the text (`tests/test_stats.py`, in-memory SQLite); no handout exists.
- Ex 11 follows plan section 6 : plain attribute, computed properties, bug demo (`max_guesses = 0` over before start, `-3` never ends), then validating setter. `play` keeps the redundant `check_guess` line, as the solution does.
- Ex 13 orders steps datetime, argv, hard mode, json, re, tests so the signature of `play` matches the solution (`hard`, then `history`).
- Ex 13 omits the solution's "Game saved" message on `quit` (see problems below).
- The `type Mark = ...` statement is used (as in the solution and slide 12), not `Mark = Literal[...]`.

## Problems in solutions, starters or handouts (for the coordinator)

1. **`allowed.txt` is not handed out.** Starter 09 has no `wordle/data/` and the handout dir has only `raw-words.txt` and `tests/`. Ex 9 Step 4 needs `allowed.txt` (8 639 words, the file in `solutions/09-python-io/wordle/data/`); the text says it is handed out. Add it (and `SOURCES.md`) to `exercises/handouts/09-python-io/`.
2. **Stale `words.txt` in solutions 09 to 13** : a 715-word file in the project root next to the 935-word `wordle/data/words.txt`. Ex 9 tells students to delete the old one; the solutions should not carry it.
3. **`tests/test_exceptions.py` missing from solutions 09 to 13** (present in solution 08 and starter 09).
4. **Ex 10 : the `bool` `play` returns is still not used by any caller** (`__main__` ignores it; `play` records the game itself). The text says the result decides the last argument of `record_game`.
5. **Ex 10 : `connect(path="wordle.db")` is relative to the working directory**, against the lesson of Ex 9. The text says so and offers a fixed path in *If time permits*.
6. **Ex 11 : `play` prints `The word was X.` also after a win**, and calls `check_guess` twice (before `game.guess`). Harmless; the text matches the solution.
7. **Ex 13 : `quit` prints "Game saved. Run Wordle again to resume." but the save is cleared at once** (the code after `break` calls `clear_saved_game()`), and the game is recorded as lost. Only Ctrl+C or Ctrl+D leaves a save. Remove the message or skip the clear on quit.
8. **Ex 13 : `follows_hints(guess, history)`** differs from the Exercise 5 *If time* signature `follows_hints(guess, previous, marks)`, and also rejects a yellow letter reused in the same position.
9. **Ex 13 : `tests/test_ex13.py`** holds three tests; the text builds a superset (adds a `pytest.raises(..., match=...)` test).

## Build and site

- Slide references that did not resolve : `*`__str__` and `__repr__`*` (a title that contains code spans is not matched by the site). Ex 11 Step 5 therefore names that slide in plain text.
- `build/site.config.ts` "Run the game" row says `uv run python -m wordle` for every exercise; fine for 9 to 13.
- The site build needs `PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/Presentation-Template` from a worktree.

## Slide titles used in italics

- 09 : Reading Text Files, Paths with pathlib, The csv Module, File Open Modes, Using with
- 10 : DB API Concepts, Inserting Data, Parameterized Queries, Committing Data, Retrieving Data, Transactions
- 11 : Creating Classes, Class Members, Attributes Are Public, A Computed Attribute, When a Plain Attribute Is Not Enough, The Rule of Thumb, Class Attributes and Instance Attributes
- 12 : Typing Collections, Checking with mypy, Closed Sets with Literal, Optional Values
- 13 : The datetime Module, Date Arithmetic with timedelta, Command-Line Arguments with sys.argv, The json Module, Reading and Writing JSON Files, JSON and Python Types, Regular Expressions with re, Matching and Searching, Testing with pytest, Exceptions and Parametrized Tests, Reading a Test Failure

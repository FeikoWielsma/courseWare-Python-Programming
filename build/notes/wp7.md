> Historical record (2026-10-17). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# WP7 notes : solutions and exercise texts 9 to 13 made to agree

Resolves the problems listed in `wp2c.md`.

| # | Problem | Resolution |
|---|---|---|
| 1 | `allowed.txt` not handed out | `allowed.txt` and `SOURCES.md` added to `exercises/handouts/09-python-io/`; Exercise 9 names four handouts and tells the student to copy both files into `wordle/data/` |
| 2 | Stale root `words.txt` in solutions 09 to 13 | Removed; starters 10 to 13 lose it too (starter 09 keeps it, it is the finished Exercise 8) |
| 3 | `tests/test_exceptions.py` missing | Copied from solution 08 into solutions 09 to 13 |
| 4 | `play`'s `bool` unused | From Exercise 10 `play` returns `tuple[int, bool]` (guesses, won) and does not record; `__main__` unpacks it and calls `record_game(connection, secret, guesses, won)`. Exercises 10, 11 and 13 quote the new code. Exercise 9 is unchanged (`play` still records the CSV row itself) |
| 5 | `quit` said "Game saved" but cleared the save | `quit` is give up in every exercise: no save, no message, recorded as a loss. Matches the Exercise 13 text |
| 6 | "The word was X." after a win; `check_guess` twice | Message now only after a loss (Exercises 11 to 13). The `check_guess` call in `play` is kept on purpose : `Game.guess` validates for itself, and `follows_hints` in Exercise 13 indexes into the guess, so `play` must validate first (the Exercise 13 text already says so) |
| 7 | `follows_hints` signatures differ | One signature, `follows_hints(guess, history)` with `history` a list of `(guess, marks)`, and one rule : green stays in place, yellow appears somewhere. Exercise 5's optional step and Exercise 13 say so. The old extra clause that rejected a yellow letter reused in the same place is gone, and the `crabs` assertion with it |

## Transcripts

`11-python-classes`, `12-type-hinting` and `13-python-libraries` lose the line `The word was CRANE.` after the win (item 6). Transcripts 01 to 10 are unchanged. The `--record` mode writes CRLF on Windows : the three files were converted back to LF.

## Left for the coordinator

- `wordle/data/answers.txt` in solutions 09 to 13 is byte for byte the same as `words.txt` and no text mentions it.
- `connect(path="wordle.db")` is still relative to the working directory (Exercise 10 offers a fixed path in *If time permits*).
- `tests/test_ex13.py` holds three tests and the text builds a superset (adds a `pytest.raises` test); unchanged.

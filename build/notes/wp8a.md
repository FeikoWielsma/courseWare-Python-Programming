> Historical record (2026-10-17). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# WP8a : review findings fixed in the solutions and exercise texts

Date: 2026-10-17. Model: Claude Sonnet 5.5. Branch `t3/242639ef` (from `prg400-wordle`).

| ID | Resolution |
|---|---|
| F02 | `save.json` now holds `max_guesses` and `hard`; `save_game` / `load_saved_game` carry them; `main` takes them from the save, and from the options only for a new game. `Game.is_over` tests `guesses_left <= 0` (solutions 11 to 13, Ex 11 text and its quoted `-3 -3 True`). Handout `test_game.py` gains `test_game_is_over_when_the_limit_drops_below_the_history` (4 tests; Ex 11 counts updated). Checked by hand: `--easy`, one guess, interrupt, restart without flags gives `Guess 2/10`; `--hard` also survives. |
| F24 | `play` prints the restored `Game` before the first prompt; Ex 13 Step 4 snippet and expected output show the board. |
| F03 | `tests/test_stats.py` (the four tests of Ex 10, verbatim) in solutions 10 to 13 and so in starters 11 to 13. |
| F04 | `test_ex13.py` has the `clink` assertion and the capital-letter test, in the order of the text. |
| F05 | Ex 10 gives the three SQL strings (`COUNT/SUM/COALESCE`, `WHERE/GROUP BY/ORDER BY`, `ORDER BY id DESC`) with a plain-language reading of each. Step 3 skeleton contains the query, Step 4 drops from ★★★ to ★★, Step 5 stays ★★★ (the loop). No slide title is cited for the new SQL slide; add a pointer when it has landed. |
| F06 | `connect` and `record_game` no longer commit. The caller owns the transaction: `with closing(connect()) as connection, connection:` in `main`, `with closing(connect()) as connection:` in `print_stats`. Verified: no `ResourceWarning` under `-W always`, games persist across processes. Side effect: the Ex 10 Step 2 REPL experiment no longer leaves a committed row in `wordle.db`, which had made the Step 6 "Games played: 4" example off by one. REPL sessions close their connection. |
| F15 | The handler in solutions 09 to 13 names `wordle/data/words.txt` and `wordle/data/allowed.txt`; Ex 9 Step 3 tells the student to change it. Ex 8 keeps its own text. |
| F16 | `wordle/data/answers.txt` removed from solutions 09 to 13 (and so from starters 10 to 13). |
| F23 | Guard before `letter_counts` in `best_guess` of solutions 12 and 13. |
| F14 | Ex 2 Steps 2 and 3 say the guess must be five letters until Ex 4. |
| F22 | Ex 9 Step 1 has a set/loop skeleton, Step 5 a `with` skeleton (both stay ★★). |

Transcripts: none changed; all 13 scripted games still match.

## Day 4 time

Reviewer estimate against stated: Ex 9 75 vs 45, Ex 10 95 vs 60, Ex 11 110 vs 90.

- Ex 9: Step 6 (CSV stats, replaced by the database in Ex 10) is now ★ code to read and type, saving about 8 minutes; the handler edit adds 2. Expected about 65 minutes. Moving Steps 5 or 6 to *If time permits* would break the Ex 10 starter chain (Ex 10 Step 6 edits `print_stats` and `record_history`).
- Ex 10: SQL given saves about 15 minutes; the `closing` explanation adds 3. Expected about 80 minutes (range 65 to 95).
- Ex 11: unchanged apart from a fourth handed-out test; expected about 110 minutes. No step can move to optional without breaking the Ex 12/13 chain.

The stated minutes in the exercise intros were left at 45 and 60: the plan budget is a coordinator decision.

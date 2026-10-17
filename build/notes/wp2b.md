# WP2b progress

- Exercise 5 converted to containers and tier badges; fixed WORDLE_SECRET instructions and the early render import required by pytest collection.
- Verified Exercise 5 starter duplicate bug, corrected solution game and five selected scoring tests; all nine solution tests pass.
- Exercises 6–8 and build verification completed in the resumed session.
- Decision: retain the Exercise 5 step order with a temporary render stub, keeping the playable old display until Step 5.
- Slide references so far: Annotating a Function; Default Arguments.

- Exercise 6 rewritten and verified: package creation ★, module split ★★, module execution ★, test boundaries ★★; optional rich outside the solution chain.
- Verified Ex 6 slate/crane transcript and four passing tests. Explicit pytest pythonpath configuration is necessary when continuing from Ex 5.
- Ex 6 slide references: Packages in Python; from...import Statement; Installing Packages.

- Exercise 7 rewritten: render ★★; consistent ★; candidates ★★★; letter_counts/best_guess ★★; hint integration ★★; optional automatic solver.
- Verified Ex 7 eight tests and slate/hint/crane output (15 candidates, GRACE). Solver handout imports all four functions, so text explicitly defers collection until Step 4 while the game remains playable.
- Ex 7 slide references: Zip Function; Filtered List Comprehension; Dictionary Comprehensions; Set Comprehensions; Built-ins that Take a Function.

- Exercise 8 rewritten: InvalidGuess ★; validator/wrapper ★★; game recovery ★★; main recovery ★★; first student-written tests ★★★; optional extra validation tests.
- Verified Ex 8 eleven passing tests and all three rejected guesses followed by a first-turn win.
- Ex 8 slide references: User Defined Exceptions; Raising Exceptions; Typed Exception Handling.
- PDF/site builds and rendered review completed on 2026-10-17.


## Resumed completion (2026-10-17)

Branch: `t3/exercise-texts-5-to-8`. Merged `t3/wp2b-exercise-texts` as requested (7bbcd7e); no push or subsequent merge. Removed the inherited generated site from the index in 2abc9dc. Original exercise commits remain in history: 3784acc, 0a2789a, b49fd99, 9617909, plus their inherited fixups. Resumed exercise commits: ba62411 (5), 3e60c39 (6), 887018b (7), and the commit containing this final report (8).

### Steps and verification

- Exercise 5: bug reproduction ★, main/loader ★, validation ★★, scoring ★★★, rendering ★★, play ★★; optional hard mode. Fresh starter run with `error`, `crane` reproduces `(E)[R](R) O (R)`; solution gives `(E)[R] R  O  R ` and wins in two. Nine tests pass; the selected scoring run passes five with four deselected. Clarified removing the old quit print. Moved the final main implementation into the solution to keep the Step 6 hint and solution cue together on paper.
- Exercise 6: package ★, module split ★★, module execution ★, test imports ★★; optional rich only. Fresh `slate`, `crane` game wins in two; four tests pass. Explained the temporarily mixed test imports and the required pytest pythonpath setting.
- Exercise 7: renderer ★★, consistency ★, candidates ★★★, counts/recommendation ★★, hint integration ★★; optional automatic solver. Eight tests pass; `slate`, `hint`, `crane` yields `15 words left, try GRACE`, keeps guess 2 available, and wins in two. Corrected the description of the consistency test: its negative assertion changes the guess to raise, not the proposed secret. Normalised fence/container spacing and shortened Step 1 to avoid a cue-only PDF page.
- Exercise 8: exception ★, validation/wrapper ★★, game recovery ★★, main recovery ★★, own tests ★★★; optional extra validation tests. Eleven tests pass. `cran`, `cr4ne`, `zzzzz`, `crane` prints all three specified reasons and wins on turn one. Also ran the missing-file and EOF paths from a temporary copy: both print the reference messages and exit successfully. Normalised markup and kept the Step 3 hint together on paper.

### Gates and rendered review

- `uv sync`: pass.
- `uv run python build/check-fences.py`: pass, 334 fences, no problems.
- `uv run ruff check .`: pass.
- From build/: `bun run C:/Git/courseWare/Presentation-Template/build/build.ts --exercises --skip-lint`: pass after final edits.
- From build/: `bun run site.config.ts`: pass after final edits, using `PRESENTATION_TEMPLATE_DIR=C:/Git/courseWare/Presentation-Template` because the worktree has no sibling template checkout.
- Opened all four generated pages in the T3 browser. Verified all hint/output/solution disclosures open, the solution confirmation works, tier sequences match the steps, and all 13 italic references become slide buttons. Rechecked the final Exercise 5 solution placement on the site.
- Rendered the exercise PDF with PyMuPDF for visual review. Corrected stranded cues/split hints in Exercises 5, 7 and 8 and inspected the final affected pages. Long reference-code lines wrap in the shared PDF style; no source changes were made to disguise those exact excerpts.

### Exact italic slide references

- 5: *Annotating a Function*; *Default Arguments*.
- 6: *Packages in Python*; *from...import Statement*; *Installing Packages*.
- 7: *Zip Function*; *Filtered List Comprehension*; *Dictionary Comprehensions*; *Set Comprehensions*; *Built-ins that Take a Function*.
- 8: *User Defined Exceptions*; *Raising Exceptions*; *Typed Exception Handling*.

### Coordinator-only follow-up and reference limitations

- `uv run python build/make-starters.py --check` fails for Exercise 5 only. A fresh generated tree compared against the current starter has exactly one extra file: `uv.lock`, committed by the inherited WIP. Remove that tracked generated lock file. The checker also excludes locks while generating but does not ignore them while comparing, so running a starter can recreate this failure; align those policies in the generator. No starter or generator changes made here.
- Exercise 7's handout imports all four solver functions at collection time. This prevents running the candidates test in Step 3 before Step 4 exists. Text explicitly defers full collection and offers a direct assertion check. Consider splitting tests or moving imports inside tests for immediate step-by-step feedback.
- Exercise 6 reference code drops local collection annotations retained in Exercise 5 (`used_letters`, `unmatched`); Exercise 7's `history` is also unannotated. Text preserves annotations when moving student functions and quotes later reference excerpts exactly. Coordinator should decide whether to restore local annotations across the reference chain.
- No failing reference-solution tests or game-output discrepancies found. Rich remains outside the solution chain. Exercise 8 exception tests remain absent from the handout as intended.

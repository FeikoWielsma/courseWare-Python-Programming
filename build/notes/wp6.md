> Historical record (2026-10-17). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# WP6 : PRG400 exercise-site extras

Implementation notes for the course-side quiz, starter rows and Wordle Easter egg.

- Starter rows follow the shipped starter and solution stages: no row for Exercise 1; script invocation in Exercises 2 to 5; package invocation from Exercise 6; tests from Exercise 5; mypy from Exercise 12.
- `build/site/quiz.json` is the shared data source for the site quiz and Python snippet checker. Each code example's stdout is checked against its keyed answer.
- The Wordle plug-in is course-owned and adds only its own inlined CSS and JavaScript. Its duplicate scoring marks greens first and spends only unmatched copies on yellow marks.
- Question counts: module 01: 2; 02: 3; 03: 3; 04: 4; 05: 4; 06: 2; 07: 3; 08: 2; 09: 2; 10: 3; 11: 4; appendix 12: 4; appendix 13: 3. Total: 39. The checker runs all 25 code examples.
- Headless `file://` checks passed for starter rows on 01, 04, 05, 06 and 12; the quiz reached its result screen; typing `wordle` opened the egg and `error` against `crane` scored yellow, green, grey, grey, grey before Escape closed it.
- Coordinator follow-up needed: run `uv run python build/site/check-quiz.py` in CI beside the existing fence and Ruff checks.

> Historical record (2026-10-14). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# WP1 progress

## Status

- Completed the reference solutions for Exercises 1–13, all specified handouts, word lists, transcripts, starter generation and the coordinator checker.
- Moved the three superseded calculator solution folders into `archive/calculator/solutions/`.
- `build/check-solutions.py` passes all 13 stages. Test counts: Ex 5 (9), Ex 6 (4), Ex 7 (8), Ex 8 (11), Ex 9 (9), Ex 10 (9), Ex 11 (12), Ex 12 (12), Ex 13 (17). Exercises 1–4 have no tests. Mypy passes for 12 and 13.
- `uv sync`, fence check, `ruff check .`, solution compileall, and `make-starters.py --check` pass. The broad `compileall demos solutions` command also reaches non-bundled legacy Python 2 demo folders and fails there; the release workflow's allowlisted demo folders plus `solutions` compile successfully.
- Remaining in WP1: none. Coordinator follow-up is listed below.

## Decisions

- Use the requested stage folder names exactly, including `01-environment-configuration`, `12-type-hinting` and `13-python-libraries`.
- For Exercises 1–3, transcripts record their demonstration scripts because the plan does not introduce a playable game until Exercise 4.
- The answer list has 935 unique common, family-friendly five-letter words. The allowed list contains every five-letter ASCII ENABLE entry plus all course answers.
- Exercise 9 reads cleaned `wordle/data/words.txt` and includes the required `answers.txt` and `allowed.txt` files.
- Names chosen where the plan leaves names open: `load_allowed`, `history_path`, `print_stats`, `follows_hints`, `SAVE_PATH`, `save_game`, `load_saved_game`, and `clear_saved_game`.

## Coordinator changes needed

- Add `pytest` to the root `pyproject.toml` development group as specified in plan section 7.
- Add CI steps `uv run python build/make-starters.py --check` and `uv run python build/check-solutions.py`.
- No `ruff.toml` exception is needed. The required `InvalidGuess` API name has a local `# noqa: N818` comment.

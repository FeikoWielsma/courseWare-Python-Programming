# WP2a progress : exercise texts 1 to 4

## Done

- Ex 1 : rewritten for the `wordle` project.

## Left

- Ex 2, Ex 3, Ex 4; gates; PDF and site build.

## Decided

- Ex 1 adds `ruff` with `uv add --dev ruff`, because `uv run ruff` in a fresh project only works when ruff is installed globally.
- Ex 1 renames `main.py` to `wordle.py`, because `solutions/01-environment-configuration/` has `wordle.py` and no `main.py`, and Ex 2 to 5 run `wordle.py`.
- Ex 1's If time copies the ruff demo into the student project, because the course's `ruff.toml` excludes it from a run in the course folder.

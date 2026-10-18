> Historical record (2026-10-17). Current commands and defaults: MAINTAINING.md; index: README.md in this folder.

# WP2a progress : exercise texts 1 to 4

## Done

- Ex 1 to Ex 4 written for the Wordle spine, verified against the solutions, and built (PDF and site).
- Every quoted output was produced by running the solution, or for Ex 4 Steps 1 to 4 the intermediate stage
  assembled from the step solutions, with `WORDLE_SECRET=crane`. Ex 1's `uv init`, `uv add --dev ruff` and
  ruff transcripts were produced in a fresh `uv init wordle` project.
- Ex 4's text was first committed inside the WIP commit `7e16656`; it needed no change on resume.

## Left

- Nothing in WP2a. Coordinator items are in the report.

## Decided

- Ex 1 adds `ruff` with `uv add --dev ruff`, because `uv run ruff` in a fresh project only works when ruff is installed globally. It says pytest arrives the same way in Ex 5.
- Ex 1 renames `main.py` to `wordle.py`, because `solutions/01-environment-configuration/` has `wordle.py` and no `main.py`, and Ex 2 to 5 run `wordle.py`.
- Ex 1's If time copies the ruff demo into the student project, because the course's `ruff.toml` excludes it from a run in the course folder.
- Ex 1 quotes the ruff finding in full rather than its first lines.
- The If time permits headings in Ex 2 to 4 keep a tier pill (plan section 4 gives them one); the site still treats them as optional.

## Coordinator changes needed

- `solutions/01..04/pyproject.toml` carry `dev = ["pytest>=8"]` and no `ruff`. The text adds ruff in Ex 1 and pytest in Ex 5, so the dev group of 01 to 04 should be `["ruff"]` (and 05 on `ruff` plus `pytest`). Regenerate starters afterwards.
- The site launcher needs `PRESENTATION_TEMPLATE_DIR` in a T3 worktree, because `../../Presentation-Template` does not exist there.

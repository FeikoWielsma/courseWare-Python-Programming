> Historical record (2026-10-14). Current commands and defaults: MAINTAINING.md; index: ../README.md.

# WP3e Progress Notes: Appendix slides and demos 12 & 13

## Status
- **Module 12 (Type Hinting)**: Done.
  - Added slide `Closed Sets with Literal` and demo `06_literal.py`.
  - Explains why `Literal` rather than `str` (closed set vs arbitrary string).
  - Shows real output of `mypy` reporting value outside the set.
  - Updated recap and summary slides.
  - Fixed stale path comment in `05_mypy_error.py`.
  - Demos 01 to 06 gap-free.
- **Module 13 (Libraries & Testing)**: Done.
  - Added slide `Command-Line Arguments with sys.argv` and demo `09_sys_argv.py` with pointer to `argparse`.
  - Replaced the 3 `unittest` slides and 2 demos with 3 `pytest` slides and 3 demos:
    1. Slide `Testing with pytest` (`test_` prefix, plain `assert`, `uv add --dev pytest`, `uv run pytest`, `uv run pytest -v`) and demo `10_pytest_basic.py`.
    2. Slide `Reading a Test Failure` (deliberately failing test, real failure report output from pytest) and demo `11_pytest_failure.py`.
    3. Slide `Exceptions and Parametrized Tests` (`pytest.raises`, `@pytest.mark.parametrize`) and demo `12_pytest_features.py`.
  - Replaced `09_unittest_basic.py` and `10_unittest_fixtures.py` with `09_sys_argv.py`, `10_pytest_basic.py`, `11_pytest_failure.py`, and `12_pytest_features.py`.
  - Updated `Standard Library Overview` and `Summary : Python Libraries` slides.
  - Renumbered demo files and pills gap-free (01 to 12).
- **Gates**:
  - `uv sync`: clean.
  - `uv run python build/check-fences.py`: 330 fences checked, all clean.
  - `uv run ruff check .`: clean (0 errors).
  - `uv run python -m compileall -q demos/12-appendix-type-hinting demos/13-appendix-libraries`: clean.
  - `bun run C:/Git/courseWare/Presentation-Template/build/build.ts`: built cleanly (237 slides total).
  - `bun run C:/Git/courseWare/Presentation-Template/build/lint-slides.ts`: all slides within budget.
  - All demos in 12 and 13 run under Python 3.14.

## Decisions
- D6 & Q9 followed: neutral traffic light colors (`"red"`, `"amber"`, `"green"`) used for `Literal`.
- Demos numbered gap-free:
  - 12: 01 to 06.
  - 13: 01 to 12.
- `ruff.toml`: No per-file-ignore paths broken (demos/13-appendix-libraries had no entries).

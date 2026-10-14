# WP3e Progress Notes: Appendix slides and demos 12 & 13

## Status
- **Module 12 (Type Hinting)**: Done.
  - Added slide `Closed Sets with Literal` and demo `06_literal.py`.
  - Explains why `Literal` rather than `str` (closed set vs arbitrary string).
  - Shows real output of `mypy` reporting value outside the set.
  - Updated recap and summary slides.
  - Fixed stale path comment in `05_mypy_error.py`.
- **Module 13 (Libraries & Testing)**: In progress.
  - Need to add `sys.argv` slide and demo `09_sys_argv.py` with pointer to `argparse`.
  - Need to replace 3 `unittest` slides with 3 `pytest` slides:
    1. `Testing with pytest` (`test_` prefix, plain `assert`, `uv add --dev pytest`, `uv run pytest`, `uv run pytest -v`).
    2. `Reading a Test Failure` (deliberate failure, real failure report output from pytest).
    3. `Exceptions and Parametrized Tests` (`pytest.raises`, `@pytest.mark.parametrize`).
  - Need to replace `09_unittest_basic.py` and `10_unittest_fixtures.py` with:
    - `09_sys_argv.py`
    - `10_pytest_basic.py`
    - `11_pytest_failure.py`
    - `12_pytest_features.py`
  - Update `Standard Library Overview` and `Summary : Python Libraries` slides.
  - Renumber demo files and pills gap-free (01 to 12).

## Decisions
- D6 & Q9 followed: neutral traffic light colors (`"red"`, `"amber"`, `"green"`) used for `Literal`.
- Demos numbered gap-free:
  - 12: 01 to 06.
  - 13: 01 to 12.
- `Co-Authored-By: gemini-3.8-flash-high <noreply@google.com>`

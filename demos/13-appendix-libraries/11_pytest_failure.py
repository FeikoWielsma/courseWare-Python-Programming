"""A deliberately failing test to demonstrate pytest's failure reports.

Run with pytest to see the failure report :

    uv run pytest demos/13-appendix-libraries/11_pytest_failure.py
"""


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def test_wrong_sum() -> None:
    assert add(2, 3) == 6


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

"""A test is a function whose name starts with test_ and uses plain assert.

Run the tests with pytest :

    uv run pytest demos/13-appendix-libraries/10_pytest_basic.py
    uv run pytest -v demos/13-appendix-libraries/10_pytest_basic.py
"""


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def test_positive_numbers() -> None:
    assert add(2, 3) == 5


def test_with_zero() -> None:
    assert add(0, 7) == 7


def test_negative_numbers() -> None:
    assert add(-2, -3) == -5


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

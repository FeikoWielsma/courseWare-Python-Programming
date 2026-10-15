"""Testing expected exceptions and parametrized tests with pytest.

Run with pytest :

    uv run pytest demos/13-appendix-libraries/12_pytest_features.py
    uv run pytest -v demos/13-appendix-libraries/12_pytest_features.py
"""

import pytest


def divide(a: int, b: int) -> float:
    """Divide a by b, raising ValueError when b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (5, 2, 2.5),
    ],
)
def test_divide(a: int, b: int, expected: float) -> None:
    assert divide(a, b) == expected


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

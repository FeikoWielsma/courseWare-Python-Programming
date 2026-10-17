import pytest


def divide(a: float, b: float) -> float:
    return a / b


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

"""Solution to Exercise 13, step 4 : the module under test."""


def add(i: float, j: float) -> float:
    """Return the sum of two numbers."""
    return i + j


def subtract(i: float, j: float) -> float:
    """Return the difference of two numbers."""
    return i - j


def multiply(i: float, j: float) -> float:
    """Return the product of two numbers."""
    return i * j


def divide(i: float, j: float) -> float:
    """Return the quotient of two numbers, refusing a zero divisor."""
    if j == 0:
        raise ValueError("cannot divide by zero")
    return i / j

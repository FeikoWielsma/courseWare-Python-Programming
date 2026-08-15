"""A deliberate type error, for mypy to find.

The file runs without complaint. Only the checker objects :

    uv run mypy demos/00a-modern-python/07_mypy_error.py

    error: Argument 1 to "double" has incompatible type "str"; expected "int"
"""


def double(n: int) -> int:
    """Double a number."""
    return n * 2


result: int = double("ab")
print(result)

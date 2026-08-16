"""Solution to Exercise 12, steps 2 to 5.

Run the checker over this file to see it pass :

    uv run mypy shapes12.py
"""


def area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height


def describe(name: str, size: float) -> str:
    """Describe a room and its area."""
    return f"{name} has an area of {size}"


def average(values: list[float]) -> float:
    """Return the mean of a list of numbers."""
    return sum(values) / len(values)


def greet(name: str | None = None) -> str:
    """Greet someone by name, or greet a stranger.

    Annotating this `name: str = None` would be a lie, because the default is
    not a str. `str | None` is what makes the default honest.
    """
    if name is None:
        return "Hello, stranger"
    return f"Hello, {name}"


print(describe("kitchen", area(3.0, 4.0)))
print(average([1.0, 2.0, 3.0]))
print(greet())
print(greet("Alice"))

# Step 3 asked you to swap the two arguments and run mypy again. Uncommenting
# the line below still runs, and still prints nonsense, but mypy reports:
#   Argument 1 to "describe" has incompatible type "float"; expected "str"
# print(describe(area(3.0, 4.0), "kitchen"))

# Step 4 asked for a list of the wrong type. This too runs until it does not,
# and mypy reports it without running anything:
#   List item 0 has incompatible type "str"; expected "float"
# print(average(["a", "b"]))

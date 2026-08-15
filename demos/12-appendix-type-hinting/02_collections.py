"""Annotating the built-in container types."""

scores: list[int] = [10, 20, 30]
names: set[str] = {"Alice", "Bob"}
ages: dict[str, int] = {"Alice": 30, "Bob": 25}

point: tuple[int, int] = (3, 4)
row: tuple[str, int, float] = ("Audi", 2019, 52643.0)

# An ellipsis means "more of the same type", for a tuple of unknown length.
readings: tuple[float, ...] = (1.5, 2.5, 3.5, 4.5)


def average(values: list[float]) -> float:
    """Return the mean of a list of numbers."""
    return sum(values) / len(values)


print(scores, names, ages)
print(point, row, readings)
print(average([1.0, 2.0, 3.0]))

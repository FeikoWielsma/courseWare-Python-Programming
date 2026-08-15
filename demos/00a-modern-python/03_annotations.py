"""Annotating variables and function signatures."""

age: int = 25
height: float = 1.87
name: str = "Alice"
is_student: bool = True

print(age, height, name, is_student)


def area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height


def log_message(message: str) -> None:
    """Print a message and return nothing."""
    print(message)


print(area(3.0, 4.0))
log_message("annotated and run")

"""Structural pattern matching, added in Python 3.10 (PEP 634)."""


def describe(command: str) -> str:
    """Match a command against a series of patterns."""
    match command.split():
        # A literal pattern, matched by value.
        case ["quit"]:
            return "leaving"
        # A capture pattern: the second word is bound to the name.
        case ["go", direction]:
            return f"walking {direction}"
        # An or-pattern, and a guard that must also hold.
        case ["take" | "get", item] if item != "moon":
            return f"picking up the {item}"
        # A wildcard, which matches anything the earlier cases did not.
        case _:
            return "I do not understand"


for line in ["quit", "go north", "take lamp", "take moon", "sing"]:
    print(f"{line:12} -> {describe(line)}")


def area(shape: tuple) -> float:
    """Match on the shape of the data, not just its value."""
    match shape:
        case ("circle", radius):
            return 3.14159 * radius**2
        case ("rectangle", width, height):
            return width * height
        case _:
            raise ValueError(f"unknown shape: {shape}")


print(area(("circle", 2)))
print(area(("rectangle", 3, 4)))

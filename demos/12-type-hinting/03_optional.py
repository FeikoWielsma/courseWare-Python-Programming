"""A parameter that may be absent is typed with `| None`."""


def greet(name: str | None = None) -> str:
    """Greet someone by name, or greet a stranger."""
    if name is None:
        return "Hello, stranger"
    return f"Hello, {name}"


def parse(value: str | int) -> int:
    """Accept either a string or an integer and return an integer."""
    return int(value)


print(greet())
print(greet("Alice"))
print(parse("42"), parse(42))

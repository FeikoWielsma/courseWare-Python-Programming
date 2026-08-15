"""Annotations are ignored while the program runs."""


def double(n: int) -> int:
    """Double a number, at least when it is given one."""
    return n * 2


# The annotation says int. Passing a string is not an error at runtime :
# str supports *, so this prints abab.
print(double("ab"))

# The annotations are kept, and can be read back.
print(double.__annotations__)

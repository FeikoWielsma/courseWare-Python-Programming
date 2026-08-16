"""Built-in functions that take a function, and the two that reduce to a bool."""

words = ["ticket", "to", "mars", "one", "way"]

# sorted() returns a new list; list.sort() rearranges in place and returns None.
print(sorted(words))
print(sorted(words, reverse=True))

# key= takes a function, applied to each element to decide the order. The
# elements themselves are returned untouched.
print(sorted(words, key=len))
print(sorted(words, key=str.upper))

# min and max take the same key.
print(min(words, key=len), max(words, key=len))

numbers = [4, 8, 15, 16, 23, 42]

# any() is True when at least one element is true, all() when every one is.
print(any(n > 40 for n in numbers))
print(all(n > 40 for n in numbers))
print(all(n % 2 == 0 for n in numbers))

# Both stop as soon as the answer is known, so they are cheap on long sequences.
print(any(word.startswith("t") for word in words))

# An empty sequence: any() is False, all() is True. Worth knowing before it
# surprises you.
print(any([]), all([]))

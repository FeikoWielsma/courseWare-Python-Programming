"""Lambda expressions: small anonymous functions passed to another function."""

words = ["banana", "pie", "Washington", "book"]

# Sort by last letter
by_last = sorted(words, key=lambda w: w[-1])
print("By last letter  :", by_last)

# Sort case-insensitively
by_case = sorted(words, key=lambda w: w.lower())
print("Case-insensitive:", by_case)

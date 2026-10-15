words = ["ticket", "to", "mars", "one", "way"]
print(sorted(words))  # ['mars', 'one', 'ticket', 'to', 'way']
print(sorted(words, key=len))  # ['to', 'one', 'way', 'mars', 'ticket']
print(min(words, key=len), max(words, key=len))  # to ticket

track = ("Imagine", "John Lennon", 183)
print(track[0])  # Imagine
print(track[1:])  # ('John Lennon', 183)
print(len(track))  # 3
# track[2] = 240  # TypeError: tuple items cannot be assigned.

long_mix = track[:2] + (240,)
print(long_mix)  # ('Imagine', 'John Lennon', 240)
print(track)  # ('Imagine', 'John Lennon', 183)

titles = ("Imagine", "Yesterday", "Respect")
shorter = titles[:-1]
print(shorter)  # ('Imagine', 'Yesterday')
del titles
print(shorter)  # ('Imagine', 'Yesterday')

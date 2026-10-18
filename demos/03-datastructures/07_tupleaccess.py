track = ("Orbit", "Nova", 222)
print(track[0])  # Orbit
print(track[1:])  # ('Nova', 222)
print(len(track))  # 3
# track[2] = 240  # TypeError: tuple items cannot be assigned.

long_mix = track[:2] + (240,)
print(long_mix)  # ('Orbit', 'Nova', 240)
print(track)  # ('Orbit', 'Nova', 222)

titles = ("Orbit", "Echo", "Pulse")
shorter = titles[:-1]
print(shorter)  # ('Orbit', 'Echo')
del titles
print(shorter)  # ('Orbit', 'Echo')

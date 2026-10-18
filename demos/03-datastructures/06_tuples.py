track = ("Orbit", 222)
dimensions = (1920, 1080)
titles = "Orbit", "Echo"  # The comma creates a tuple.
empty = ()
single = ("Orbit",)  # A one-item tuple needs the comma.
print(track, dimensions, titles, empty, single)
print(track[0])  # Orbit
print(track[1])  # 222
print(tuple())  # ()

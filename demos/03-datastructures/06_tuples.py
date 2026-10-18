track = ("Imagine", 183)
dimensions = (1920, 1080)
titles = "Imagine", "Yesterday"  # The comma creates a tuple.
empty = ()
single = ("Imagine",)  # A one-item tuple needs the comma.
print(track, dimensions, titles, empty, single)
print(track[0])  # Imagine
print(track[1])  # 183
print(tuple())  # ()

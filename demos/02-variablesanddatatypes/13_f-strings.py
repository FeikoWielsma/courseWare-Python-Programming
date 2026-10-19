title = "Imagine"
seconds = 222
print(f"Now playing: {title.upper()}")
print(f"With a 30-second intro: {seconds + 30} seconds")

print(f"{title!r}")  # 'Imagine', quotes remain visible
print(f"{seconds = }")  # seconds = 222, useful during debugging

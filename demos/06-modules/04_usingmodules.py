from timing import format_duration

tracks = {"Imagine": 183, "Yesterday": 125}
for title, seconds in tracks.items():
    label = format_duration(seconds)
    print(f"{title}: {label}")

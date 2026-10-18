from timing import format_duration

tracks = {"Orbit": 222, "Echo": 185}
for title, seconds in tracks.items():
    label = format_duration(seconds)
    print(f"{title}: {label}")

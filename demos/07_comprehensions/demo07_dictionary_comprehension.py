durations = {"Imagine": 183, "Yesterday": 125, "Respect": 149}
short_tracks = {title: seconds for title, seconds in durations.items() if seconds < 150}
print(short_tracks)  # {'Yesterday': 125, 'Respect': 149}
minutes = {title: round(seconds / 60, 2) for title, seconds in durations.items()}
print(minutes)  # {'Imagine': 3.05, 'Yesterday': 2.08, 'Respect': 2.48}

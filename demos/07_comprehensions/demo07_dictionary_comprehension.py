durations = {"Orbit": 222, "Echo": 185, "Pulse": 204}
short_tracks = {title: seconds for title, seconds in durations.items() if seconds < 200}
print(short_tracks)  # {'Echo': 185}
minutes = {title: round(seconds / 60, 1) for title, seconds in durations.items()}
print(minutes)  # {'Orbit': 3.7, 'Echo': 3.1, 'Pulse': 3.4}

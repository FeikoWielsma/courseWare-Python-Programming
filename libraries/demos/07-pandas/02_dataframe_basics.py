import pandas as pd

tracks = pd.DataFrame({
    "title": ["Imagine", "Yesterday", "Respect"],
    "artist": ["John Lennon", "The Beatles", "Aretha Franklin"],
    "duration_s": [183, 126, 146],
})
print(tracks)
print(tracks.shape)
print(tracks["duration_s"])

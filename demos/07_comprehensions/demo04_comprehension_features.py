def format_duration(seconds: int) -> str:
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder:02d}"


tracks = [("Orbit", 222), ("Echo", 185), ("Pulse", 204)]
labels = [f"{title} [{format_duration(seconds)}]" for title, seconds in tracks]
print(labels)

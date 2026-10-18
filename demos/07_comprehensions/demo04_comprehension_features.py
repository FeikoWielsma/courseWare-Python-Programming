def format_duration(seconds: int) -> str:
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder:02d}"


tracks = [("Imagine", 183), ("Yesterday", 125), ("Respect", 149)]
labels = [f"{title} [{format_duration(seconds)}]" for title, seconds in tracks]
print(labels)

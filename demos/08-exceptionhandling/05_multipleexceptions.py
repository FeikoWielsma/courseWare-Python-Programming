lengths = [222, None, "live"]
for length in lengths:
    try:
        print(f"Length: {int(length)} seconds")
    except (TypeError, ValueError):
        print(f"Missing or invalid duration: {length!r}")

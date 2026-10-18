text = "three"
try:
    seconds = int(text)
except ValueError:
    print(f"Invalid track length: {text!r}")

text = "222"
try:
    seconds = int(text)
except ValueError:
    print(f"Invalid track length: {text!r}")
else:
    print(f"Track length: {seconds} seconds")

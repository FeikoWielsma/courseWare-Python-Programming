text = "live"
try:
    int(text)
except ValueError as error:
    print(f"Cannot read track length {text!r}: {error}")
    print(error.args)

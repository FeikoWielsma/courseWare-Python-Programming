def parse_duration(text: str) -> int:
    minutes_text, seconds_text = text.split(":")
    minutes = int(minutes_text)
    seconds = int(seconds_text)
    if minutes < 0 or not 0 <= seconds < 60:
        raise ValueError(f"Invalid duration: {text!r}")
    return minutes * 60 + seconds


print(parse_duration("3:42"))
try:
    parse_duration("3:99")
except ValueError as error:
    print(error)
    raise  # Let the caller decide how to recover.

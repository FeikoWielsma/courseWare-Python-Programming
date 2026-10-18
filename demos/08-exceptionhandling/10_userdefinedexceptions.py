class InvalidDurationError(ValueError):
    pass


def parse_duration(text: str) -> int:
    minutes_text, seconds_text = text.split(":")
    minutes = int(minutes_text)
    seconds = int(seconds_text)
    if minutes < 0 or not 0 <= seconds < 60:
        raise InvalidDurationError(f"Invalid duration: {text!r}")
    return minutes * 60 + seconds


try:
    parse_duration("3:99")
except InvalidDurationError as error:
    print(f"Playlist entry rejected: {error}")

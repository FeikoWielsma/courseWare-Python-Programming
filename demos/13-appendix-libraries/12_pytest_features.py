import pytest


def format_duration(seconds: int) -> str:
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder:02d}"


def parse_duration(text: str) -> int:
    minutes_text, seconds_text = text.split(":")
    minutes = int(minutes_text)
    seconds = int(seconds_text)
    if minutes < 0 or not 0 <= seconds < 60:
        raise ValueError(f"Invalid duration: {text!r}")
    return minutes * 60 + seconds


def test_invalid_duration() -> None:
    with pytest.raises(ValueError):
        parse_duration("3:99")


@pytest.mark.parametrize(
    ("seconds", "expected"),
    [(0, "0:00"), (59, "0:59"), (60, "1:00"), (3600, "60:00")],
)
def test_duration_display(seconds: int, expected: str) -> None:
    assert format_duration(seconds) == expected

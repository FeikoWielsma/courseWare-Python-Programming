def format_duration(seconds: int) -> str:
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder:02d}"


def test_minutes_and_seconds() -> None:
    assert format_duration(222) == "3:42"


def test_exact_minute() -> None:
    assert format_duration(60) == "1:00"

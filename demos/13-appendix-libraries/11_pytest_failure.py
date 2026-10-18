def format_duration(seconds: int) -> str:
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder}"


def test_exact_minute() -> None:
    assert format_duration(60) == "1:00"

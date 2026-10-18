def repeat_track(title: str, count: int) -> list[str]:
    return [title] * count


queue: list[str] = repeat_track(222, 2)

def repeat_track(title: str, count: int) -> list[str]:
    return [title] * count


print(repeat_track(222, 2))  # [222, 222], despite the str annotation.
print(repeat_track.__annotations__)

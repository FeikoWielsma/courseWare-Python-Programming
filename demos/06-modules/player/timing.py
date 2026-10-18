SECONDS_PER_MINUTE: int = 60


def format_duration(seconds: int) -> str:
    minutes = seconds // SECONDS_PER_MINUTE
    remainder = seconds % SECONDS_PER_MINUTE
    return f"{minutes}:{remainder:02d}"

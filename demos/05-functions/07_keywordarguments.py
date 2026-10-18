def format_duration(seconds: int, separator: str) -> str:
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}{separator}{remainder:02d}"


print(format_duration(separator=".", seconds=222))

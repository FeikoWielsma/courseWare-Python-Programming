def format_duration(seconds: int) -> str:
    """Format a non-negative track length as minutes and two-digit seconds."""
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder:02d}"


help(format_duration)

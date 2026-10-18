def format_duration(seconds):
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes}:{remainder:02d}"

label = format_duration(222)
message = f"Orbit [{label}]"
print(message)

def clean_title(title: str) -> str:
    return title.strip()


def shout_title(title: str) -> str:
    return title.upper()


formatters = {"clean": clean_title, "shout": shout_title}
print(formatters["clean"]("  Orbit  "))
for name, format_title in formatters.items():
    print(name, format_title("Echo"))

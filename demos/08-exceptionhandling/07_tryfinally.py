def parse_seconds(text: str) -> int:
    try:
        return int(text)
    finally:
        print("Duration check finished")


try:
    parse_seconds("live")
except ValueError:
    print("Duration unavailable")

volume = 50
queue_limit = 20

def preview_volume() -> None:
    volume = 10
    print(f"Preview volume: {volume}")


def set_limit() -> None:
    global queue_limit
    queue_limit = 30

preview_volume()
print(f"Current volume: {volume}")
set_limit()
print(f"Queue limit: {queue_limit}")

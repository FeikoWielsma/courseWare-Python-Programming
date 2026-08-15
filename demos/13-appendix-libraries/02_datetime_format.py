"""Turning a datetime into text, and text back into a datetime."""

from datetime import datetime

launch = datetime(2026, 8, 15, 12, 30, 0)

# strftime formats, strptime parses. The f is for format, the p is for parse.
print(launch.strftime("%d-%m-%Y %H:%M"))
print(launch.strftime("%A %d %B %Y"))

parsed = datetime.strptime("24-12-2026 18:00", "%d-%m-%Y %H:%M")
print(parsed)

# ISO 8601 needs no format string at all, in either direction.
print(launch.isoformat())
print(datetime.fromisoformat("2026-12-24T18:00:00"))

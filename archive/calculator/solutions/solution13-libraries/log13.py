"""Solution to Exercise 13, step 3 : regular expressions."""

import re

lines = [
    "2026-08-15 12:30 ERROR disk full",
    "2026-08-15 12:31 INFO backup started",
    "2026-08-15 12:45 WARN disk at 91 percent",
    "2026-08-16 09:02 ERROR connection refused",
]

pattern = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}) "
    r"(?P<level>\w+) (?P<message>.*)"
)

for line in lines:
    match = pattern.match(line)
    if match and match.group("level") == "ERROR":
        print(f"{match.group('date')} {match.group('time')} : {match.group('message')}")

numbers: list[str] = []
for line in lines:
    match = pattern.match(line)
    if match:
        numbers.extend(re.findall(r"\d+", match.group("message")))
print("numbers in the messages :", numbers)

for line in lines:
    print(re.sub(r"\d{4}-\d{2}-\d{2}", "[date]", line))

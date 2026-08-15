"""Parentheses capture the part of the match you actually want."""

import re

line = "2026-08-15 12:30 ERROR disk full"

pattern = r"(\d{4})-(\d{2})-(\d{2}) (\d{2}:\d{2}) (\w+) (.*)"
m = re.search(pattern, line)
if m:
    print("whole match :", m.group(0))
    print("year        :", m.group(1))
    print("level       :", m.group(5))
    print("all groups  :", m.groups())

# Named groups read better than numbers once there are more than two.
named = re.search(r"(?P<level>ERROR|WARN|INFO) (?P<message>.*)", line)
if named:
    print(named.group("level"), "->", named.group("message"))

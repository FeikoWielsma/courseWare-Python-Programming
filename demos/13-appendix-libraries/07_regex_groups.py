import re

line = "12:30 PLAY Imagine"
match = re.search(r"(\d{2}):(\d{2}) (\w+) (.*)", line)
if match is not None:
    print(match.group(0))  # 12:30 PLAY Imagine
    print(match.groups())  # ('12', '30', 'PLAY', 'Imagine')

named = re.search(r"(?P<action>PLAY|SKIP) (?P<title>.*)", line)
if named is not None:
    print(named.group("action"))  # PLAY
    print(named.group("title"))  # Imagine

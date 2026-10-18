with open("playlist.txt", encoding="utf-8") as playlist:
    first = playlist.readline()
    rest = playlist.read()
print(repr(first))  # 'So What\n'
print(repr(rest))

with open("playlist.txt", encoding="utf-8") as playlist:
    for number, line in enumerate(playlist, start=1):
        print(f"{number}. {line.rstrip()}")

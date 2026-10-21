with open("last_played.txt", mode="w", encoding="utf-8") as fw:
    fw.write("So What\n")
# The file is closed here, even if write() raised.
print(fw.closed)  # True

with open("last_played.txt", encoding="utf-8") as fr:
    print(fr.read(), end="")  # So What

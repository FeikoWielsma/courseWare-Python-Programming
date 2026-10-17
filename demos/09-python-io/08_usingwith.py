with open("foo.txt", mode="w", encoding="utf-8") as fw:
    fw.write("one line\n")
# The file is closed here, even if write() raised.
print(fw.closed)  # True

with open("foo.txt", encoding="utf-8") as fr:
    print(fr.read(), end="")  # one line

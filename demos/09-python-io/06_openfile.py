text_file = open("playlist.txt", "rt", encoding="utf-8")
print(text_file)
text_file.close()

binary_file = open("playlist.txt", "rb")
print(binary_file)
binary_file.close()

raw_file = open("playlist.txt", "rb", buffering=0)
print(raw_file)
raw_file.close()

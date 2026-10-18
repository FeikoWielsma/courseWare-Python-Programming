from struct import pack, unpack

state = pack("<iii", 7, 184, 65)  # track number, seconds played, volume
with open("player.bin", mode="wb") as fw:
    fw.write(state)

with open("player.bin", mode="rb") as fr:
    track, seconds, volume = unpack("<iii", fr.read())
print(track, seconds, volume)  # 7 184 65

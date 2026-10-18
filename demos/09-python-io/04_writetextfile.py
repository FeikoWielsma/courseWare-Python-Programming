with open("road_trip.txt", mode="w", encoding="utf-8") as fw:
    fw.write("Jóga\n")
    fw.write("Hoppípolla\n")
    fw.write("Svefn-g-englar\n")

with open("road_trip.txt", mode="a", encoding="utf-8") as fa:
    fa.write("Glósóli\n")

with open("road_trip.txt", encoding="utf-8") as fr:
    print(fr.read(), end="")

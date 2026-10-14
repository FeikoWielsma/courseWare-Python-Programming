import csv

with open("planets.csv", "w", newline="", encoding="utf-8") as fw:
    writer = csv.writer(fw)
    writer.writerow(["name", "moons"])
    writer.writerows([["Earth", 1], ["Mars", 2]])

with open("planets.csv", newline="", encoding="utf-8") as fr:
    for row in csv.reader(fr):
        print(row)

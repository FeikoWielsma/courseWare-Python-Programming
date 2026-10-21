import csv

with open("history.csv", "w", newline="", encoding="utf-8") as fw:
    writer = csv.writer(fw)
    writer.writerow(["track", "artist", "seconds"])
    writer.writerows([["So What", "Miles Davis", 562], ["Hello, Goodbye", "The Beatles", 208]])

with open("history.csv", newline="", encoding="utf-8") as fr:
    for row in csv.reader(fr):
        print(row)

import csv

total = 0
with open("listening_history.csv", newline="", encoding="utf-8") as fr:
    for row in csv.DictReader(fr):
        seconds = int(row["seconds"])
        total += seconds
        print(f"{row['track']}: {seconds} s")
print(f"Total: {total // 60} min {total % 60} s")

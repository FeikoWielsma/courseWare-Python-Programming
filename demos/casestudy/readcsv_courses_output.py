import csv

courses = []

with open("courses.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f"{row[0]:10}{row[1]:10}{row[2]:15}{row[3]}")
            line_count += 1
        else:
            print(f"{row[0]:10}{row[1]:10}{row[2]:15}{row[3]}")
            line_count += 1
    print()
    print(f"Processed {line_count} courses.")

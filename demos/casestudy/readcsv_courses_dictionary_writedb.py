import sqlite3
import csv

courses = []
conn = sqlite3.connect('courses.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS courses")
c.execute("create table courses (name TEXT, duration TEXT, location TEXT, price TEXT)")

with open('courses.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for course in csv_reader:
        if line_count == 0:
            print(f'{"      ".join(course)}')
            line_count += 1
        print(f'{course["Name"]:10}{course["Duration"]:14}{course["Location"]:14}{course["Price"]}')
        line_count += 1
        courses.append(dict(course))
    print()
    print(f'Processed {line_count} courses.')

with conn:
    for course in courses:
        conn.execute("INSERT INTO courses VALUES( ?, ?, ?, ?)", tuple(course.values()))

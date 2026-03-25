import sqlite3
import csv

courses = []
conn = sqlite3.connect('courses.db')
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS courses")
c.execute("create table courses (name TEXT, duration TEXT, location TEXT, price TEXT)")

with open('courses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for course in csv_reader:
        if line_count == 0:
            print(f'{course[0]:10}{course[1]:10}{course[2]:15}{course[3]}')
            line_count += 1
        else:
            print(f'{course[0]:10}{course[1]:10}{course[2]:15}{course[3]}')
            line_count += 1
            courses.append(course)
    print()
    print(f'Processed {line_count} courses.')

with conn:
    for course in courses:
        conn.execute("INSERT INTO courses VALUES( ?, ?, ?, ?)", tuple(course))
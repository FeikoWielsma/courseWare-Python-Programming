rows = [(1,), (2,)]
for (number,) in rows:
    print(number)  # 1, then 2

records = [(1, ("Imagine", "John Lennon"))]
for number, (title, artist) in records:
    print(number, title, artist)  # 1 Imagine John Lennon

durations = {"Imagine": 183, "Yesterday": 125}
for title, seconds in durations.items():
    print(f"{title}: {seconds} seconds")

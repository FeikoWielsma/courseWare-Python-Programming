selection = ("Imagine", "Toxic")
print(selection)  # ('Imagine', 'Toxic')

primary, backup = selection

print(primary)  # 'Imagine'
print(backup)  # 'Toxic'

primary, backup = backup, primary

print(primary)  # 'Toxic'
print(backup)  # 'Imagine'

rows = [(1,), (2,)]
for (number,) in rows:
    print(number)  # 1, then 2

records = [(1, ("Imagine", "John Lennon"))]
for number, (title, artist) in records:
    print(number, title, artist)  # 1 Imagine John Lennon

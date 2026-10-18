selection = ("Orbit", "Nova")
print(selection)  # ('Orbit', 'Nova')

primary, backup = selection

print(primary)  # 'Orbit'
print(backup)  # 'Nova'

primary, backup = backup, primary

print(primary)  # 'Nova'
print(backup)  # 'Orbit'

rows = [(1,), (2,)]
for (number,) in rows:
    print(number)  # 1, then 2

records = [(1, ("Orbit", "Nova"))]
for number, (title, artist) in records:
    print(number, title, artist)  # 1 Orbit Nova

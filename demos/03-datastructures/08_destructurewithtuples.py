selection = ("Imagine", "Toxic")
print(selection)  # ('Imagine', 'Toxic')

primary, backup = selection

print(primary)  # 'Imagine'
print(backup)  # 'Toxic'

primary, backup = backup, primary

print(primary)  # 'Toxic'
print(backup)  # 'Imagine'

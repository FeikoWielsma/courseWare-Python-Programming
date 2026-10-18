durations = {"Imagine": 183, "Yesterday": 125, "Respect": 149}
print(durations)  # {'Imagine': 183, 'Yesterday': 125, 'Respect': 149}

durations["Toxic"] = 199
durations["Thriller"] = 357
print(durations)
# {'Imagine': 183, 'Yesterday': 125, 'Respect': 149, 'Toxic': 199, 'Thriller': 357}

print(durations["Yesterday"])  # 125
print(durations["Thriller"])  # 357

durations["Respect"] = 147
print(durations["Respect"])  # 147

del durations["Imagine"]
# print(durations["Imagine"])  # KeyError

durations.clear()  # remove all entries in dict
print(durations)  # {}

del durations  # delete entire dictionary
# print(durations)  # NameError: name 'durations' is not defined

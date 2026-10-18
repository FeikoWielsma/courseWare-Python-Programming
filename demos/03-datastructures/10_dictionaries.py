durations = {"Orbit": 222, "Echo": 185, "Pulse": 204}
print(durations)  # {'Orbit': 222, 'Echo': 185, 'Pulse': 204}

durations["Nova"] = 196
durations["Intro"] = 90
print(durations)  # {'Orbit': 222, 'Echo': 185, 'Pulse': 204, 'Nova': 196, 'Intro': 90}

print(durations["Echo"])  # 185
print(durations["Intro"])  # 90

durations["Pulse"] = 210
print(durations["Pulse"])  # 210

del durations["Orbit"]
# print(durations["Orbit"])  # KeyError

durations.clear()  # remove all entries in dict
print(durations)  # {}

del durations  # delete entire dictionary
# print(durations)  # NameError: name 'durations' is not defined

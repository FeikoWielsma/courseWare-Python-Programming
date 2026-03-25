planets = ["venus", "mars", "jupiter"]

print(len(planets))
print(range(len(planets)))
print(type(range(len(planets))))

for index in range(len(planets)):
    print("Current planet :", planets[index])
print("Lift off!")

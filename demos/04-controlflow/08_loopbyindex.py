"""Three ways to walk a sequence, from least to most Pythonic."""

planets = ["venus", "mars", "jupiter"]

# range(len(...)) works, and is what someone arriving from C or Java writes.
# It is worth seeing once, so that you recognise it.
print(len(planets))
print(range(len(planets)))
print(type(range(len(planets))))

for index in range(len(planets)):
    print("By index          :", planets[index])

# When the index is not needed, iterate the sequence itself.
for planet in planets:
    print("Directly          :", planet)

# When the index *is* needed, enumerate gives both, and cannot fall out of step
# with the sequence the way a separate counter can.
for index, planet in enumerate(planets):
    print(f"With enumerate    : {index} {planet}")

# enumerate counts from zero unless told otherwise.
for number, planet in enumerate(planets, start=1):
    print(f"Numbered from one : {number} {planet}")

print("Lift off!")

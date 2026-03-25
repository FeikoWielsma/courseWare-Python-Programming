for letter in "Python":
    if letter == "h":
        continue
    print("Current Letter :", letter)
print("After first loop!")

for letter in "Programming":
    if letter == "i":
        break
    print("Current Letter :", letter)
print("After second loop!")

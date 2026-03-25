
courselist =[]
count = 0
entrymode = True

while(entrymode):
    course = {}
    course["name"] = input("Enter course name : ")
    course["duration"] = input("Enter duration : ")
    course["location"] = input("Enter location : ")
    course["price"] = input("Enter price : ")
    courselist.append(course)
    count = count + 1
    if count == 2:
       entrymode = False

for c in courselist:
    print(c)

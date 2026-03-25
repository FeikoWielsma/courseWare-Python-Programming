import json

courselist = []

courselist.append(
    {"name": "Java", "duration": 5, "location": "Rotterdam", "price": 2450}
)
courselist.append(
    {"name": "Python", "duration": 4, "location": "Amsterdam", "price": 1750}
)

with open("courses.json", "w") as f:
    json.dump(courselist, f, indent=4)

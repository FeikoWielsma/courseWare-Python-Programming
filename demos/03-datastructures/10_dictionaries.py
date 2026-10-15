dict1 = {"Albert": 2341, "Robert": 9102, "Enrico": 3258}
print(dict1)  # {'Albert': 2341, 'Robert': 9102, 'Enrico': 3258}

dict1["Werner"] = 3490
dict1[2] = "Data"
print(dict1)  # {'Albert': 2341, 'Robert': 9102, 'Enrico': 3258, 'Werner': 3490, 2: 'Data'}

print(dict1["Robert"])  # 9102
print(dict1[2])  # Data

dict1["Enrico"] = 9999
print(dict1["Enrico"])  # 9999

del dict1["Albert"]
# print(dict1["Albert"])  # KeyError

dict1.clear()  # remove all entries in dict
print(dict1)  # {}

del dict1  # delete entire dictionary
# print(dict1)  # NameError: name 'dict1' is not defined

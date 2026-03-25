di1 = {"Albert": 2341, "Robert": 9102, "Enrico": 3258}
print(di1)  # {'Albert': 2341, 'Robert': 9102, 'Enrico': 3258}

di1["Werner"] = 3490
di1[2] = "Data"
print(
    di1
)  # {'Albert': 2341, 'Robert': 9102, 'Enrico': 3258, 'Werner': 3490, 2: 'Data'}

print(di1["Robert"])  # 9102
print(di1[2])  # Data

di1["Enrico"] = 9999
print(di1["Enrico"])  # 9999

del di1["Albert"]
# print(dict1['Albert'])    # KeyError

di1.clear()  # remove all entries in dict
print(di1)  # {}

del di1  # delete entire dictionary
print(di1)  # NameError: name 'di1' is not defined

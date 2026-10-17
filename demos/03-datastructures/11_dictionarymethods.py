# The repeated key in the first line is the point: the last value wins.

di1 = {"Albert": 2341, "Robert": 9102, "Albert": 3258}
print(di1["Albert"])  # Result : 3258

print(di1.keys())
print(di1.values())
print(di1.items())
print(di1.get("Robert"))  # 9102
print(di1.popitem())

for name, nr in di1.items():
    print(f"Key {name} with value {nr}")

if "Albert" in di1:
    print(f"Albert's value is {di1['Albert']}")

# di2 = {['Albert']: 2341, 'Robert': 9102}  # TypeError: cannot use 'list' as a dict key
# print(di2[['Albert']])

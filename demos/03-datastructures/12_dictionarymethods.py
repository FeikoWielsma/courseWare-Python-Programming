di1 = {"Albert": 2341, "Robert": 9102, "Albert": 3258}
print(di1["Albert"])  # Result : 3258

print(di1.keys())
print(di1.values())
print(di1.items())
print(di1.get("Robert"))  # 9102
print(di1.popitem())

for name, nr in di1.items():
    print(f"Key {name} with value {nr}")

if "Albert" in di1:  # OR di1.has_key('Name')
    print("Name's value is {}".format(di1["Albert"]))

# di2 = {['Albert']: 2341, 'Robert': 9102}     # TypeError: unhashable type: 'list'
# print(di2[['Albert']])

# The repeated key in the first line is the point: the last value wins.

di1 = {"Orbit": 222, "Echo": 185, "Orbit": 204}
print(di1["Orbit"])  # Result : 204

print(di1.keys())
print(di1.values())
print(di1.items())
print(di1.get("Echo"))  # 185
print(di1.popitem())

for name, nr in di1.items():
    print(f"Key {name} with value {nr}")

if "Orbit" in di1:
    print(f"Orbit's value is {di1['Orbit']}")

# di2 = {['Orbit']: 222, 'Echo': 185}  # TypeError: cannot use 'list' as a dict key
# print(di2[['Orbit']])

# The repeated key in the first line is the point: the last value wins.

di1 = {"Imagine": 183, "Yesterday": 125, "Imagine": 181}
print(di1["Imagine"])  # Result : 181

print(di1.keys())
print(di1.values())
print(di1.items())
print(di1.get("Yesterday"))  # 125
print(di1.popitem())

# di2 = {['Imagine']: 183, 'Yesterday': 125}  # TypeError: cannot use 'list' as a dict key
# print(di2[['Imagine']])

from functools import reduce

var1 = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(var1)  # 24

var2 = reduce((lambda x, y: x / y), [1, 2, 3, 4])
print(var2)  # 0.041666666666666664

li1 = [1, 2, 3, 4]
result = li1[0]
for x in li1[1:]:
    result = result * x

print(result)

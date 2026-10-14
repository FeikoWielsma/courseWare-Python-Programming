from functools import reduce

product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)  # 24

result = 1
for number in [1, 2, 3, 4]:
    result *= number
print(result)  # 24

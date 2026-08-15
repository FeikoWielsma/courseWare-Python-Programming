def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)


print(power(2, 3))
print(power(3, 2))
print(power(5, 1))
# print(power(3))

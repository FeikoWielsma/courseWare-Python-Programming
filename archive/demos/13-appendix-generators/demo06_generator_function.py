def countdown(n):
    while n > 0:
        yield n
        n -= 1


x = countdown(10)
print(x)  # <generator object countdown at 0x00D5B4E0>

# Counting down from 10
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

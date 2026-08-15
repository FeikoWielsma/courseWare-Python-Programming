from math import sqrt

# from math import *

n = int(input("Enter range:  "))

count = 1
while count < n:
    r = sqrt(count)
    print("square root of " + str(count) + "= ", end="")
    count = count + 1
    print(r)

# print(dir())

fibs = [0, 1]
num = input("How many Fibonacci numbers do you want? ")
for _ in range(num - 2):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)

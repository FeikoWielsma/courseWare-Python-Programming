slist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(slist)

new_list = []

for x in slist:
    if (x % 2) == 0:
        new_list.append(str(x))

print(new_list)
# ['2', '4', '6', '8', '10']

# Using list comprehension
new_list = [str(x) for x in slist if (x % 2) == 0]
print(new_list)
# ['2', '4', '6', '8', '10']

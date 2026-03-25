slist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(slist)

new_list = []
for x in slist:
    new_list.append(x * 2)
print(new_list)

# list comprehensions syntax
new_list2 = [x * 2 for x in slist]
print(new_list2)

list_str = [str(x) for x in slist]
print(list_str)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# could also use a map here
# list comprehension can be a bit more concise, e.g. when we want to use a predicate
new_list_str2 = list(map(str, slist))
print(new_list_str2)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

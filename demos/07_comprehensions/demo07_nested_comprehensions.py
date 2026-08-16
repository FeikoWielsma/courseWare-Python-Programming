li = [3, 2, 4, 1]
# inner comprehension produces: [4, 3, 5, 2]
[elem * 2 for elem in [item + 1 for item in li]]  # [8, 6, 10, 4]

list_a = ["A", "B"]
list_b = ["C", "D"]

list_c = [[x + y for x in list_a] for y in list_b]
print(list_c)

# [['AC', 'BC'], ['AD', 'BD']]

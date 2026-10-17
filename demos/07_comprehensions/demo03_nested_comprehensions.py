list_a = ["A", "B"]
list_b = ["C", "D"]
rows = [[x + y for x in list_a] for y in list_b]
print(rows)  # [['AC', 'BC'], ['AD', 'BD']]

words = ["one", "two"]
letters = [letter for word in words for letter in word]
print(letters)  # ['o', 'n', 'e', 't', 'w', 'o']

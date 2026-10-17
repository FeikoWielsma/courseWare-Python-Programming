numbers = [1, 2, 3, 4, 5, 6]
labels = []
for number in numbers:
    if number % 2 == 0:
        labels.append(str(number))
print(labels)  # ['2', '4', '6']

labels = [str(number) for number in numbers if number % 2 == 0]
print(labels)  # ['2', '4', '6']

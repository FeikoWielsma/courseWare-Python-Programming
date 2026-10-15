numbers = [1, 2, 2, 3, 4]
squares = {number**2 for number in numbers}
print(sorted(squares))  # [1, 4, 9, 16]
even_squares = {number**2 for number in numbers if number % 2 == 0}
print(sorted(even_squares))  # [4, 16]

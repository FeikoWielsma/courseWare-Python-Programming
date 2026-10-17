name = "Albert"
age = 55
print(f"My name is {name} and my age is {age}")
print(f"{name.upper()} will be {age + 1} next year")

print(f"{name!r}")  # 'Albert', the repr() with its quotes
print(f"{age = }")  # age = 55, the expression and its value

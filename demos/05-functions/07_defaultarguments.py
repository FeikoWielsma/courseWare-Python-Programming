def print_info(name: str, age: int = 35) -> None:
    """This prints name and age passed into this function"""
    print("Name:", name)
    print("Age:", age)


print_info(age=55, name="Albert")
print_info(name="Werner")

# When you use the * (asterisk) in front of a parameter when calling a function in Python,
# it unpacks a list or tuple into positional arguments.


def greet(name: str, age: int) -> None:
    print(f"Hello, {name}. You are {age} years old.")


args = ["Alice", 30]
greet(*args)  # same as greet("Alice", 30)

# It allows you to pass a sequence (like a list or tuple) into a
# function that expects separate arguments, without having to manually type each one.


# can also see ** used for keyword arguments:
def greet(name: str, age: int) -> None:
    print(f"Hello, {name}. You are {age} years old.")


kwargs = {"name": "Alice", "age": 30}
greet(**kwargs)  # same as greet(name="Alice", age=30)

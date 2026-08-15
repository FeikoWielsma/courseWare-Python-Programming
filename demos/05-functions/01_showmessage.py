def show_message(message: str) -> None:
    """This prints a passed parameter into this function"""
    print(message)


show_message("First call to user defined function!")
show_message("Again second call to the same function")
show_message(100)
# show_message()  # TypeError: missing 1 required positional argument: 'message'

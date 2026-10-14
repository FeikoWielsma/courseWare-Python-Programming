def hello_solar_system(old_function):
    def wrapper_function():
        print("Hello Solar System")
        old_function()

    return wrapper_function


def hello_galaxy(old_function):
    def wrapper_function():
        print("Hello Galaxy")
        old_function()

    return wrapper_function


@hello_galaxy
@hello_solar_system
def hello():
    print("Hello World")


hello()

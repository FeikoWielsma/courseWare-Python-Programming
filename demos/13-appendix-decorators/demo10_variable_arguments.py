def hello_solar_system(original_function):
    def new_function(*args, **kwargs):
        original_function(*args, **kwargs)
        print("Hello, solar system!")

    return new_function


def hello_galaxy(original_function):
    def new_function(*args, **kwargs):
        original_function(*args, **kwargs)
        print("Hello, galaxy!")

    return new_function


@hello_galaxy
@hello_solar_system
def hello(planet=None):
    if planet:
        print("Hello " + planet)
    else:
        print("Hello World")


@hello_galaxy
@hello_solar_system
def goodbye(planets, moons, species):
    print(planets)
    print(moons)
    print(species)


hello("Earth")
goodbye("planets", "moons", "species")

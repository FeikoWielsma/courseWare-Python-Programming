def helloSolarSystem(original_function):
    def new_function(*args, **kwargs):
        original_function(*args, **kwargs)
        print("Hello, solar system!")
    return new_function

def helloGalaxy(original_function):
    def new_function(*args, **kwargs):
        original_function(*args, **kwargs)
        print("Hello, galaxy!")
    return new_function

@helloGalaxy
@helloSolarSystem
def hello(planet=None):
    if planet:
        print ("Hello "+planet)
    else:
        print ("Hello World")

@helloGalaxy
@helloSolarSystem
def goodbye(planets, moons, species):
    print (planets)
    print (moons)
    print (species)

hello("Earth")
goodbye("planets", "moons", "species")

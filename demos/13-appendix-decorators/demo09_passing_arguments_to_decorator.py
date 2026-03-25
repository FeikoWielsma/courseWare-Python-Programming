def helloSolarSystem(old_function):
    def wrapper_function(planet=None):
        print ("Hello Solar System")
        old_function(planet)
        print ("Leaving Solar System")
    return wrapper_function

@helloSolarSystem
def hello(planet=None):
    if planet:
        print ("Hello "+planet)
    else:
        print ("Hello World")

hello("Mars")
hello()

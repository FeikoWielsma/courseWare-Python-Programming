def helloSolarSystem(old_function):
    def wrapper_function():
        print ("Hello Solar System")
        old_function()
    return wrapper_function

def helloGalaxy(old_function):
    def wrapper_function():
        print ("Hello Galaxy")
        old_function()
    return wrapper_function

@helloGalaxy
@helloSolarSystem
def hello():
    print ("Hello World")

hello()
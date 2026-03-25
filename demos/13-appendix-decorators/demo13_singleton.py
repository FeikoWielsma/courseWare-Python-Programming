instances = {}  # dictionary to hold class and their only instance


def get_instance(klass, *args):  # this function is used by decorator
    if klass not in instances:
        instances[klass] = klass(*args)
    return instances[klass]


def singleton(klass):  # decorator function
    def on_call(*args):
        return get_instance(klass, *args)

    return on_call


@singleton
class Star:
    def __init__(self, name):
        self.name = name


# A solar system should have only one star
sun = Star("Sun")
print(sun.name)
taurus = Star("Taurus")
print(taurus.name)

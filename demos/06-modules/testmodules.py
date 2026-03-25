version = "0.1"


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def show(self):
        print("Person -- firstname: %s  lastname: %s" % (self.firstname, self.lastname))


def sayhi():
    print("Hi, this is testmodules speaking.")

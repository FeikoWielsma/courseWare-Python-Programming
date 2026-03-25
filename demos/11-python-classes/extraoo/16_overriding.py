class Parent:  # define parent class
    def my_method(self):
        print("Calling parent method")


class Child(Parent):  # define child class
    def my_method(self):
        print("Calling child method")


c = Child()  # instance of child
c.my_method()  # child calls overridden method

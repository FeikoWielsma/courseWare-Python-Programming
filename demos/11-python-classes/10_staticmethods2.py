# Filename: objvariables.py


class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print(f"(Initializing {self.name})")

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def __del__(self):
        """I am dying."""
        print(f"{self.name} is being destroyed!")

        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population:d} robots working.")

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print(f"Greetings, my masters call me {self.name}.")

    def how_many():
        """Prints the current population."""
        print(f"We have {Robot.population:d} robots.")

    how_many = staticmethod(how_many)


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()
# droid1.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\n_robots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
del droid1
del droid2

Robot.how_many()

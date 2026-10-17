class SchoolMember:
    """Represents any school member."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"(Initialized SchoolMember: {self.name})")

    def tell(self):
        """Tell my details."""
        print(f'Name:"{self.name}" Age:"{self.age}"')


class Teacher(SchoolMember):
    """Represents a teacher."""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"(Initialized Teacher: {self.name})")

    def tell(self):
        SchoolMember.tell(self)
        print(f'Salary: "{self.salary:d}"')


class Student(SchoolMember):
    """Represents a student."""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f"(Initialized Student: {self.name})")

    def tell(self):
        SchoolMember.tell(self)
        print(f'Marks: "{self.marks:d}"')


t = Teacher("Mrs. Shrividya", 40, 30000)
s = Student("Swaroop", 25, 75)

print()  # prints a blank line

members = [t, s]
for member in members:
    member.tell()  # works for both Teachers and Students


class A:
    def show(self, msg):
        print(f'class A -- msg: "{msg}"')


class B:
    def show(self, msg):
        print(f'class B -- msg: "{msg}"')


class C:
    def show(self, msg):
        print(f'class C -- msg: "{msg}"')


def test():
    objs = [
        A(),
        B(),
        C(),
        A(),
    ]
    for idx, obj in enumerate(objs):
        msg = f"message # {idx + 1}"
        obj.show(msg)


if __name__ == "__main__":
    test()

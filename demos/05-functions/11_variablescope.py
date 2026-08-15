x = 50  # This is a global variable
y = 50  # This is a global variable


def func1() -> None:
    x = 2
    print("Changed local x to", x)


def func2() -> None:
    print("Access global x as", x)


def func3() -> None:
    global y
    y = 2
    print("Changed global y to", y)


func1()  # prints 2
print("x is still", x)  # prints 50

func2()  # prints 50
print("x is still", x)  # prints 50

func3()  # prints 2
print("Value of y is", y)  # prints 2

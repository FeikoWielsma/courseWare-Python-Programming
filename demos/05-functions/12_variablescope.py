x = 50
y = 50


def func1() -> None:
    x = 2
    print("Local x   :", x)


def func2() -> None:
    global y
    y = 2


func1()
print("x is still:", x)
func2()
print("y is now  :", y)

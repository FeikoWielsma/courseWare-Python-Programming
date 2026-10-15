def divide(total: int, count: int) -> float:
    try:
        return total / count
    finally:
        print("This always runs")


try:
    divide(10, 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

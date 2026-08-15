import traceback


def exception_do_not_catch():
    try:
        print("In exception_do_not_catch")
        i = 10
        j = 0
        z = i / j
        print(z)
    finally:
        print("Finally executed in exception_do_not_catch")
    print("Will never reach this point")


print("\n_calling exception_do_not_catch")

try:
    exception_do_not_catch()
except Exception as e:
    print("Caught exception from exception_do_not_catch in main program.")
    print(e.args)
    traceback.print_exc()

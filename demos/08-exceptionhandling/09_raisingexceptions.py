try:
    raise NameError("HiThere")
except NameError:
    print("An exception flew by!")
    raise  # re-raise it for a caller to handle

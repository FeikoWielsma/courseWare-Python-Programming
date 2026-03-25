while True:
    try:
        x = int(input("Please enter a number: "))
        # x = int(input("Please enter a number: "), 16)    # input is "A"
        # x = int(input("Please enter a number: "), 2)     # input is 1010
        # x = int(input("Please enter a number: "), 8)       # input is 12
    except Exception as x:
        print(x)
    else:
        print(str(x) + " is a really good number")

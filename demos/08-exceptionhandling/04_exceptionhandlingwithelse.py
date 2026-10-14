while True:
    try:
        x = int(input("Please enter a number: "))
        # x = int(input("Please enter a number: "), 16)  # input is "A"
        # x = int(input("Please enter a number: "), 2)   # input is 1010
        # x = int(input("Please enter a number: "), 8)   # input is 12
    except ValueError as e:
        print("Oops! That was not valid number:", e)
    else:
        print(f"Yeah! {x} was a really good number")

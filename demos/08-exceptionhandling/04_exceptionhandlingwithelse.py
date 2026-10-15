try:
    x = int(input("Please enter a number: "))
except ValueError:
    print("Oops! That was not a valid number")
else:
    print(f"Yeah! {x} was a really good number")

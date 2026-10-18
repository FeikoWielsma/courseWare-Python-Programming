try:
    seconds = int("three")
except ValueError:
    print("Track length must be a whole number")
except Exception as error:
    print(f"Other problem: {error}")
else:
    print(f"Track length: {seconds}")

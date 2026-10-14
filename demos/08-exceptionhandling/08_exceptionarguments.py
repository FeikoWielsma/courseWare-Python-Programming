# Define a function here.
def temp_convert(var):
    try:
        return int(var)
    except ValueError as e:
        print("Argument does not contain numbers:", e)


# Call above function here.
temp_convert("xyz")

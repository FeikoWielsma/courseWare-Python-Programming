def temp_convert(value: str) -> None:
    try:
        print(int(value))
    except ValueError as error:
        print("Argument does not contain numbers:", error)


temp_convert("xyz")

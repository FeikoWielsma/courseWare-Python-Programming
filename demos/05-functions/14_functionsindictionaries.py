def to_celsius(value: float) -> float:
    return (value - 32) * 5 / 9


def to_fahrenheit(value: float) -> float:
    return value * 9 / 5 + 32


converters = {
    "C": to_celsius,
    "F": to_fahrenheit,
    "K": lambda value: value + 273.15,
}

unit = "C"
print(converters[unit](212))  # look up the function, then call it

for unit, convert in converters.items():
    print(unit, convert(100))

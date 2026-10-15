def kelvin_to_fahrenheit(temperature: float) -> float:
    assert temperature >= 0, "Colder than absolute zero!"
    return (temperature - 273.15) * 1.8 + 32


print(f"{kelvin_to_fahrenheit(273.15):.1f}")  # 32.0
print(kelvin_to_fahrenheit(-5))  # Deliberate AssertionError.

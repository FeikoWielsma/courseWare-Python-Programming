def kelvin_to_fahrenheit(temperature):
    assert temperature >= 0, "Colder than absolute zero!"
    return ((temperature - 273) * 1.8) + 32


print(kelvin_to_fahrenheit(273))
print(int(kelvin_to_fahrenheit(505.78)))
print(kelvin_to_fahrenheit(-5))

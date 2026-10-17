stock = {"tea": 12, "coffee": 0, "cocoa": 5}
available = {name: count for name, count in stock.items() if count > 0}
print(available)  # {'tea': 12, 'cocoa': 5}
prices = {"tea": 2.0, "coffee": 4.0}
with_tax = {name: round(price * 1.21, 2) for name, price in prices.items()}
print(with_tax)  # {'tea': 2.42, 'coffee': 4.84}

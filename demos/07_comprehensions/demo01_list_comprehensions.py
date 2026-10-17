filenames: list[str] = ["sales", "stock", "prices"]
csv_files = []
for name in filenames:
    csv_files.append(f"{name}.csv")
print(csv_files)  # ['sales.csv', 'stock.csv', 'prices.csv']

csv_files = [f"{name}.csv" for name in filenames]
print(csv_files)  # ['sales.csv', 'stock.csv', 'prices.csv']

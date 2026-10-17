names = [" Sales ", "Stock", "sales", "Prices "]
unique = {name.strip().lower() for name in names}
print(sorted(unique))  # ['prices', 'sales', 'stock']

csv_files = ["sales.csv", "notes.txt", "sales.csv", "stock.csv"]
unique_csv = {name for name in csv_files if name.endswith(".csv")}
print(sorted(unique_csv))  # ['sales.csv', 'stock.csv']

filenames = ["sales.csv", "notes.txt", "stock.csv"]
csv_files = []
for name in filenames:
    if name.endswith(".csv"):
        csv_files.append(name)
print(csv_files)  # ['sales.csv', 'stock.csv']

csv_files = [name for name in filenames if name.endswith(".csv")]
print(csv_files)  # ['sales.csv', 'stock.csv']

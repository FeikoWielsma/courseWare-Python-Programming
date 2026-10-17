readings = [[18.2, 19.6], [20.1, 21.8]]
rounded = [[round(value) for value in row] for row in readings]
print(rounded)  # [[18, 20], [20, 22]]

flat = []
for row in readings:
    for value in row:
        flat.append(value)
print(flat)  # [18.2, 19.6, 20.1, 21.8]

flat = [value for row in readings for value in row]
print(flat)  # [18.2, 19.6, 20.1, 21.8]

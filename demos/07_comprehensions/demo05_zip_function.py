titles = ["Orbit", "Echo", "Pulse"]
lengths = [222, 185, 204]
pairs = list(zip(titles, lengths))
print(pairs)
checked = list(zip(titles, lengths, strict=True))
print(checked)

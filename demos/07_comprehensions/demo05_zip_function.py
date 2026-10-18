titles = ["Imagine", "Yesterday", "Respect"]
lengths = [183, 125, 149]
pairs = list(zip(titles, lengths))
print(pairs)
checked = list(zip(titles, lengths, strict=True))
print(checked)

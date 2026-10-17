counts = dict.fromkeys(["a", "b", "c"], 0)
print(counts)  # {'a': 0, 'b': 0, 'c': 0}
groups: dict[str, list[int]] = {key: [] for key in ["a", "b", "c"]}
groups["a"].append(1)
print(groups)  # {'a': [1], 'b': [], 'c': []}

from functools import reduce

lengths = [183, 125, 149]
total = reduce(lambda running, seconds: running + seconds, lengths)
print(total)  # 457
print(sum(lengths))  # 457

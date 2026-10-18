from functools import reduce

lengths = [222, 185, 204]
total = reduce(lambda running, seconds: running + seconds, lengths)
print(total)  # 611
print(sum(lengths))  # 611

sizes_mb = [12, 8, 25]
print(sum(size for size in sizes_mb if size >= 10))  # 37
print(any(size > 20 for size in sizes_mb))  # True
print(all(size <= 20 for size in sizes_mb))  # False
print(any([]), all([]))  # False True

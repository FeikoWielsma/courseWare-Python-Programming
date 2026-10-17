sizes_mb = [120, 80, 250]
print(sum(size for size in sizes_mb if size >= 100))  # 370
print(any(size > 200 for size in sizes_mb))  # True
print(all(size <= 200 for size in sizes_mb))  # False
print(any([]), all([]))  # False True

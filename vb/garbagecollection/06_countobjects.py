import gc

print(gc.get_count())
gc.collect()
print(gc.get_count())
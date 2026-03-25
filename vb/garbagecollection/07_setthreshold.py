import gc

print(gc.get_threshold())
gc.set_threshold(1000, 15, 15)
print(gc.get_threshold())

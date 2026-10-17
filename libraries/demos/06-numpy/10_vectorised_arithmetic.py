import numpy as np

traffic = np.array([1_200, 3_400, 900, 15_800, 7_650])
limits = np.array([2_000, 2_000, 2_000, 10_000, 10_000])

print(traffic > limits)

# # An array and a single number : the number applies to every element.
# print(np.round(traffic / 1024, 2))
# print(traffic * 2)

# # Two arrays of the same shape : element against matching element.
# print(limits - traffic)
# print(np.round(traffic / limits, 2))

# # The named functions work the same way, over the whole array at once.
# print(np.round(np.sqrt(traffic), 1))
# print(np.round(np.log10(traffic), 2))

# # A comparison is arithmetic too, and gives an array of True and False.
# print(traffic > limits)

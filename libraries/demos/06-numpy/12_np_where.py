import numpy as np

disk = np.array([41, 88, 96, 12, 73, 91, 55])
print(disk)
new_disk = []
for i in disk:
    if i > 90:
        new_disk.append(0)
    else:
        new_disk.append(90 - i)
# where(condition, value_if_true, value_if_false), evaluated per element.
print(np.where(disk > 90, 0, 90 - disk))

# # Either branch can be an array or a single value, in any combination.
# print(np.where(disk > 90, "FULL", "ok"))

# # Nesting gives more than two outcomes. Three is about the readable limit.
# print(np.where(disk > 90, "critical", np.where(disk > 70, "warning", "fine")))

# # With one argument it answers "where?" rather than "which value?".
# print(np.where(disk > 90)[0])

# print(np.clip(disk, 0, 90))

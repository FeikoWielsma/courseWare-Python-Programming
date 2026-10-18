"""Three ways to walk a sequence, from least to most Pythonic."""

playlist = ["Imagine", "Yesterday", "Respect"]

# range(len(...)) works, and is what someone arriving from C or Java writes.
# It is worth seeing once, so that you recognise it.
print(len(playlist))
print(range(len(playlist)))
print(type(range(len(playlist))))

for index in range(len(playlist)):
    print("By index          :", playlist[index])

# When the index is not needed, iterate the sequence itself.
for title in playlist:
    print("Directly          :", title)

# When the index *is* needed, enumerate gives both, and cannot fall out of step
# with the sequence the way a separate counter can.
for index, title in enumerate(playlist):
    print(f"With enumerate    : {index} {title}")

# enumerate counts from zero unless told otherwise.
for number, title in enumerate(playlist, start=1):
    print(f"Numbered from one : {number} {title}")

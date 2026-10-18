queue = ["Imagine", "Yesterday", "Yesterday", "Thriller", "Respect"]
print(queue.count("Yesterday"))  # 2
queue.insert(0, "Warm-up")
queue.append("Let It Be")
print(queue)
print(queue.index("Respect"))  # 5
queue.remove("Yesterday")  # Only the first matching item is removed.
print(queue)
queue.reverse()
print(queue)
queue.sort()
print(queue)

queue = ["Orbit", "Echo", "Echo", "Intro", "Pulse"]
print(queue.count("Echo"))  # 2
queue.insert(0, "Warm-up")
queue.append("Encore")
print(queue)
print(queue.index("Pulse"))  # 5
queue.remove("Echo")  # Only the first matching item is removed.
print(queue)
queue.reverse()
print(queue)
queue.sort()
print(queue)

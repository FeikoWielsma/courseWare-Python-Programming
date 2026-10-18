history = ["Library", "Album", "Track"]
history.append("Queue")
history.append("Artist")
print(history)  # ['Library', 'Album', 'Track', 'Queue', 'Artist']
print(history.pop())  # Artist
print(history)  # ['Library', 'Album', 'Track', 'Queue']
history.pop()  # Queue
history.pop()  # Track
print(history)  # ['Library', 'Album']

titles = ["Bohemian Rhapsody", "Yesterday", "Imagine"]
print(sorted(titles))  # ['Bohemian Rhapsody', 'Imagine', 'Yesterday']
print(sorted(titles, key=len))  # ['Imagine', 'Yesterday', 'Bohemian Rhapsody']
print(min(titles, key=len), max(titles, key=len))  # Imagine Bohemian Rhapsody

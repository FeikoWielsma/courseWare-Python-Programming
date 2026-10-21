titles = [" Imagine ", "Yesterday", "imagine", "Respect "]
unique = {title.strip().lower() for title in titles}
print(sorted(unique))  # ['imagine', 'respect', 'yesterday']

files = ["cover.jpg", "notes.txt", "cover.jpg", "stage.jpg"]
unique_photos = {name for name in files if name.endswith(".jpg")}
print(sorted(unique_photos))  # ['cover.jpg', 'stage.jpg']

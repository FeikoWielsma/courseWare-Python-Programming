titles = [" Orbit ", "Echo", "orbit", "Pulse "]
unique = {title.strip().lower() for title in titles}
print(sorted(unique))  # ['echo', 'orbit', 'pulse']

files = ["cover.jpg", "notes.txt", "cover.jpg", "stage.jpg"]
unique_photos = {name for name in files if name.endswith(".jpg")}
print(sorted(unique_photos))  # ['cover.jpg', 'stage.jpg']

filenames = ["cover.jpg", "notes.txt", "stage.jpg"]
photo_files = []
for name in filenames:
    if name.endswith(".jpg"):
        photo_files.append(name)
print(photo_files)  # ['cover.jpg', 'stage.jpg']

photo_files = [name for name in filenames if name.endswith(".jpg")]
print(photo_files)  # ['cover.jpg', 'stage.jpg']

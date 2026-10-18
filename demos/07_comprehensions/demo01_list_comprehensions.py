filenames: list[str] = ["cover", "stage", "crowd"]
photo_files = []
for name in filenames:
    photo_files.append(f"{name}.jpg")
print(photo_files)  # ['cover.jpg', 'stage.jpg', 'crowd.jpg']

photo_files = [f"{name}.jpg" for name in filenames]
print(photo_files)  # ['cover.jpg', 'stage.jpg', 'crowd.jpg']

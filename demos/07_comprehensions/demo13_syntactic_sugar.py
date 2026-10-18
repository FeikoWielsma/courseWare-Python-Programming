files = ["COVER.JPG", "STAGE.JPG"]
mapped = list(map(lambda name: name.lower(), files))
print(mapped)  # ['cover.jpg', 'stage.jpg']
comprehended = [name.lower() for name in files]
print(comprehended)  # ['cover.jpg', 'stage.jpg']

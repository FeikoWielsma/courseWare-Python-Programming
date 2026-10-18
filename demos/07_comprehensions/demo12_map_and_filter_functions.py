def clean_filename(name: str) -> str:
    return name.strip().lower()


def is_photo(name: str) -> bool:
    return name.endswith(".jpg")


files = ["  COVER.JPG ", "STAGE.JPG", "NOTES.TXT"]
cleaned = list(map(clean_filename, files))
photos = list(filter(is_photo, cleaned))
print(photos)  # ['cover.jpg', 'stage.jpg']
print([name for name in cleaned if is_photo(name)])

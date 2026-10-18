filename = "  IMG_0421.JPG  "
clean = filename.strip().lower()
print(repr(clean))  # 'img_0421.jpg'
print(clean.upper())  # IMG_0421.JPG
print(clean.endswith(".jpg"))  # True
print(clean.startswith("img_"))  # True
print(clean.replace(".jpg", "_edit.jpg"))  # img_0421_edit.jpg
print(clean.find("0421"))  # 4
print(clean.find("holiday"))  # -1
print(clean.count("_"))  # 1
print(len(clean))  # 12
print("Imagine".isalpha())  # True
print("Beyoncé".isascii())  # False

playlist_text = "Imagine, Yesterday, Respect"
titles = playlist_text.split(", ")
print(titles)  # ['Imagine', 'Yesterday', 'Respect']
print(" / ".join(titles))  # Imagine / Yesterday / Respect
print("Imagine\nYesterday".splitlines())  # ['Imagine', 'Yesterday']

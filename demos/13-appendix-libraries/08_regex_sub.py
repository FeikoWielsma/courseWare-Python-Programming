import re

text = "IMG_0421.JPG; IMG_0422.JPG"
print(re.sub(r"IMG_\d{4}\.JPG", "[photo]", text))
print(re.sub(r"IMG_(\d{4})\.JPG", r"photo_\1.jpg", text))
print(re.split(r";\s*", text))

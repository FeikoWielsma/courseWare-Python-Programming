import re

text = "Playing Imagine (183s), Yesterday (125s)"
print(re.match(r"Playing", text) is not None)  # True
print(re.match(r"Yesterday", text) is not None)  # False
print(re.search(r"Yesterday", text) is not None)  # True
print(re.findall(r"\d+", text))  # ['183', '125']
print(re.fullmatch(r"IMG_\d{4}\.jpg", "IMG_0421.jpg") is not None)  # True
print(re.fullmatch(r"IMG_\d{4}\.jpg", "notes.txt") is not None)  # False

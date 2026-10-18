import re

text = "Playing Orbit (222s), Echo (185s)"
print(re.match(r"Playing", text) is not None)  # True
print(re.match(r"Echo", text) is not None)  # False
print(re.search(r"Echo", text) is not None)  # True
print(re.findall(r"\d+", text))  # ['222', '185']
print(re.fullmatch(r"IMG_\d{4}\.jpg", "IMG_0421.jpg") is not None)  # True
print(re.fullmatch(r"IMG_\d{4}\.jpg", "notes.txt") is not None)  # False

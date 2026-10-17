import json

book = {}
book["title"] = "Light Science:  Introduction to Photographic Lighting"
book["tags"] = ("Photography", "Kindle", "Light")
book["published"] = True
book["comment_link"] = None
book["id"] = 1024
with open("ebook.json", "w") as f:
    json.dump(book, f)
# with open('ebook.json', 'w') as f:
#    json.dump(book, f, indent= 3)

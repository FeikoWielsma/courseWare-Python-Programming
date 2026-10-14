import json
import codecs

with codecs.open("ebook.json", "r", encoding="utf-8") as f:
    data_from_json = json.load(f)

print(type(data_from_json))
print(data_from_json)

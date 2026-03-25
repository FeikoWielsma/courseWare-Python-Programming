import json

json_string = '{"first_name": "Albert", "last_name":"Einstein"}'
parsed_json = json.loads(json_string)

print(parsed_json["first_name"])  # Albert
print(parsed_json["last_name"])  # Einstein

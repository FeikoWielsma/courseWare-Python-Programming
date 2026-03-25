import json
from unittest.mock import Mock
mock = Mock()
print(mock)

# Patch the json library
json = mock
print(json)
json2 = json.dump_methods()
print(json2)
print(json2.dump_methods())

mock = mock.some_attribute
print(mock)

mock = mock.do_something()
print(mock)

json3 = Mock()
json3.loads('{"k": "v"}').get('k')

print(json3)
print(json3.loads)
print(json3.loads.get)

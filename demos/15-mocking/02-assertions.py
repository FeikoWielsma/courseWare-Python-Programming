from unittest.mock import Mock

# Create a mock object
json = Mock()

print(json.loads('{"key": "value"}'))  # <Mock name='mock.loads()' id='4550144184'>

print(json.loads.assert_called())
print(json.loads.assert_called_once())
print(json.loads.assert_called_with('{"key": "value"}'))
print(json.loads.assert_called_once_with('{"key": "value"}'))

print(json.loads('{"key": "value"}'))
# print(json.loads.assert_called_once())
# print(json.loads.assert_called_once_with('{"key": "value"}'))
# print(json.loads.assert_not_called())

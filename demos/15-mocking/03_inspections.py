from unittest.mock import Mock

json = Mock()
json.loads(s='{"key": "value"}')
json.loads.assert_called_with('{"key": "value"}')

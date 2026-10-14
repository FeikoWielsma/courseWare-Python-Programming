from unittest.mock import Mock

# Create a mock object
json = Mock()
print(json.loads('{"key": "value"}'))
# <Mock name='mock.loads()' id='4391026640'>

# Number of times you called loads():
print(json.loads.call_count)
1
# The last loads() call:
print(json.loads.call_args)
# call('{"key": "value"}')

# List of loads() calls:
print(json.loads.call_args_list)
# [call('{"key": "value"}')]

# List of calls to json's methods (recursively):
print(json.method_calls)
# [call.loads('{"key": "value"}')]

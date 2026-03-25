import sys

a = 'my-string'
# b = [a] # Make a list with a as an element.
# c = { 'key': a } # Create a dictionary with a as one of the values.
print(sys.getrefcount(a))
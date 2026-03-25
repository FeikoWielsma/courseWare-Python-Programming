import re

# Regular expressions are compiled into pattern objects, which 
# have methods for various operations such as searching for pattern 
# matches or performing string substitutions.

p1 = re.compile('ab*')
print (p1)

p2 = re.compile('ab*', re.IGNORECASE)
print (p2)
import testmodules

print(testmodules.version)
testmodules.sayhi()
p = testmodules.Person("Albert", "Einstein")
print(p)

from testmodules import *

print(version)
sayhi()
p = Person("Werner", "Heisenberg")
print(p)

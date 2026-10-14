print("My name is %s and weight is %d kg!" % ("Albert", 55))

i = 111
print("Integer %d Hexadecimal %x exponential %e floating point %.3f" % (i, i, i, i))

s = "{0}, {1}, {2}".format("a", "b", "c")
print(s)  # 'a, b, c'
s = "{}, {}, {}".format("a", "b", "c")
print(s)  # 'a, b, c'
s = "{2}, {1}, {0}".format("a", "b", "c")
print(s)  # 'c, b, a'

print("{2}, {1}, {0}".format(*"abc"))  # unpacking argument sequence : 'c, b, a'

# arguments' indices can be repeated : 'abracadabra'
print("{0}{1}{0}".format("abra", "cad"))

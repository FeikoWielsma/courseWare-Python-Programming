t = ("Albert", "Einstein")
print(t)  # ('Albert', 'Einstein')

v, s = t

print(v)  # 'Albert'
print(s)  # 'Einstein'

v, s = s, v

print(v)  # 'Einstein'
print(s)  # 'Albert'

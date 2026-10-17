t = ("Albert", "Einstein")
print(t)  # ('Albert', 'Einstein')

v, s = t

print(v)  # 'Albert'
print(s)  # 'Einstein'

v, s = s, v

print(v)  # 'Einstein'
print(s)  # 'Albert'

rows = [(1,), (2,)]
for (number,) in rows:
    print(number)  # 1, then 2

records = [(1, ("Albert", "Einstein"))]
for number, (first, last) in records:
    print(number, first, last)  # 1 Albert Einstein

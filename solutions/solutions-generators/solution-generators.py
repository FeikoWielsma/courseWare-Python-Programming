def firstN(iterator, n):
  for i in range(n):
    yield iterator[i]

def intsfrom(i):
    while 1:
        yield i
        i = i + 1

def fibgen(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

it = [11,22,33,44,55]
print(list(firstN(it, 4)))

fi = firstN(it,3)
for x in fi:
    print(x)

#inf = intsfrom(10)
#for i in inf:
#    print(i)
    
fibo = fibgen(100)
print(list(fibo))
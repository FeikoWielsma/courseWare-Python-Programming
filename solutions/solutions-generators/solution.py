
def firstn(g, n):

    for i in range(n):
        yield next(g)


def intsfrom(i):
    while 1:
        yield i
        i = i + 1


def exclude_multiples(n, ints):
    #name = "Excluding multiples of {}".format(n)
    for i in ints:

        if (i % n): yield i
        #print(1)


def sieve(ints):
    while 1:
        prime = next(ints)
        yield prime
        ints = exclude_multiples(prime, ints)


def prime(l, n):
    for i in l:
        if not n % i:
            return False
    return True

def sieve2(ints):
    primes = [2]
    for i in ints:
        if prime(primes, i):
            yield i
            primes.append(i)

# def sieve2(ints):
#     while 1:
#         prime = next(exclude_multiples2(ints))
#         yield prime


def fibgen(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

if __name__ == '__main__':

    # print([f for f in fibgen(200)])
    for i in sieve2(intsfrom(2)):
        print(i)

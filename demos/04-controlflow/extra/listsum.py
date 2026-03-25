def list_sum(values):
    sum = 0
    for value in values:
        sum += value
    return sum

def test():
    a = [11, 22, 33, 44, ]
    print list_sum(a)

if __name__ == '__main__':
    test()


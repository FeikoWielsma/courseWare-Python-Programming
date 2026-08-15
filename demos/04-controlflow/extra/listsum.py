def list_sum(values):
    total = 0
    for value in values:
        total += value
    return total


def test():
    a = [11, 22, 33, 44]
    print(list_sum(a))


if __name__ == '__main__':
    test()

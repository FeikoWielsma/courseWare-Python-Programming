def test():
    numbers = [11, 22, 33, 0, 44, 55, 66]
    print(f'numbers: {numbers}')
    total = 0
    for item in numbers:
        if item == 0:
            break
        total += item
    print(f'sum: {total}')


test()

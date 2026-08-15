def test():
    numbers = [11, 22, 33, 44, 55, 66]
    print(f'before: {numbers}')
    for idx, item in enumerate(numbers):
        if item % 2 != 0:
            continue
        numbers[idx] *= 3
    print(f'after: {numbers}')


test()

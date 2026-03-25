def test():
    numbers = [11, 22, 33, 0, 44, 55, 66, ]
    print 'numbers: %s' % (numbers, )
    sum = 0
    for item in numbers:
        if item == 0:
            break
        sum += item
    print 'sum: %d' % (sum, )
    
test()

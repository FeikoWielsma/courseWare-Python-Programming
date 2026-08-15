def fibs(num):
    result = [0, 1]
    for _ in range(num - 2):
        result.append(result[-2] + result[-1])
    return result

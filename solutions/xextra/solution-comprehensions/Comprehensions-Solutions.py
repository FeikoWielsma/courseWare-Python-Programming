# List comprehension 1

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number % 2 == 0]
print (b)

# List comprehension 2

li1 = [i for i in range(1,101) if int(i**0.5)==i**0.5]
print (li1)

def eg1_for(matrix):
    flat = []
    for row in matrix:
        for x in row:
            flat.append(x)
    return flat

def eg1_lc(matrix):
    return [x for row in matrix for x in row ]

matrix = [ range(0,5), range(5,10), range(10,15) ]
print ("Original Matrix: " + str(matrix))
print ("FOR-loop result: " + str(eg1_for(matrix)))
print ("LC result      : " + str(eg1_lc(matrix)))

def eg3_for(keys, values):
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = values[i]
    return dic

def eg3_lc(keys, values):
    return { keys[i] : values[i] for i in range(len(keys)) }

country = ['Germany', 'France', 'Belgium', 'England', 'Spain', 'Italy']
capital = ['Berlin', 'Paris','Brussels', 'London', 'Madrid', 'Rome']
print ("FOR-loop result: " + str(eg3_for(country, capital)))
print ("LC result      : " + str(eg3_lc(country, capital)))


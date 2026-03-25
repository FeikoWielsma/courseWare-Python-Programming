fr = open('calculationdata.txt', mode='r', encoding='UTF-8')

for line in fr.readlines():
    s = line.rstrip('\n')
    slist = s.split(',')
    print (slist)
fr.close()
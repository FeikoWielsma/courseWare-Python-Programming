fr = open('calculationdata.txt', encoding='UTF-8')

for line in fr:
    s = line.rstrip('\n')
    slist = s.split(',')
    print (slist)
fr.close()

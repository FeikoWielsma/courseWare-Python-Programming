with open('calculationdata.txt', encoding='UTF-8') as fr:
    for line in fr:
        s = line.rstrip('\n')
        slist = s.split(',')
        print(slist)

def test():
    infilename = "nothing_noplace.txt"
    try:
        infile = open(infilename, "r")
        for line in infile:
            print(line)
    except IOError:
        print(f'cannot open file "{infilename}"')


test()

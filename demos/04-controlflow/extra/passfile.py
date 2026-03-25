import sys


def writer(outfile, msg="\n"):
    outfile.write(msg)


def test():
    writer(sys.stdout, "aaaaa\n")
    writer(sys.stdout)
    writer(sys.stdout, "bbbbb\n")


test()

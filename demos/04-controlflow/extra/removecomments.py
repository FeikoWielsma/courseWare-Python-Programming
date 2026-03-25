import sys


def filter(infile, outfile, filterfunc):
    for line in infile:
        line = filterfunc(line)
        outfile.write(line)


def add_comment(line):
    line = "## %s" % (line,)
    return line


def remove_comment(line):
    if line.startswith("## "):
        line = line[3:]
    return line


def main():
    filter(sys.stdin, sys.stdout, add_comment)


if __name__ == "__main__":
    main()

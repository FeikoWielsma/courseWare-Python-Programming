import sys


def apply_filter(infile, outfile, filterfunc):
    for line in infile:
        outfile.write(filterfunc(line))


def add_comment(line):
    line = f"## {line}"
    return line


def remove_comment(line):
    line = line.removeprefix("## ")
    return line


def main():
    apply_filter(sys.stdin, sys.stdout, add_comment)


if __name__ == "__main__":
    main()

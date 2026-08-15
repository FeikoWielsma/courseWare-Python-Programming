NO_COLOR, RED, GREEN, BLUE = range(4)


def test(color):
    if color == RED:
        print("It's red.")
    elif color == GREEN:
        print("It's green.")
    elif color == BLUE:
        print("It's blue.")


def main():
    color = BLUE
    test(color)


if __name__ == '__main__':
    main()

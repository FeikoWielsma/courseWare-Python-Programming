def fancy(obj):
    print(f'fancy fancy -- {obj} -- fancy fancy')


def plain(obj):
    print(f'plain -- {obj} -- plain')


def show(func, obj):
    func(obj)


def main():
    a = {'aa': 11, 'bb': 22}
    show(fancy, a)
    show(plain, a)


if __name__ == '__main__':
    main()

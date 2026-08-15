def show_args(x, y=-1, *args, **kwargs):
    print('-' * 40)
    print('x:', x)
    print('y:', y)
    print('args:', args)
    print('kwargs:', kwargs)


def test():
    show_args(1)
    show_args(x=2, y=3)
    show_args(y=5, x=4)
    show_args(4, 5, 6, 7, 8)
    show_args(11, y=44, a=55, b=66)


test()

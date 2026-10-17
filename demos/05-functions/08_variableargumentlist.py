def show_arg_lists(arg: int, *args: int, **kwargs: int) -> None:
    """Demonstrate positional and keyword variable-length arguments."""
    print("arg   :", arg)
    print("args  :", args)
    print("kwargs:", kwargs)


show_arg_lists(1, 2, 3, 4, 5, x=1, y=2)
show_arg_lists(33, x=8, y=9)
show_arg_lists(44)

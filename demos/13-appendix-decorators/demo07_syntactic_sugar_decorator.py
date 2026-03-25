def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))

    return func_wrapper


@p_decorate
def get_text(name):
    return "Hello {0} how are you".format(name)


print(get_text("Albert"))

# Outputs <p>Hello Albert, how are you</p>

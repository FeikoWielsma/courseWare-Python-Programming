def get_text(name):
    return "Hello {0}, how are you".format(name)


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))

    return func_wrapper


my_get_text = p_decorate(get_text)

print(my_get_text("Albert"))

# <p>Outputs Hello Albert, how are you</p>

get_text = p_decorate(get_text)

print(get_text("John"))

# <p>Outputs Hello Albert, how are you</p>

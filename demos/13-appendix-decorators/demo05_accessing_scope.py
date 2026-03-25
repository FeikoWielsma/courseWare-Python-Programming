def start_at(start):
    def increment_by(inc):
        return start + inc

    return increment_by


f = start_at(10)
g = start_at(100)

print(f(1), g(2))  # print 11 102


# inner function accessing outer scope
def compose_greet_func(name):
    def get_message():
        return "Hello there " + name + "!"

    return get_message


greet = compose_greet_func("Albert")
print(greet())

# Outputs: Hello there Albert

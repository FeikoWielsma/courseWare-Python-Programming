def greet(name):
    def get_message():
        return "Hello "

    result = get_message()+name
    return result

print (greet("Albert"))

# Outputs: Hello Albert
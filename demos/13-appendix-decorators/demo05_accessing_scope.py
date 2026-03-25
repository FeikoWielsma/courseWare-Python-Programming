def startAt(start):
    def incrementBy(inc):
        return start + inc
    return incrementBy

f = startAt(10)    
g = startAt(100)

print (f(1), g(2))  # print 11 102

# inner function accessing outer scope
def compose_greet_func(name):
    def get_message():
        return "Hello there "+name+"!"

    return get_message

greet = compose_greet_func("Albert")
print (greet())

# Outputs: Hello there Albert
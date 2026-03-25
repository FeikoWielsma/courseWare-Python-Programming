instances = {} #dictionary to hold class and their only instance

def getInstance(klass,*args): #this function is used by decorator
    if klass not in instances:
        instances[klass]=klass(*args)
    return instances[klass]

def singleton(klass): #decorator function
    def onCall(*args):
        return getInstance(klass,*args)
    return onCall

@singleton
class Star:
    def __init__(self,name):
        self.name=name

#A solar system should have only one star
sun = Star('Sun')
print (sun.name)
taurus = Star('Taurus')
print (taurus.name)
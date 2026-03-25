class Person:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello, world! I'm %s." % self.name

p = Person()
p.setName('pipo')
print p.getName()
p.greet()
print p.name
# print Person().name
#Person().setName('mamaloe')
#print Person().getName()
#Person().greet()
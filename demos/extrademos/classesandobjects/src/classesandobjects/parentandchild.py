class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"
   def parentMethod(self):
      print 'Calling parent method'
   def setAttr(self, attr):
      Parent.parentAttr = attr
   def getAttr(self):
      #print "Parent attribute :", Parent.parentAttr
      return Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"
   def childMethod(self):
      print 'Calling child method'

p = Parent()
c = Child()

print p.getAttr()
p.setAttr("pipo")
print p.getAttr()

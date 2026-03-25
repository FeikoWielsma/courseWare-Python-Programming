class MyClass(object):
   pass
   def __del__(self):
       print('Inside destructor')

a = MyClass()
a.obj = a
del a
input('Give input to terminate:')
from anygui import *
def hello(event): print 'Hello, world!'
btn = Button(text='Hello')
link(btn, hello)

win = Window(title='Hello, Anygui!')
win.add(btn)

btn.size = win.size = 200, 100
app = Application()
app.add(win)

app.run()

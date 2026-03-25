from anygui import *

app = Application()
win = Window()
app.add(win)

loadButton = Button(text="Open")
win.add(loadButton)

saveButton = Button(text="Save")
win.add(saveButton)

app.run()

from anygui import *
app = Application()
win = Window()
app.add(win)

loadButton = Button(text='Open')
loadButton.geometry = 225, 5, 80, 25
win.add(loadButton)

saveButton = Button(text='Save')
saveButton.geometry = 315, 5, 80, 25
win.add(saveButton)

filename = TextField()
filename.geometry = 5, 5, 210, 25
win.add(filename)

contents = TextArea()
contents.geometry = 5, 35, 390, 260
win.add(contents)

app.run()

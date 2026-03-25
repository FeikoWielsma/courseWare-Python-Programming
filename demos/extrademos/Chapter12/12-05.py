from anygui import *
app = Application()
win = Window(title='Simple Editor')
app.add(win)

saveButton = Button(text='Save', height=25)
win.add(saveButton, right=5, top=5, hmove=1)

loadButton = Button(text='Open', height=25)
win.add(loadButton, right=(saveButton, 10), top=5, hmove=1)

filename = TextField(height=25)
win.add(filename, right=(loadButton, 10), top=5, left=5, hstretch=1)
contents = TextArea()
win.add(contents, top=(filename, 5), left=5, right=5, bottom=5,
        hstretch=1, vstretch=1)

def load(event):
    file = open(filename.text)
    contents.text = file.read()
    file.close()

link(loadButton, load)

def save(event):
    file = open(filename.text, 'w')
    file.write(contents.text)
    file.close()

link(saveButton, save)
app.run()

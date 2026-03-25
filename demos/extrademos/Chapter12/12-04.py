from anygui import *

app = Application()
win = Window()
app.add(win)

saveButton = Button(text="Save", height=25)
# 5 points from the right window edge and 5 points from the top; move button
# horizontally to keep it that way:
win.add(saveButton, right=5, top=5, hmove=1)

loadButton = Button(text="Open", height=25)
# 10 points from saveButton (to the right) and 5 points from the top; move button
# horizontally to keep it that way:
win.add(loadButton, right=(saveButton, 10), top=5, hmove=1)

filename = TextField()
# 10 points from loadButton (to the right), 5 points from the top, and 5 points
# from the left edge of the window; stretch text field horizontally to keep it
# that way:
win.add(filename, right=(loadButton, 10), top=5, left=5, hstretch=1)

contents = TextArea()
# 5 points from filename (above), 5 points from the left edge of the window,
# 5 points from the right edge of the window, and 5 points from the bottom of
# the window; stretch text area both horizontally and vertically to keep it that
# way:
win.add(contents, top=(filename, 5), left=5, right=5, bottom=5, hstretch=1, vstretch=1)

app.run()

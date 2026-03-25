from wxPython.wx import *
def hello(event): print 'Hello, world!'
class MyApp(wxApp):
    def OnInit(self):
        win_id = wxNewId()
        win = wxFrame(NULL, win_id, 'Hello, wxPython!',
                      size=wxSize(200, 100))
        btn_id = wxNewId()
        btn = wxButton(win, btn_id, 'Hello')
        EVT_BUTTON(btn, btn_id, hello)
        win.Show(true)
        return true

app = MyApp()
app.MainLoop()

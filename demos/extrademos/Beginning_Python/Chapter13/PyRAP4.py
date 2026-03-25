#!/usr/bin/env python
import findgtk
import gtk
import time
import gobject

class PyRAPGUI:
    def __init__(self):
        self.wTree = gtk.glade.XML ("PyRAP.glade", "window1")
        dic={ "on_window1_destroy" : self.quit,
              "on_button1_clicked" : self.send,
              "on_treeview1_button_press_event": self.moduletree_press,
              }
        self.wTree.signal_autoconnect (dic)
        self.username="Bob"
        #setup the text view to act as a log window
        self.logwindowview=self.wTree.get_widget("textview1")
        self.logwindow=gtk.TextBuffer(None)
        self.logwindowview.set_buffer(self.logwindow)

        #initialize our host tree
        self.hosttree=self.wTree.get_widget("treeview1")
        model=gtk.TreeStore(gobject.TYPE_STRING, gobject.TYPE_STRING)
        self.hostsmodel=model
        host_inter=self.insert_row(model,None,'www.immunitysec.com', 'Default Main Server')
        self.hosttree.set_model(model)
        renderer=gtk.CellRendererText()
        column=gtk.TreeViewColumn("Host/Channel",renderer, text=0)
        column.set_resizable(True)
        self.hosttree.append_column(column)

        renderer=gtk.CellRendererText()
        column=gtk.TreeViewColumn("Users",renderer, text=1)
        column.set_resizable(True)
        self.hosttree.append_column(column)

    def insert_row(self, model, parent, firstcolumn, secondcolumn,
                   thirdcolumn=None):
        myiter=model.insert_after(parent,None)
        model.set_value(myiter,0,firstcolumn)
        model.set_value(myiter,1,secondcolumn)
        if thirdcolumn != None:
            model.set_value(myiter,2,thirdcolumn)
        return myiter

    #Handlers for the GUI signals
    def quit(self,obj):
        "Handles the 'destroy' signal of the window."
        gtk.main_quit()
        sys.exit(1)
        
    def send(self,obj):
        "Handles the 'clicked' signal of the button."
        message=self.wTree.get_widget("entry1").get_text()
        print "Message=%s" % message
        self.log(self.username + ": " + message, "black")

    def treeview1_press(self,obj,event):
        """
        Handle people double clicking on our tree view
        """
        #print "Clicked"
        if event.type==gtk.gdk._2BUTTON_PRESS:
            #print "Double click"
            model,iter=self.treeview1.get_selection().get_selected()
            if iter==None:
                print "weird - nothing was selected, yet we got a double-click"
                return
            nodetext=model.get_value(iter,0)
            #now do something based on nodetext.
        #...
        
    def log(self,message,color,enter="\n"):
        """
        A helper method for the "send" GUI signal handler: 
        logs a message to the log window and scrolls the window to the bottom
        """
        message=message+enter
        
        buffer = self.logwindow
        iter = buffer.get_end_iter()
        #gtk versioning avoidance
        if color != "black":
            tag = buffer.create_tag()
            tag.set_property("foreground", color)
            self.logwindow.insert_with_tags(buffer.get_end_iter(), message, tag)	
        else:
            self.logwindow.insert(iter, message)
        #gtk.FALSE and gtk.TRUE on older pyGTK
        mark = buffer.create_mark("end", buffer.get_end_iter(), False)
        self.logwindowview.scroll_to_mark(mark,0.05,True,0.0,1.0)
        #print "Exited log function"

if __name__ == '__main__':    
    PyRAPGUI()
    try:
        gtk.threads_init()
    except:
        print "No threading was enabled when you compiled pyGTK!"
        import sys
        sys.exit(1)
    gtk.threads_enter()
    gtk.main()
    gtk.threads_leave()

# $Id: base.py,v 1.2 2004/04/10 21:22:11 mandava Exp $

# This is a program which creates a window and has
# no way of exiting except to be killed by using the shell.

# Importing pygtk module and initializing the gtk+ environment.

import gtk

# The python class named base defines a class instance initialization
# method __init__(). this __init__ function creates a top level window
# and directs gtk+ to display it. The Gtk window is created with the
# argument gtk.WINDOW_TOPLEVEL that specifies that we want the window
# to undergo window manager decoration and placement.the window is set to
# 200 by 200 by default so that you can manipulate it.


class base:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.show()

    # This function defines the main() method which calls the pyGTK main()
    # function which in turn invokes GTK+ main event processing loop to handle
    # mouse and keyboard events as well as window events.

    def main(self):
        gtk.main()


# The following lines check if the __name__ variable is "__main__" which
# indicates that the program is being run directly from python and not
# being imported into a running python imterpreter. The
# program creates a new instance of the base class and saves a reference
# to it in the variable window.It then invokes the method main() to start the
# GTK event processing loop. When control reaches this point , GTK will
# sleep waiting for events,timeouts,or file IO notifications to occur.

if __name__ == "__main__":
    window = base()
    window.main()

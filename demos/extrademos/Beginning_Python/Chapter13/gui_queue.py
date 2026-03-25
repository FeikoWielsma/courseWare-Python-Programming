#!/usr/bin/env python
"""
gui_queue.py

This Python modules does what we need to do to avoid threading issues on both Linux and Windows.
Your other modules can include this file and use it without knowing anything about gtk.
"""

#Python License for Beginner's Python book

import findgtk
import gtk
import random
import socket
import time
from threading import RLock
import timeoutsocket #used for set_timeout()

class gui_queue:
    """wakes up the gui thread which then clears our queue"""
    def __init__(self,gui,listenport=0):
        """If listenport is 0, we create a random port to listen on"""
        self.mylock=RLock()
        self.myqueue=[]
        if listenport==0:
            self.listenport=random.randint(1025,10000)
        else:
            self.listenport=listenport
        print "Local GUI Queue listening on port %s"%self.listenport
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("", self.listenport))  
        self.listensocket=s
        self.listensocket.listen(300) #listen for activity.
        #time.sleep(15)
        self.gui=gui
        return
    
    def append(self,command,args):
        """
        Append can be called by any thread
        """
        #print "about to acquire..."
        self.mylock.acquire()
        self.myqueue.append((command,args))
        #this won't work on a host with a ZoneAlarm firewall 
        #or no internet connectivity...
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #small timeout will wake up the gui thread, but not
        #cause painful pauses if we are already in the gui thread.
        #important to note that we use timeoutsocket and it
        #is already loaded.
        s.set_timeout(0.01)
        #wakey wakey!
        #print "Connecting to port %d"%self.listenport
        try:
            s=s.connect(("localhost",self.listenport))
        except:
            #ignore timeouts
            pass
        #print "About to release"
        self.mylock.release()
        return

    def clearqueue(self, socket, x):
        """
        Clearqueue is only called by the main GUI thread
        Don't forget to return 1
        """
        #print "Clearing queue"
        #clear this...TODO: add select call here.
        newconn,addr=self.listensocket.accept()
        for i in self.myqueue:
            (command,args)=i
            self.gui.handle_gui_queue(command,args)
        self.myqueue=[]
        return 1

class Queued:

    def __init__(self):
        self.gui_queue=gui_queue(self) #our new gui queue
        #for older pyGTK:
        #gtk.input_add(self.gui_queue.listensocket,
        #              gtk.gdk.INPUT_READ, self.gui_queue.clearqueue)
        #
        #for newer pyGTK (2.6):
        import gobject
        gobject.io_add_watch(self.gui_queue.listensocket, gobject.IO_IN,
                             self.gui_queue.clearqueue)

    def handle_gui_queue(self, command, args):
        """
        Callback the gui_queue uses whenever it receives a command for us.
        command is a string
        args is a list of arguments for the command
        """
        gtk.threads_enter()
        #print "handle_gui_queue"
                
        method = getattr(self, command, None)
        if method:
            apply(method, args)
        else:
            print "Did not recognize action to take %s: %s"%(command,args)
        #print "Done handling gui queue"
        gtk.threads_leave()
        return 1
    
    def gui_queue_append(self,command,args):
        self.gui_queue.append(command,args)
        return 1

from xmlrpclib import ServerProxy, Fault
from server import Node, UNHANDLED
from client import randomString
from threading import Thread
from time import sleep
from os import listdir
import sys
from anygui import *

HEAD_START = 0.1 # Seconds
SECRET_LENGTH = 100

class ListableNode(Node):
    """
    An extended version of Node, which can list the files
    in its file directory.
    """
    def list(self):
        return listdir(self.dirname)

class Client(Application):
    """
    The main client class, which takes care of setting up the GUI and
    starts a Node for serving files.
    """
    def __init__(self, url, dirname, urlfile):
        """
        Creates a random secret, instantiates a ListableNode with that secret,
        starts a Thread with the ListableNode's _start method (making sure the
        Thread is a daemon so it will quit when the application quits),
        reads all the URLs from the URL file and introduces the Node to
        them. Finally, sets up the GUI.
        """
        Application.__init__(self)
        self.secret = randomString(SECRET_LENGTH)
        n = ListableNode(url, dirname, self.secret)
        t = Thread(target=n._start)
        t.setDaemon(1)
        t.start()
        # Give the server a head start:
        sleep(HEAD_START)
        self.server = ServerProxy(url)
        for line in open(urlfile):
            line = line.strip()
            self.server.hello(line)
        self.setUp()

    def updateList(self):
        """
        Updates the ListBox with the names of the files available
        from the server Node.
        """
        self.files.items = self.server.list()

    def setUp(self):
        """
        Sets up the GUI. Creates a Window, a TextField, and a Button, and
        a ListBox, and lays them out. Binds the submit Button to
        self.fetchHandler.
        """
        win = Window(title='File Sharing Client')
        self.add(win)

        self.input = input = TextField()
        submit = Button(text='Fetch', height=input.height)

        self.files = files = ListBox()
        self.updateList()

        win.add(submit,
                top=10,
                right=10,
                hmove=1)

        win.add(input,
                top=10,
                left=10,
                right=(submit, 10),
                hstretch=1)

        win.add(files,
                top=(input,10),
                left=10,
                right=10,
                bottom=10,
                hstretch=1,
                vstretch=1)

        link(submit, self.fetchHandler)

    def fetchHandler(self, event):
        """
        Called when the user clicks the 'Fetch' button. Reads the
        query from the TextField, and calls the fetch method of the
        server Node. After handling the query, updateList is called.
        If the query is not handled, an error message is printed.
        """
        query = self.input.text
        try:
            self.server.fetch(query, self.secret)
            self.updateList()
        except Fault, f:
            if f.faultCode != UNHANDLED: raise
            print "Couldn't find the file", query

def main():
    urlfile, directory, url = sys.argv[1:]
    client = Client(url, directory, urlfile)
    client.run()

if __name__ == '__main__': main()

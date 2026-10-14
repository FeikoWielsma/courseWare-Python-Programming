#!/usr/bin/python
#
# SockServUDP.py: SocketServer-based server program
#
# Create a BaseRequestHandler subclass, overriding the
# superclass' handle() method to define functionality.
#
import SocketServer

class UCHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        remote = self.client_address    # gets remote client address
        data, skt = self.request        # gets data and socket for reply
        print data
        skt.sendto(data.upper(), remote)# sends response back

myaddr = ('127.0.0.1', 11111)           # Our "standard" address
#
# The next line creates a SocketServer that will use a
# UCHandler to handle each request that it receives.
#
myserver = SocketServer.UDPServer(myaddr, UCHandler)
#
# Then we just tell the server to keep on serving ...
#
myserver.serve_forever()


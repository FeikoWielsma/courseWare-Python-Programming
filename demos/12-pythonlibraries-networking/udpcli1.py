#!/usr/bin/python
#
# udpcli1.py: simplest client program
#
# Gets a string from the user, has a server process it, prints the result
#
from socket import socket, AF_INET, SOCK_DGRAM
srvaddr = ('127.0.0.1', 11111)      # server address
data = raw_input("Send: ")          # gets data from user
s = socket(AF_INET, SOCK_DGRAM)     # create a socket
s.bind(('127.0.0.1', 0))            # can also use ('', 0) - what's different?
s.sendto(data, srvaddr)             # send the data
data, addr = s.recvfrom(1024)       # receive the reply
print "Recv:", data

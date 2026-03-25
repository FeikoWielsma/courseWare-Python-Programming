#!/usr/bin/python
#
#
#
from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.bind(('127.0.0.1', 11111))
s.listen(5)
while 1:
    sock, addr = s.accept()
    while 1:
        data = sock.recv(1024) # max byte count
        if data == "\r\n":
            break
        sock.send(data.upper())
    sock.close()
    print "Connection closed"

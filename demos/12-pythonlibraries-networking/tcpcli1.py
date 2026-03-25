#!/usr/bin/python
#
# tcpc1.py
#
from socket import socket, AF_INET, SOCK_STREAM
srvaddr = ('127.0.0.1', 11111)
s = socket(AF_INET, SOCK_STREAM)
s.connect(srvaddr)
while 1:
    data = raw_input("Send: ")
    s.send(data + "\r\n")
    if data == "":
        break
    data = s.recv(1024)
    print data[:-2]
s.close()

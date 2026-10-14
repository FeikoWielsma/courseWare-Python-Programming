#!/usr/bin/python
#
# udpserv1.py: the simplest imaginable UDP server program
#
# It returns the upper case equivalent of each received string
#
from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 11111))
while 1: # nowadays, "while True"
    data, addr = s.recvfrom(1024)
    print "Received %r from %s " % (data, addr)
    s.sendto(data.upper(), addr)

#!/usr/bin/python
# creosote.py - first pass

import sys, socket

def spew(msg, host='localhost', port=7739):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 0))
    s.sendto(msg, (host, port))

def bucket(port=7739):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', port))
    print 'creosote bucket waiting on port: %s' % port
    while 1:
        data, addr = s.recvfrom(1024)
        print `data`[1:-1]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        bucket()
    else:
        from string import joinfields
        spew(joinfields(sys.argv[1:],' '))



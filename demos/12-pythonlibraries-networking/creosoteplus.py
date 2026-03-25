#!/usr/bin/python
# creosote.py - lightweight message passing with datagrams
# author: jeffbauer@bigfoot.com
# over-the-top logging by sholden@holdenweb.com

"""
$Revision: 4 $
$Date: 6/23/03 5:11p $
Steve Holden    http://www.holdenweb.com/

Version History

4   June 23, 2003 - Attempted to flush standard output from bucket,
    while retaining message splitting functionality added earlier.
    SH.
0.4 November 3, 1998 - Fixed spew buffer overflow error reported by
    David Ascher.  Apparently winsock does not respect the buffer limit.
0.3 August 26, 1998  - Minor improvements
"""

__version__="4"

import socket, time, sys

BUFSIZE = 4096
PORT = 7739
MAXLEN = 72

def spew(msg, host='localhost', port=PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 0))
    while msg:
        s.sendto(msg[:BUFSIZE], (host, port))
        msg = msg[BUFSIZE:]

def bucket(port=PORT, logfile=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', port))
    print 'creosote bucket waiting on port: %s' % port
    if logfile:
        f = open(logfile, 'a+')
    while 1:
        try:
            data, addr = s.recvfrom(BUFSIZE)
            d = `data`[1:-1]
            msg = ""
            m = "%s %s" % (time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(time.time())), d)
            while len(m) > MAXLEN:
                i =  m.rfind(" ", 20, MAXLEN)
                if i == -1:
                    msg = msg + m[:MAXLEN] + "\\\n"
                    m = "                    "+m[MAXLEN:]
                else:
                    msg = msg + m[:i] + "\n"
                    m = "                    "+m[i+1:]
            msg = msg+m
            print msg
            if logfile:
                print >> f, msg
                logfile.flush()
        except socket.error, msg:
            print msg
        sys.stdout.flush()

class MrCreosote:
    """lightweight message passing with datagrams"""
    def __init__(self, host='localhost', port=PORT):
        self.host = host
        self.port = port
        self.client = None
        self.disabled = 0
        self.redirect_server = None
        self.redirect_client = None
    def bucket(self, logfile=None):
        bucket(self.port, logfile)
    def redirector(self, host, port=PORT):
        if self.disabled:
            return
        if self.redirect_server is None:
            self.redirect_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.redirect_server.bind('', self.port)
        if self.redirect_client is None:
            self.redirect_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.redirect_client.bind('', 0)
        while 1:
            data, addr = self.redirect_server.recvfrom(BUFSIZE)
            self.redirect_client.sendto(data, (host, port))
    def spew(self, msg):
        if self.disabled:
            return
        if self.client is None:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.client.bind('', 0)
        while msg:
            self.client.sendto(msg[:BUFSIZE], (self.host, self.port))
            msg = msg[BUFSIZE:]

if __name__ == '__main__':
    """usage: creosote [message]"""
    import sys
    if len(sys.argv) < 2:
        bucket()
    else:
        spew(" ".join(sys.argv[1:]))



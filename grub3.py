#!/usr/bin/python

import socket
import time
socket.setdefaulttimeout(2)
# s = socket.socket()
# a = socket.socket()
# b = socket.socket()
target = "attackdirect.samsclass.info"
port = 3300
hiddenPort = 3003

while port < 4000:

    a = socket.socket()
    b = socket.socket()
    s = socket.socket()
    s.connect((target, 3100))
    print 'Connecting first port 3100'
    try:
        a.connect((target, port))
        print "Connecting second port %d" % port
        time.sleep(2)
    except socket.error:
        print 'Error.'
    try:
        b.connect((target, hiddenPort))
        print b.recv(1024)
        break
    except socket.error:
        print 'Not this port!'
        port += 100
        b.close()
        a.close()
        s.close()

b.close()
a.close()
s.close()


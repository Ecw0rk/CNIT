#!/usr/bin/python

import socket
import time
import socket
socket.setdefaulttimeout(2)

i = 1000
while i < 4000:
    print "connecting port %d" % i
    try:
        s = socket.socket()
        s.connect(("attackdirect.samsclass.info", i))
        print s.recv(1024)
        break
    except socket.error:
        print "Not this port!"
        i += 1000

s.close()

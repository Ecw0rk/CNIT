#!/usr/bin/python

import socket
s = socket.socket()
socket.timeout(2)

i = 1000
while i < 4000:
    s.connect(("attack.samsclass.info", i))
    print s.recv(1024)
    s.close()

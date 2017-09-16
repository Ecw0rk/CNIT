#!/usr/bin/python

import socket
import time
socket.setdefaulttimeout(2)
s = socket.socket()
target = raw_input('Target URL: ')
tport = int(raw_input('Target Port: '))

s.connect((target, tport))
# time.sleep(5)
print s.recv(1024)
s.close()

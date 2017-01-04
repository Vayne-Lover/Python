#!/usr/local/bin/python
import socket
import select

s=socket.socket()

host=socket.gethostname()
port=1234
s.bind((host,port))

s.listen(5)

epoll=select.epoll()
epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)
while True:
    epoll_list=epoll.poll()
    for fd.events in epoll_list:
        if fd == s.fileno():
            c,addr=s.accept()
            print 'Get connection.',addr

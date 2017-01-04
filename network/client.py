#!/usr/local/bin/python
import socket

c=socket.socket()

host=socket.gethostname()
port=1234

c.connect((host,port))
print c.recv(1024) 

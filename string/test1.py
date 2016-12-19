#!/usr/local/bin/python
from string import Template
a="Hello,%s,%s."
b=('world','%python')
c=a%b
print c
d="This is %.3f"
e=3.4567
f=d % e
print f 
x="ihihihi"
g=Template("HAHAH,$x,yeah")
h=g.substitute(x="ihihihi")
print h

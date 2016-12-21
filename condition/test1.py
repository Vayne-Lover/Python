#!/usr/local/bin/python
#print 'Age:',42
#print 1,2,3
#print (1,2,3)
#print 'Hello'+','+'world!'
#print 'Hi',
#print 'Y'
#x,y=1,2
#print x,y
#x,y=y,x
#print x,y
#x,y,res=[1,2,3,4]
#print res
#a=2
#a+=2
#print a
#print bool(''),bool({}),bool([]),bool(0),bool(None)
#x=y=[1,2,3]
#z=[1,2,3]
#print x==z
#print x is z
#b=4
#c= b*3 if b<5 else b
#print c
#x=1
#while x<=5:
#  print x
#  x+=1
#print x
#for i in range(0,3):
#  print i
#d={'a':1,'b':2}
#for k in d:
#  print k,d[k]
#a=['x','y','z']
#b=[1,2,3]
#for i in zip(a,b):
#  print a,b
#for i in zip(xrange(0,5),xrange(122)):
#  print i
#print sorted([3,5,2])
#print reversed([3,5,4])
#print [ x*x for x in range(0,10) if x%3==0 ]
girls=['alice','bernice','clarice']
boys=['chris','arnold','bob']
letterGirls={}
for girl in girls:
  letterGirls.setdefault(girl[0],[]).append(girl)
print letterGirls
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]
a={'x':1,'y':2}
b=a
print b
a=None
#del b
print b
exec 'print "Hello!"'
from math import sqrt
scope={}
exec 'sqrt=1' in scope
print sqrt(4)
print scope['sqrt']
print scope.keys()
scope['x']=2
scope['y']=3
print eval('x*y',scope)

#!/usr/local/bin/python
__metaclass__=type
class Fibs:
  def __init__(self):
    self.a=0
    self.b=1
  def __iter__(self):
    return self
  def next(self):
    self.a,self.b=self.b,self.a+self.b
fibs=Fibs()
for i in xrange(10):
  fibs.next()
  print fibs.a    
it=iter([1,2,3,4])
print it.next()
print it.next()

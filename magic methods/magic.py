#!/usr/local/bin/python
#class A:
#  def __init__(self):
#    self.value=42
#a=A()
#print a.value
#class B:
#  def __init__(self,value=25):
#    self.v=value
#b=B()
#print b.v
#class A:
#  def v(self):
#    print 'A'
#class B(A):
#  pass
#class C(A):
#  def v(self):
#    print 'C'
#a=A()
#a.v()
#b=B()
#b.v()
#c=C()
#c.v()
__metaclass__=type
class Bird:
  def __init__(self):
    self.h=True
  def eat(self):
    if self.h:
      print 'H!'
      h=False
    else:
      print 'N h!'
class SongBird(Bird):
  def __init__(self):
    #Bird.__init__(self)
    super(SongBird,self).__init__()
    self.s='Sound'
  def sing(self):
    print 'Sing!'
bd=Bird()
bd.eat()
bd.eat()
sb=SongBird()
sb.eat()
sb.sing()

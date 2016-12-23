#!/usr/local/bin/python
_metaclass_=type
#class Person:
#  def setName(self,name):
#    self.name=name
#  def getName(self):
#    return self.name
#  def greet(self):
#    print "Hello world!I'm %s" % self.name
#a=Person()
#b=Person()
#a.setName('HI')
#b.setName('HA')
#a.greet()
#b.greet() 
#print a.name
#class Secretive:
#  def __inaccessable(self):
#    print "Can't see me."
#  def accessable(self):
#    print 'The message:'
#    self.__inaccessable()
#c=Secretive()
#c.accessable()
#c._Secretive__inaccessable()
class Filter:
  def init(self):
    self.blocked=[]
  def filter(self,seq):
    return [x for x in seq if x not in self.blocked]
class SPAMFilter(Filter):
  def init(self):
    self.blocked=['SPAM']
class Talk:
  def talk(self):
    print "Talk."
class TalkFilter(Talk,Filter):
  pass
a=SPAMFilter()
a.init()
s=['SPAM','hi','SPAM','ha']
b=a.filter(s)
print b
print issubclass(SPAMFilter,Filter)
print SPAMFilter.__bases__
print isinstance(a,SPAMFilter)
print s.__class__
c=TalkFilter()
print TalkFilter.__bases__
c.talk()


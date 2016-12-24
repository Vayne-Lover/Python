#!/usr/local/bin/python
#class MuffledCalculator:
#  muffled=False
#  def calc(self,expr):
#    try:
#      return eval(expr)
#    except (ZeroDivisionError,TypeError):
#      if self.muffled:
#        print "There are errors."
#      else:
#        raise
#a=MuffledCalculator()
#print a.calc('2/1')
##print a.calc('2/"dsf"')
##print a.calc('1/0')
#a.muffled=True
#print a.calc('1/0')
#class Test:
#  def init(self): 
#    try:
#      x=1
#      y='sg'
#      print x/y
#    except (ZeroDivisionError,TypeError),e:
#      print e
#a=Test()
#a.init()    
#class Test1:
#  def init(self): 
#    try:
#      x=1
#      y='sg'
#      print x/y
#    except Exception,e:
#      print e
#a=Test1()
#a.init()
#try:
#  print 'Go!'
#except Exception,e:
#  print e
#else:
#  print 'Planned.'
x=1
try:
  x=2
  print x
  x=1/0
except Exception,e:
  x=3
  print x
  print e
finally:
  x=4
  print x


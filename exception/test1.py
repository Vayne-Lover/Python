#!/usr/local/bin/python
class MuffledCalculator:
  muffled=False
  def calc(self,expr):
    try:
      return eval(expr)
    except ZeroDivisionError:
      if self.muffled:
        print "Can't divide zero"
      else:
        raise
a=MuffledCalculator()
print a.calc('2/1')
#print a.calc('1/0')
a.muffled=True
print a.calc('1/0')

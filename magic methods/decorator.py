#!/usr/local/bin/python
__metaclass__=type
class Temp:
  @staticmethod
  def smeth():
    print 'Static method!'
  
  @classmethod
  def cmeth(cls):
    print 'Class method of ',cls
Temp().smeth()
Temp().cmeth()

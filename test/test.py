#!/usr/local/bin/python
import unittest,my_math

class ProductTestCase(unittest.TestCase):
  def testInt(self):
    for x in xrange(-10,10):
      for y in xrange(-10,10):
        p=my_math.product(x,y)
        self.failUnless(p==x*y,'Int failed.')

  def testFloat(self):
    for x in xrange(-10,10):
      for y in xrange(-10,10):
        x=x/10.0
        y=y/10.0
        p=my_math.product(x,y)
        self.failUnless(p==x*y,'Float failed.')

if __name__=='__main__':
  unittest.main()

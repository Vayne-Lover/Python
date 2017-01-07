#!/usr/local/bin/python
import profile
def foo(x,y):
  return x*y

if __name__=="__main__":
  profile.run("foo(1,2)")

#!/usr/local/bin/python

import random

def print_image(s):
  def line(pos,length=len(s)):
    return '. '*(pos)+'X'+'. '*(length-pos-1)
  for pos in s:
    print line(pos)

def conflict(state,nextX):
  nextY=len(state)
  for i in range(nextY):
    if abs(state[i]-nextX) in (0,nextY-i):
      return True
  return False

def queens(num=8,state=()):
  for pos in range(num):
    if not conflict(state,pos):
      if len(state)==num-1:
        yield (pos,) 
      else:
        for result in queens(num,state+(pos,)):
          yield (pos,) + result

#print list(queens(4))
print_image(random.choice(list(queens(8))))

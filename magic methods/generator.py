#!/usr/local/bin/python
def flat(nested):
  for sublist in nested:
    for element in sublist:
      yield element
nested_list=[[1,2],[3,4],[5,6,7]]
for i in flat(nested_list):
  print i
def repeater(v):
  while True:
    new=(yield v)
    if new is not None:
      v=new
r=repeater(10)
print r.next()
print r.send('Hi!')

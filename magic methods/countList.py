#!/usr/local/bin/python
class CountList(list):
  def __init__(self,*args):
    super(CountList,self).__init__(*args)
    self.count=0
  def __getitem__(self,index):
    self.count+=1
    return super(CountList,self).__getitem__(index)
cl=CountList(range(10))
print cl
print cl.reverse()
print cl
print cl[1]+cl[2]
print cl.count

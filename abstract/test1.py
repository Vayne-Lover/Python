#!/usr/local/bin/python
#fib=[0,1]
#for i in range(0,8):
#  fib.append(fib[-2]+fib[-1])
#print fib
#def fibs(n):
#  fib=[0,1]
#  for i in range(n-2):
#    fib.append(fib[-2]+fib[-1])
#  return fib
#print fibs(5)
#def square(x):
#  'Calculate x*x.'
#  return x*x
##print square._doc_
#help(square)
#def inc(x):
#  x[0]=x[0]+1
#  return x
#a=[2]
#b=inc(a)
#print a
#print b
#def hello(name='hi',str='world'):
#  print '%s,%s'%(name,str)
#hello()
#hello('a')
#hello(str='jjj')
#def para(*p):
#  print p
#para(1)
#para(1,2)
#para(1,2,3)
#def para1(**p):
#  print p
#para1(sth='da',sd='gg')
#def para2(x=1,*y,**z):
#  print x
#  print y
#  print z
#para2(3,2,4,1,stg='sd',saf='pp')
#x=1
#scope=vars()
#print scope['x']
#scope['x']+=1
#print x
def a(x):
  def b(y):
    return x*y
  return b
i=a(3)
print i(4)
j=a(5)
print j(10)
print a(5)(4)
def fac(n):
  if n==1:
    return 1
  else:
    return n*fac(n-1)
print fac(5)


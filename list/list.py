#!/usr/local/bin/python
#a=[1,2,3,4,5,6,7,8,9,10]
#print a[:3]
#print a[-3:]
#print a[:]
#print a[::2]
#print a[8:3:-1]
#print [1,2,3]+[4,5,6]
#print ["Hi"]*3
#print 1 in a
#print max(a)
#print min(a)
#print len(a)
#print list("Hello")
#b=[1,3,5,7,9,8]
#b[1]=4
#print b
#del b[1]
#print b
#c=list("Perl")
#c[1:1]=list('ython')
#c[-4:]=[]
#c.append('n')
#print c.count('t')
#print c
#d=[1,2,3]
#d.extend([4,5,6])
#print d
#e=[7,8,9]
#print e+[10,11,12]
#print e
f=list("abcdefg")
print f.index('c')
f.insert(len(f),'h')
print f
print f.pop()
f.append('h')
print f
f.remove('h')
print f
g=[1,2,3]
g.reverse()
print g
h=[3,4,8,2,6]
i=h[:]
i.sort()
print i
h.sort(reverse=True)
print h
j=['ads','dd','eeeee','asdsadd']
print j.sort(key=len)
print j

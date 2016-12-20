#!/usr/local/bin/python
#items=[('a','b'),(1,2)]
#b=dict(items)
#print b
#c=dict(name='c',age=42)
#print c
#print len(c)
#c['sex']='female'
#print c
#del c['age']
#print c
#print 'sex' in c
#c['age']=25
#print c
#print c.clear()
#print c
#x={'name':'a','age':'14'}
#y=x
#print y
#z=y.copy()
#z.clear()
#print x
#print y
#print z
x={'name':'a','age':14}
y=x.copy()
y['age']=25
print x
print y
a={}
b=a.fromkeys(['name','age'],'(hahaha)')
print b
print b.get('name')
print b.get('hi','N/A')

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
#x={'name':'a','age':14}
#y=x.copy()
#y['age']=25
#print x
#print y
#a={}
#b=a.fromkeys(['name','age'],'(hahaha)')
#print b
#print b.get('name')
#print b.get('hi','N/A')
#c={}
#print c.has_key('name')
#c['name']='Eric'
#print c.has_key('name')
#x={'name':'a','age':'14'}
#print x.items()
#print x.pop('age')
#print x
#y={}
#print y.setdefault('name','N/A')
#print y
#y['name']='Apple'
#y.setdefault('name','N/A')
#print y
x={'a':'1','b':'2','c':'3'}
y={'c':'5'}
x.update(y)
print x
print x.values()

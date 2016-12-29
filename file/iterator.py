#!/usr/local/bin/python
f=open(r'/Users/Vayne-Lover/Desktop/CS/Python/PythonPractice/file/somefile1.txt','w')
f.write('123\n')
f.write('456\n')
f.write('789\n')
f.close()
lines=list(open(r'somefile1.txt','r'))
print lines
a,b,c=open('somefile1.txt')
print a
print b
print c

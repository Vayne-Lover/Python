#!/usr/local/bin/python
f=open(r'/Users/Vayne-Lover/Desktop/CS/Python/PythonPractice/file/somefile.txt','w')
f.write('01234567890123456789')
f.seek(5)
f.write('Hello,world!')
f.close()
f=open('/Users/Vayne-Lover/Desktop/CS/Python/PythonPractice/file/somefile.txt')
print f.read()

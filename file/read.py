#!/usr/local/bin/python
import pprint
#with open('/Users/Vayne-Lover/Desktop/CS/Python/PythonPractice/file/somefile.txt') as f:
#  print f.read(7)
#  print f.read()
#  f.close()
#f=open('/Users/Vayne-Lover/Desktop/CS/Python/PythonPractice/file/somefile.txt')
#for i in range(3):
#  print f.readline()
#f.close()
#pprint.pprint(open('/Users/Vayne-Lover/Desktop/CS/Python/PythonPractice/file/somefile.txt').readlines())
f=open('/Users/Vayne-Lover/Desktop/CS/Python/PythonPractice/file/somefile.txt')
lines=f.readlines()
lines[1]='HiHiHi\n'
f.close()
f=open('/Users/Vayne-Lover/Desktop/CS/Python/PythonPractice/file/somefile.txt','w')
f.writelines(lines)
#for i in lines:
#  print i
f.close


#!/usr/local/bin/python
#f=open('/Users/Vayne-Lover/Desktop/CS/Python/PythonPractice/file/somefile.txt')
#while True:
#  char=f.read(1)
#  if not char:
#    break
#  print char
#f.close()
f=open('/Users/Vayne-Lover/Desktop/CS/Python/PythonPractice/file/somefile.txt')
while True:
  line=f.readline()
  if not line:
    break
  print line
f.close()

#!/usr/local/bin/python
# -*- coding: utf-8 -*- 

def return_chinese(s):
  if isinstance(s,unicode):
    return s.encode('utf-8')
  else:
    return s.decode('utf-8').encode('utf-8')

s='Hi'
print isinstance(s,unicode)
print isinstance(s,str)
print s.decode('ascii').encode('utf-8')
str='中文'
print 'Type of str: ',type(str)
print 'Value of str: ',str
u=u'中文'
print 'Type of u: ',type(u)
print 'Value of u: ',u.encode('gbk')
print 'Value of u: ',u.encode('utf-8')
str1=str.decode('utf-8')
print 'Type of str1: ',type(str1)
print 'Value of str1: : ',str1
str2=str1.encode('utf-8')
print 'Value of str2: ',str2
print return_chinese('Ha')
print return_chinese('测试')



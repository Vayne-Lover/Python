#!/usr/local/bin/python
#print 'Pirce is %d'% 43
#print 'Pirce is %x'% 43
#print 'Pirce is %o'% 43
#from math import pi
#print 'Pi is %.2f'%pi
#print 'Repr %r'%42L
#print 'Str %s'%42L
#print '%10.2f'% 1.334
#print '%-10.2f'% 2.334
#print '%+10.3f'% 3.334
#print '%010.2f'% 4.334
#print '% 10.2f'% 5.334
#print '%.*s' %(5,'Cplusplus hiee')
#print "hihihi ads sad fd a".find('ads')
#print "dasfja safj nf f".find('i')
#print 'asdhi!!! fa '.find('!!!',0,9)
#a=['1','2','3','4','5']
#b='|'.join(a)
#print b
#print 'afkafljAAAAA'.lower()
#print 'afsf'.title()
#c='abcdefg'
#print 'e' in c
#print 'avbdasd'.replace('a','x')
#print 'a|b|d|e'.split('|')
from string import maketrans
table=maketrans('acs','bde')
print 'acs acs'.translate(table,' ')

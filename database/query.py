#!/usr/local/bin/python
import sqlite3,sys

conn=sqlite3.connect('food.db')
curs=conn.cursor()

query='SELECT * FROM food WHERE %s'%  sys.argv[1]

print query
print 
curs.execute(query)
names=[f[0] for f in curs.description]
print 'Description:',curs.description
print 
print names
print
#print curs.fetchall()
print  
for row in curs.fetchall():
  #print curs.fetchall()
  for pair in zip(names,row):
    print '%s : %s'% pair
  print 

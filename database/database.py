#!/usr/local/bin/python
import sqlite3

def convert(v):
  if v.startswith('~'):
    return v.strip('~')
  if not v:
    v='0'
  return float(v)

conn=sqlite3.connect('food.db')
curs=conn.cursor()

curs.execute('''
CREATE TABLE food(
id       TEXT  INTEGER PRIMARY KEY,
desc     TEXT,
water    FLOAT,
kcal     FLOAT,
protein  FLOAT,
fat      FLOAT,
ash      FLOAT,
carbs    FLOAT,
fiber    FLOAT,
sugar    FLOAT
)
''')

query='INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'

for line in open('ABBREV.txt'):
  fields=line.split('^')
  vals=[convert(f) for f in fields[:10]]
  curs.execute(query,vals)

conn.commit()
conn.close()

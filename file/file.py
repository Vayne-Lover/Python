#!/usr/local/bin/python
import sys
text=sys.stdin.read()
words=text.split()
count=len(words)
print 'Words count: ',count

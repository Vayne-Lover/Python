#!/usr/local/bin/python
from urllib import urlopen
import re

p=re.compile('<h3><a .*?><a .*? href="(.*?)">(.*?)</a>')
text=urlopen('http://python.org/community/jobs').read()
for url,name in p.findall(text):
  print 'Start'
  print '%s (%s)'%(name,url)
  print 'End'

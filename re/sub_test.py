#!/usr/local/bin/python
import re

text1='Hello,*world*!'
pat=r'\*([^\*]+)\*'
res1=re.sub(pat,'<em>\\1</em>',text1)
print res1

text2='*This* is *world*'
pat2=r'\*([^\*]+?)\*'
res2=re.sub(pat2,r'<em>\1</em>',text2)
print res2

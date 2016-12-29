import fileinput

for line in fileinput.input():
  line=line.rstrip()
  num=fileinput.lineno()
  print '%-40s # %3i' %(line,num)

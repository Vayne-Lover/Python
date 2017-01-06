#!/usr/local/bin/python

import cgi
form=cgi.FieldStirage()

name=form.getvalue('name','world')

print '''
<html>
  <head>
    <title>Page</title>
  </head>
  <body>
    <h1>Hello,%s</h1>
    <form action='cgi.cgi'>
      Change name<input type='text' name='name' />
      <input type='submit'/>
    </form>
  </body>
</html>
'''%name

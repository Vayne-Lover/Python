#!/usr/local/bin/python
width=input('Please input width: ')
price_width=10
item_width=width-price_width

header='%-*s%*s'
format='%-*s%*.2f'

print width*'='
print header %(item_width,'Item',price_width,'Price')
print width*'-'
print format%(item_width,'Apple',price_width,0.442)
print format%(item_width,'Pears',price_width,0.367)

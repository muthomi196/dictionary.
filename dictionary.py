capital_city = {'Kenya':"Nairobi",'tanzania':'Arusha','Uganda':"Kampala"}
print('initial dictionary:', capital_city)
capital_city['Japan']='tokyo'
print('updated Capital cities:',capital_city)
capital_city['tanzania']='dodoma'
print('updated Capital cities:',capital_city)
del capital_city['Japan']
print('updated Capital cities:',capital_city)
print('capital city:',capital_city['Kenya'])

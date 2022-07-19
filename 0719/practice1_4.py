
air_info=[{
    'name':'A','capital':True,'air_status':{'O2':3,'CO2':2}} ,
    {'name':'B','capital':False,'air_status':{'O2':5,'CO2':3}}]

print  (air_info[0]['air_status']['O2'])

a =[]
for i in range(len(air_info)):
    a.append(air_info[i]['air_status']['O2'])
print(a)

##############################
# air_info=[{},{}]
# air_info[0]= {
#     'name':'A','capital':True,'air_status':{'O2':3,'CO2':2}
# }
# air_info[0]['name']='A'
# air_info[0]['capital'] = True
dic = {'삼겹살':7000,'우동':6000,'막창':50000,'피자':20000}
#print(dic.values())
#print(type(dic.values()))
totalVal = 0
for value in dic.values():
    totalVal = totalVal+ value
print('점심메뉴 평균은?')
print(totalVal/len(dic))

b=sum(dic.values())
print(b)
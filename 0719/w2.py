dic = {'삼겹살':7000,'우동':6000,'막창':50000,'피자':20000}
#print(dic.values())
#print(type(dic.values()))
a = 0
for i in dic.values():
    a = a+ i
print('점심메뉴 평균은?')
print(a/len(dic))
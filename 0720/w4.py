
a= int(input())

for i in range(a,-1,-1):
    print(i, end=' ')
#2
lst = list(range(a+1))[::-1]
print(*lst)
#3
while a>=0:
    print(a, end = ' ')
    a -=1


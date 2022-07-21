a= int(input())
for i in range(a+1):
    print((' '*(a-i)+('*')*(i)))


#2
for i in range(a):
    print(' '*(a-i-1)+'*'*(i+1))
#3
for i in range(1, a+1):
    print(' '*(a-i)+'*'*i)
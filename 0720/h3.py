n=5
m=9
#1
for i in range(m):
    print('*'*n)
#2 이중 for문
for i in range(m):
    for j in range(n):
        print('*', end="")
    print()
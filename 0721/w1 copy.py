num = int(input())

for i in range(1, num+1):
    if num % i == 0:
        print(i, end=' ')

print(*(range(num)))

## pinrt(1,2,3,4,5)
## print(*lst)
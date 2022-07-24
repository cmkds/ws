a= int(input())
total = 0
for i in range(1,a+1):
    total = total + i
print(total)


## 2
def list_sum(lsts):
    lst_sum =0
    for lst in lsts:
        for num in lst:
            lst_sum +=num
    print(lst_sum)
    return lst_sum
    



list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
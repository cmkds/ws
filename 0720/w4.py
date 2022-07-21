def list_sum(lsts):
    lst_sum =0
    for lst in lsts:
        for num in lst:
            lst_sum +=num
    print(lst_sum)
    return lst_sum
    



list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])





# a= int(input())

# for i in range(a,-1,-1):
#     print(i, end=' ')
# #2
# lst = list(range(a+1))[::-1]
# print(*lst)
# #3
# while a>=0:
#     print(a, end = ' ')
#     a -=1


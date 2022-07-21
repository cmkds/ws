lsts=([[1 ], [2 , 3 ], [4 , 5 , 6 ], [7 , 8 , 9 , 10 ]])

total =0
for lst in lsts:
    for i in lst:
        total += i
print(total)





#######
lst=([[1 ], [2 , 3 ], [4 , 5 , 6 ], [7 , 8 , 9 , 10 ]])
s=0
for small_lst in lst:
    for value in small_lst:
        s += value
def count_blood(lst) :
    
    dic={'A' : lst.count('A'),
        'B':lst.count('B'),
        'O':lst.count('O'),
        'AB':lst.count('AB')}
    return dic

print(count_blood(['A', 'B', 'A', 'O', 'AB', 
    'AB', 'O', 'A', 'B', 'O', 'B', 'AB',
    ]))


#########
#set으로 풀기
lst=set([a,b,0,a,ab,a])
lst

#########
for i in lst:
    if dic.get(i):
        dic[i] +=1
    else:
        dic[i] =1

###########

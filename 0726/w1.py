def duplicated_letters(str):
    lst=[]
    for char in str:
        if str.count(char)>1:
            if lst.count(char)>0:
                continue
            else:
                lst.append(char)
    return lst

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))


##set
set_lst =set(lst)
for i in set_lst:
    if str.count(i)>1:
        ans.append(i)
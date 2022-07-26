def only_square_area(lst1,lst2):
    
    newLst=[]
    for l1 in lst1:
        for l2 in lst2:
            if l1==l2:
                newLst.append(l1*l2)
    return newLst

print(only_square_area([32,55,63],[13,32,40,55]))

####2
##셋으로 만들고 셋으로 만들고 교집합.
def only_square_area(lst1,lst2):
    lst1_set =set(lst1)
    lst2_set =set(lst2)
    ans_set = lst1_set & lst2_set
    ans = []
    for length in ans_set:
        ans.append(length**2)

    return ans
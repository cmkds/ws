def lonely(abc):
    # for idx,num in enumerate(abc):
    #     checkNum= idx
    #     while(True):
    #         if checkNum==len(abc)-1:
    #             break
    #         elif num==abc[checkNum+1]:
    #             del abc[checkNum+1]
                
    #         else:
    #             break

    for idx,num in enumerate(abc):
        while(True):
            if idx==len(abc)-1:
                break
            elif num==abc[idx+1]:
                del abc[idx+1]
                
            else:
                break

       
    return abc

    



print(lonely([1, 1, 3, 3, 0, 1, 1])) # => [1, 3, 0, 1]
print(lonely([4, 4, 4, 3, 3])) # => [4, 3]



#######for문 이용하기
lst=[1,1,3,3,0,1,1]
temp =lst[0]
ans = [lst[0]]
for i in lst[1:]:
    if temp != i:
        ans.append(i)
        temp =i

###########while문 이용하기
lst=[1,1,3,3,0,1,1]
idx=1
while 1: #나중에 바꾸세요
    if lst[idx] == lst[idx-1]:
        lst.pop(idx)
    else:
        idx += 1
def low_and_up(str):
    
    newChar=''
    for i, char in enumerate(str):
        if i%2==0:
            newChar+=char
        else:
            newChar+=char.upper()
    return newChar

#for문 돌리고 
#불형
#true면 슬라이싱 돌리면서 짝수번일때만 판별하면된다.

print(low_and_up('apple')) 
print(low_and_up('banana')) 

##########
##ord로 소문자 대문자 판별하기.
###ord로 변경후 a~z 사이 A~Z사이인지 확인하기.
ord('a'), ord('z')
ord('A')

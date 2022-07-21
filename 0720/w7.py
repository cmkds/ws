numbers =[
    85, 72 , 38 , 80 , 69 , 65 , 68 , 96 , 22 , 49 , 67, 51,
    61 , 63 , 87 , 66 , 24 , 80 , 83 , 71 , 60 , 64, 52, 90,
    60 , 49 , 31 , 23 , 99 , 94 , 11 , 25 , 24
]

count = 0
# for i in range(len(numbers)):
#     count +=1
#     if count>1 :
#         if (numbers[count-1])< (numbers[count-2]):
#             numbers[count-1], numbers[count-2]=numbers[count-2], numbers[count-1]
#             count -=1 
#             i -=1


middle =int(count/2)

print(numbers[middle])
#######################################################################################

numbers =[
    85, 72 , 38 , 80 , 69 , 65 , 68 , 96 , 22 , 49 , 67, 51,
    61 , 63 , 87 , 66 , 24 , 80 , 83 , 71 , 60 , 64, 52, 90,
    60 , 49 , 31 , 23 , 99 , 94 , 11 , 25 , 24
]


for tc in range(1, len(numbers)+1):
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1-i):
            if (numbers[j])> (numbers[j+1]):
                numbers[j], numbers[j+1]=numbers[j+1], numbers[j]

middle = int(len(numbers)/2)
print(numbers)
print(middle)
print(numbers[middle])

#2
numbers = [1,2,3,4,5]
numbers = sorted(numbers)
l = len(numbers)
if l%2:
    print(numbers[len(numbers)%2])
else:
    print((numbers[1%2-1] + numbers[1%2+1])/2)
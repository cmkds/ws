def count_vowels(str):

    count =0
    vowel ='aeiou'
    for char in str:
        count +=vowel.count(char)
    return count

print(count_vowels('apple'))
print(count_vowels('banana'))

##
def func(string):
    ##1
    
    for i in 'aeiou':
        res += string.count(i)

    ##2
    res =0
    for i in string:
        if i in 'aeiou':
            res+=1
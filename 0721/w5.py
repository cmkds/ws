def get_secret_word(lst):
    a=''
    for ls in lst:
        a += chr(ls)
    return(a)

print(get_secret_word([83,115,65,102,89]))






def get_word(lst):
    ans = ''
    for num in lst:
        ans += chr(num)
    return ans
print(get_word([83,115,65,102,89]))
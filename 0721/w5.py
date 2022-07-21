def get_word(lst):
    ans = ''
    for num in lst:
        ans += chr(num)
    return ans
print(get_word([83,115,65,102,89]))
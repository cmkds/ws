def get_strong_word(word1, word2):
    total1 =0
    total2 =0

    for i in word1:
        total1 += ord(i)
    
    for i in word2:
        total2 += ord(i)

    if total1>total2:
        return word1
    elif total1<total2:
        return word2
    else :
        return total1, total2


print(get_strong_word('z','a'))
print(get_strong_word('delilah','dixon'))












# def get_strong(x,y):
#     x_num = 0
#     for i in x:
#         s += ord(i)
#     return s

# print(get_num('happy'))
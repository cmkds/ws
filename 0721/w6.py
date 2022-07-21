def get_secret_number(word):
    total =0
    for i in word:
        total += ord(i)

    return total

print(get_secret_number('happy'))






def get_num(string):
    s = 0
    for i in string:
        s += ord(i)
    return s

print(get_num('happy'))
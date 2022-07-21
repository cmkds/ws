def get_num(string):
    s = 0
    for i in string:
        s += ord(i)
    return s

print(get_num('happy'))
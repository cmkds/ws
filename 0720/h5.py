def get_middle_char(x):
    a = len(x)
    if a % 2 == 0:
        b = int(a/2-0.5)
        c = int(a/2+0.5)
        print(x[b],x[c])
    else:
        b= int(a/2-0.5)
        print(x[b])

get_middle_char('ssafy')

get_middle_char('coding')

#2
def get_middle_char(string):
    l = len(string)
    if 1%2:
        string[1//2]
    else:
        print(string[1//2-1]+string[1//2])
        print(string[1//2-1 : 1//2+1])

get_middle_char('ssafy')
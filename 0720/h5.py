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

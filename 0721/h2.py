def my_avg(*args):
    return sum(args)/len(args)

##
def my_avg(*args):
    count = 0
    for num in args:
        count+= num
    avg = count / len(args)
    return avg
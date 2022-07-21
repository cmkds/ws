
def dict_list_sum(lst):
    a=0
    for ls in lst:
        a=a+ls['age']
    print(a)
    return(a)



dict_list_sum([{'name':'kim','age':12},
     {'name':'lee','age':4}])
# print(dict_list_sum([{'name':'kim','age':12},
#      {'name':'lee','age':4}]))

# lst =[{'name':'kim','age':12},
#     {'name':'lee','age':4}]

# ### 
# s =0
# for dic in lst:
#     s += print(dic['age'])


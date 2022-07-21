
def dict_list_sum(students):
    a=0
    for student in students:
        a=a+student['age']
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


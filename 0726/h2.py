## .extend 와 .append 모두 리스트의 끝에 값이 추가된다는 것은 동일하다


lst = [1,2,3,4,5,6]

##.extend는 주어진 값의 인자를 하나하나 나눠서 리스트에 넣는다.
##쉽게 주어진 값을 for문을 돌려서 하나 씩 추가한다고
#생각하면 된다.
lst.extend('abcde')
print(lst) #[1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e']


##.append 는 값을 그대로 리스트 마지막에 추가한다.
lst = [1,2,3,4,5,6]
lst.append('abcde')
print(lst) #[1, 2, 3, 4, 5, 6, 'abcde']




##########
#########
#리스트 2개 깔끔하게 합치는법 extend 안쓰고.
lst = [1,2,3]
lst2= [4,5,6]
lst+lst2
lst[3:3] = lst2
print(lst)
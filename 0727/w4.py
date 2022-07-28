from faker import Faker

fake = Faker()

fake.name()

# class Faker():
#     def __init__(self,name):
#         self.name=name

import random
# print(random.random())
# print(random.random())

# print(random.seed(7777))
# print(random.random())

# random.seed(8888)
# random.random()

# fake1= Faker('ko_KR')
# Faker.seed(87654321)

# print(fake1.name())  #이진호

# fake2=Faker('ko_KR')
# print(fake2.name())  #강은주

#1) seed()는 알규먼트 값에 해당하는 값에대한 이름을 찾아.
#클래스의 name 속성을 변경해주는 메소드
#seed() 는 클래스 메소드

fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)

print(fake1.name()) #이진호

fake2=Faker('ko_KR')
print(fake2.name())  #김은정
2)
#seed_instance() 는 인스턴스 메소드
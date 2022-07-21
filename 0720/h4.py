temp = 36.5

print('입실 불가') if temp>=37.5 else print('입실 가능')
# 프린트 안에 한번에 넣어도 된다.
print('입실 불가' if temp>=37.5 else '입실 가능')
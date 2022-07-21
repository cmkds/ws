
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

# (1)
ssafy('가흔')

# (2)
ssafy(location='부울경', name='승현')

# (3)
ssafy('지우', location='서울')

# (4)
ssafy(name='승호', '광주')

## 키워드 인자를 사용한 뒤에 위치 인자를 활용할 수 없다.
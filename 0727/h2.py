__init__
-인스턴트를 생성
-객체를 초기화 할 때 사용
-메소드로 인해 객체가 생성되고 나면 호출된다.
__del__
-소멸자 메서드
-객체가 소멸될 때 호출된다.

__str__ ##표시용
-해당 객체의 출력 형태를 지정
-프린트 함수를 호출할 때, 자동으로 호출
-어떤 인스턴스를 출력하면 __str__의 return 값이 출력


__repr__  ##개발자용
-객체를 문자열로 표현하기 위해 사용.
-eval 함수에 사용 가능하다.
-새로운 객체를 만들어 낼 수 있다.
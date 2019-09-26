# 파이썬 연습문제 161 ~ 170

# 161 클래스와 인스턴스의 차이점에 대해 서술하라
print('# 161')
print('''클래스와 인스턴스의 차이점
인스턴스는 클래스로 만든 객체이다.
a 클래스와 a 클래스로 만든 객체 b가 있을 때
b는 객체이고 a 클래스의 인스턴스이다.''')
print()

# 162 비어있는 사람 (Human) 클래스를 "정의" 하라.


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print('응애응애')

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print('이름 : {}, 나이 : {}, 성별 : {}'.format(
            self.name, self.age, self.sex))

    def __del__(self):
        print('나의 죽음을 알리지 말라')


# 163 사람 (Human) 클래스를 "생성" 하고 areum 변수에 바인딩하여라.
areum = Human('조아름', 25, '여자')

# 164 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하여라.
areum

# 165 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하여라.
print(areum.age)

# 166 165에서 생성한 인스턴스의 이름, 나이, 성별을 출력하여라. 인스턴스 변수에 접근하여 값을 얻어 오세요.
print(areum.name, areum.age, areum.sex)

# 167 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 구현하여라.
areum.who()

# 168 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하여라.
areum.setInfo('아름', 25, '여자')

# 169 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하여라.
del areum

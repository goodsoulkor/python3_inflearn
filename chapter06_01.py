# chapter 06-01
# 파이썬 클래스
# oop(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 & 인스턴스의 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# ex1


# class Dog(object):  # object 상속
#     pass

# class Dog():
#     pass

class Dog:
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog('mikky', 2)
b = Dog('baby', 3)
c = Dog('mikky', 2)

# 비교
print(a == b, id(a), id(b), id(c))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# ex2
# self의 이해


class SelfTset:
    def func1(self):
        print('Func1 called')

    def func2(self):
        print('Func2 called')


f = SelfTset()

# print(dir(f))
print(id(f))
# f.func1()  # 예외
f.func2()
SelfTset.func1()
# SelfTset.func2()  # 예외
SelfTset.func2(f)

# ex3
# 클래스 변수, 인스턴스 변수


class WareHouse:
    # 클래스 변수
    stock_num = 0  # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse('Lee')
user2 = WareHouse('Cho')

print(WareHouse.stock_num)
# WareHouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', WareHouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('after', WareHouse.__dict__)

# ex4


class Dog:
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old.'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)


# 인스턴스 생성
c = Dog('July', 4)
d = Dog('Marry', 10)

# 메서드 호출
print(c.info())
print(d.info())
# 메서드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))

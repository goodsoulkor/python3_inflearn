# Chapter03-3
# 파이썬 리스트
# 자료구조에서 주요하다.
# 리스트 자료형(순서 O, 중복 O, 수정 O, 삭제 O)

# 선언
a = []
b = list()
c = [70, 80, 80, 90]  # Len이 가능하다.
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print('>>>>>>>>>>')
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

# Identity(id)
print('>>>>>>>>>>')
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>' * 20)
c[0] = 4
print('c -', c)
c[1:2] = ['a', 'b', 'c']  # 이렇게 하면 요소가 들어간다.(범위를 지정하면 요소로)
# c[1:2] = [['a', 'b', 'c']] --> 이렇게 하면 리스트가 들어간다.
print('c -', c)
c[1] = ['a', 'b', 'c']  # 인덱스 하나를 특정하면 리스트로 들어간다.
print('c - ', c)
c[1:3] = []  # 이렇게도 삭제가 가능하다.
print('c - ', c)
del c[2]  # 삭제
print('c - ', c)

# 리스트 함수
print('>' * 20)
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10)  # append() 끝에 데이터를 삽입
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7)
print('a - ', a)
a.reverse()
print('a - ', a)
a.remove(10)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop())  # pop() stack / Last In First Out / 마직막 값을 먼저 뺀다
print('a - ', a)
print('a - ', a.count(4))
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용 pop()
while a:
    data = a.pop()
    print(data)

# Chapter 03-06
# 파이썬 집합
'''
집합(Set) 특징
1. 순서가 없다.
2. 중복을 허용하지 않는다.
'''

# 선언
a = set()
b = set([1, 2, 3, 4, 4, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {41, 'foo', (1, 2, 3), 3.14159}

print('a :', type(a), a)
print('b :', type(b), b)
print('c :', type(c), c)
print('d :', type(d), d)
print('e :', type(e), e)
print('f :', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print(type(t), t)
print(t[0], t[1:3])

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)
print('l :', l)
print('l2 :', l2)

# 길이
print(len(a))
print(len(b))

# 집합 자료용 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 :', s1 & s2)
print('s1 & s2 :', s1.intersection(s2))
print()

print('s1 | s2 :', s1 | s2)
print('s1 | s2 :', s1.union(s2))
print()

print('s1 - s2 :', s1 - s2)
print('s1 - s2 :', s1.difference(s2))
print()

# 중복 원소 확인
print('s1 & s2 :', s1.isdisjoint(s2))  # 교집합이 있으면 False

# 부분 집합 확인
print('subset :', s1.issubset(s2))
print('superset :', s1.issuperset(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 :', s1)

s1.remove(2)  # 값이 없으면 오류가 난다.
print('s1 :', s1)
# s1.remove(7)

s1.discard(3)
print('s1 :', s1)
s1.discard(8)  # 값이 없어도 오류가 발생하지 않는다.

s1.clear()
print('s1 :', s1)

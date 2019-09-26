# chapter 04-02
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#   <Loop body>

for v1 in range(10):
    print('vi is :', v1)
print()

for v2 in range(1, 11):
    print('v2 is :', v2)
print()

for v3 in range(1, 11, 2):
    print('v3 is :', v3)
print()

# 1 ~ 1000합
sum1 = 0

for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 Sum :', sum1)

print('1 ~ 1000 Sum :', sum(range(1, 1001)))
print('1 ~ 1000 4의 배수의 합 :', sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('You are :', name)
print()

# 예제2
lotto_number = [11, 19, 21, 28, 36, 37]

for n in lotto_number:
    print("Current number :", n)
print()

# 예제3
word = 'Beautiful'

for s in word:
    print('word :', s)
print()

# 예제4
my_info = {
    'name': 'Lee',
    'age': 33,
    'city': 'Seoul'
}

for k in my_info:
    print('Key :', k)
print()

for k in my_info:
    print('values :', my_info[k])
print()

for k in my_info:
    print('value :', my_info.get(k))
print()

for v in my_info.values():
    print('value :', v)
print()

for k, v in my_info.items():
    print('key & value :', k, v)
print()

# 예제5
name = "FineApple"

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
print()

# break
numbers = [13, 3, 4, 7, 19, 24, 17, 2, 33, 15, 34, 36, 38]

for n in numbers:
    if n == 34:
        print('Found : 34!')
        break
    else:
        print('Not found :', n)
print()

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type :", v, type(v))
    print("multiply by 2 :", v * 3)
print()

# for - else

numbers = [13, 3, 4, 7, 19, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 49:
        print('Found : 49')
        break
else:
    print('Not Found : 49')
print()

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='')
    print()
print()

# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('tuple', tuple(reversed(name2)))
print('set', set(reversed(name2)))

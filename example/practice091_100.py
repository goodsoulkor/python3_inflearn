# 파이썬 문제풀이 091 ~ 100

# 091 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
print('# 091')
print('bool')
print('type(True) :', type(True))
print('type(False) :', type(False))
print()

# 092
print('# 092')
print('3 == 5 :', 3 == 5)
print()

# 093
print('# 093')
print('3 < 5 :', 3 < 5)
print()

# 094
print('# 094')
x = 4
print('1 < x < 5 :', 1 < x < 5)
print()

# 095
print('# 095')
print((3 == 3) and (4 != 3))
# True and True는 True
print()

# 096
# print(3 => 4)
# >= 이렇게 써야 맞는 표현이다.

# 097
print('# 097')
if 4 < 3:
    print("Hello World")
print()

# 098
print('# 098')
if 4 < 3:
    print("Hello World.")
else:
    print('Hi, there.')
print()

# 099
print('# 099')
if True:
    print('1')
    print('2')
else:
    print('3')
print('4')
print()

# 100
print('# 100')
if True:
    if False:
        print('1')
        print('2')
    else:
        print('3')
else:
    print('4')
print('5')

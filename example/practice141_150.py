# 파이썬 연습문제 풀이 141 ~ 150

# 141 대문자만 화면에 출력하라.
print('# 141')
my_list = ["A", "b", "c", "D"]

for i in my_list:
    if i.isupper():
        print(i)
print()

# 142 소문자만 화면에 출력하라.
print('# 142')
my_list = ["A", "b", "c", "D"]

for i in my_list:
    if i.islower():
        print(i)
print()

# 143 리스트의 문자를 대문자는 소문자로, 소문자는 대문자로 변환하라.
print('# 143')
my_list = ["A", "b", "c", "D"]
result = ''

for i in my_list:
    if i.islower():
        result += i.upper()
    else:
        result += i.lower()
print(result)
print()

# 144 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split 메서드를 사용)
print('# 144')
file_list = ['hello.py', 'ex01.py', 'ch02.py', 'intro.hwp']

for i in file_list:
    name = i.split('.')
    print(name[0])
print()

# 145 파일 이름이 리스트에 저장되어 있을 때 확장자가 *.h인 파일을 출력하라.
print('# 145')
filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in filenames:
    extention = i.split('.')
    if extention[1] == 'h':
        print(i)
print()

# 146 파일 이름이 리스트에 저장되어 있을 때 확장자가 .h나 .c인 파일을 화면에 출력하라.
print('# 146')
filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in filenames:
    extention = i.split('.')
    if extention[1] == 'h' or extention[1] == 'c':
        print(i)
print()

# 147 양수만 new_list 이름의 리스트에 저장하라.
print('# 147')
my_list = [3, -20, -3, 44]
new_list = []

for i in my_list:
    if i > 0:
        new_list.append(i)
print(new_list)
print()

# 148 대문자만을 upper_list에 저장하라.
print('# 148')
my_list = ["A", "b", "c", "D"]
upper_list = []

for i in my_list:
    if i.isupper():
        upper_list.append(i)
print(upper_list)
print()

# 149 my_list의 값을 sole_list에 저장하라. 단, 중복된 값은 제거한다.
print('# 149')
my_list = [3, 4, 4, 5, 6, 6]
sole_list = []

for i in my_list:
    if i not in sole_list:
        sole_list.append(i)
print(sole_list)
print()

# 150 내장 함수를 사용하지 않고 반복문을 사용해서 my_list에 저장된 모든 수의 합를 출력하라
print('# 150')
my_list = [3, 4, 5]
sum = 0

for i in my_list:
    sum += i
print(sum)

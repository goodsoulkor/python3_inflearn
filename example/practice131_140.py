# 파이썬 연습문제 131 ~ 140

# 131
print('# 131')
my_list = ["가", "나", "다", "라"]

for i in range(1, 4):
    print(my_list[i])

# for i in my_list[1:]:
#     print(i)
print()

# 132
print('# 132')
my_list = [1, 2, 3, 4, 5, 6]

for i in my_list[::2]:
    print(i)

print()

# 133
print('# 133')
my_list = [1, 2, 3, 4, 5, 6]
for i in my_list[1::2]:
    print(i)
print()

# 134
print('# 134')
my_list = ["가", "나", "다", "라"]
for i in my_list[::-1]:
    print(i)
print()

# 135 음수를 출력하라
print('# 135')
my_list = [3, -20, -3, 44]

for i in my_list:
    if i < 0:
        print(i)
print()

# 136 3의 배수를 출력하라
print('# 136')
my_list = [3, 100, 23, 44]

for i in my_list:
    if i % 3 == 0:
        print(i)
print()

# 137 세 글자 이상의 문자를 화면에 출력하라
print('# 137')
my_list = ["I", "study", "python", "language", "!"]

for i in my_list:
    if len(i) >= 3:
        print(i)
print()

# 138 5보다 크고 10보다 작은 수를 화면에 출력하라
print('# 138')
my_list = [3, 1, 7, 10, 5, 6]

for i in my_list:
    if i > 5 and i < 10:
        print(i)
print()

# 139 10보다 크고 20 보다 작으면서 3의 배수일 경우 화면에 출력하라
print('# 139')
my_list = [13, 21, 12, 14, 30, 18]

for i in my_list:
    if i > 10 and i < 20:
        if i % 3 == 0:
            print(i)
print()

# 140 3의 배수이거나 4의 배수를 화면에 출력하라
print('# 140')
my_list = [3, 1, 7, 12, 5, 16]

for i in my_list:
    if i % 3 == 0 or i % 4 == 0:
        print(i)

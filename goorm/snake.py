# https://level.goorm.io/exam/51353/%EB%B1%80%EC%9D%B4-%EC%A7%80%EB%82%98%EA%B0%84-%EC%9E%90%EB%A6%AC/quiz/1

user_input = list(input().split())
height = int(user_input[0])
width = int(user_input[1])
a = 0

for i in range(1, height + 1):
    if i % 2 != 0:
        print('#' * width)
    elif i % 2 == 0:
        if a == 0:
            print('.' * (width - 1) + '#')
            a += 1
        else:
            print('#' + '.' * (width - 1))
            a -= 1

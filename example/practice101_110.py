# 문제풀이 101 ~ 110

# 101 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
# print('# 101')
# user_input = input()
# print(user_input * 2)
# print()

# 102 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# print('# 102')
# user_input1 = int(input('숫자를 입력하세요: '))
# print(user_input1 + 10)

# 103 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# user_input = int(input())
# if user_input % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# 104 사용자로부터 값을 입력받은 후 해당 값에 +20을 더한 값을 출력하라. 단 값의 범위는 0~255로 가정한다. 255를 초과하는 경우 255를 출력해야 한다.
# user_input = int(input('입력값 : '))
# result = user_input + 20
# if result < 255:
#     print(result)
# else:
#     print(255)

# 105 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 값의 범위는 0~255이다. 0보다 작은 값이되는 경우 0을 출력해야 한다.
# user_input = int(input('입력값 : '))
# result = user_input - 20
# if result > 0:
#     print(result)
# else:
#     print(0)

# 106 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# user_input = input('현재시간 : ')
# if user_input[3:] == '00':
#     print('정각 입니다.')
# else:
#     print('정각이 아닙니다.')

# 107 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = ["사과", "포도", "홍시"]
# user_input = input('좋아하는 과일은? ')
# if user_input in fruit:
#     print('정답입니다.')
# else:
#     print('오답입니다.')

# 108
# warn_investment_list = ["Microsoft", "Google",
#                         "Naver", "Kakao", "SAMSUNG", "LG"]
# user_input = input()
# if user_input in warn_investment_list:
#     print('warning')
# else:
#     print('not warning')

# 109 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# user_input = input('My favorite : ')
# if user_input in fruit:
#     print('yes')
# else:
#     print('no')

# 110 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
user_input = input()
if user_input in fruit.values():
    print('Yes')
else:
    print('No')

# 문제풀이 111 ~ 120

# 111 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
# user_input = input()
# if user_input.islower() == True:
#     print(user_input.upper())
# else:
#     print(user_input.lower())

# 112
# user_input = int(input('score : '))
# if user_input > 80:
#     print('grade is A')
# elif user_input > 60:
#     print('grade is B')
# elif user_input > 40:
#     print('grade is C')
# elif user_input > 20:
#     print('grade is D')
# else:
#     print('grade is E')

# 113
# money = {
#     '달러': 1167,
#     '엔': 1.096,
#     '유로': 1268,
#     '위안': 171
# }
# user_input = input('입력 : ')
# user_input_list = user_input.split(' ')

# if user_input_list[1] == '달러':
#     ratio = money['달러']
# elif user_input_list[1] == '엔':
#     ratio = money['엔']
# elif user_input_list[1] == '유로':
#     ratio = money['유로']
# elif user_input_list[1] == '위안':
#     ratio = money['위안']

# print(int(user_input_list[0]) * ratio, '원')

# 114
# input_number1 = int(input('input number1: '))
# input_number2 = int(input('input number2: '))
# input_number3 = int(input('input number3: '))

# input_list = [input_number1, input_number2, input_number3]
# print(max(input_list))

# 115
# telecom = {
#     '011': 'SKT',
#     '016': 'KT',
#     '019': 'LGU',
#     '010': '알수없음'
# }
# user_number = input('휴대전화 번호 입력: ')
# user_number_list = user_number.split('-')
# if user_number_list[0] == '011':
#     print('당신은 {0} 사용자 입니다.'.format(telecom['011']))
# elif user_number_list[0] == '016':
#     print('당신은 {0} 사용자 입니다.'.format(telecom['016']))
# elif user_number_list[0] == '019':
#     print('당신은 {0} 사용자 입니다.'.format(telecom['019']))
# elif user_number_list[0] == '010':
#     print(telecom['010'])

# 116
# user_input = input('우편번호: ')
# if user_input[2] in ['0', '1', '2']:
#     print('강북구')
# elif user_input[2] in ['3', '4', '5']:
#     print('도봉구')
# elif user_input[2] in ['6', '7', '8', '9']:
#     print('노원구')

# 116 다른 풀이
# 문자열로 비교 가능
# user_input = input('우편번호: ')
# if user_input[2] in '012':
#     print('강북구')
# elif user_input[2] in '345':
#     print('도봉구')
# elif user_input[2] in '6789':
#     print('노원구')


# 117
# user_input = input('주민등록번호: ')
# if user_input[7] in ['1', '3']:
#     print('male')
# elif user_input[7] in ['2', '4']:
#     print('Female')

# 118
# user_input = input('주민등록번호 : ')
# if int(user_input[8:10]) <= 8:
#     print('서울 입니다.')
# elif int(user_input[8:10]) > 8:
#     print('서울이 아닙니다.')

# 119
# user_input = input('주민등록번호 : ')
# calc1 = ((int(user_input[0]) * 2) +
#          (int(user_input[1]) * 3) +
#          (int(user_input[2]) * 4) +
#          (int(user_input[3]) * 5) +
#          (int(user_input[4]) * 6) +
#          (int(user_input[5]) * 7) +
#          (int(user_input[7]) * 8) +
#          (int(user_input[8]) * 9) +
#          (int(user_input[9]) * 2) +
#          (int(user_input[10]) * 3) +
#          (int(user_input[11]) * 4) +
#          (int(user_input[12]) * 5)) % 11
# calc2 = 11 - calc1

# if int(user_input[-1]) != calc2:
#     print('유효하지 않은 주민등록번호 입니다.')
# else:
#     print('유효한 주민등록번호입니다.')

# print(calc2)

# 120
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# change = int(btc['max_price']) - int(btc['min_price'])

# if (int(btc['opening_price']) + change) > int(btc['max_price']):
#     print('상승장')
# else:
#     print('하락장')

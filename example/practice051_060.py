# 파이썬 문제 풀이 51 ~ 60

# 051 price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
print('# 051')
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
print()

# 052 슬라이싱을 사용해서 홀수만 출력하라.
print('# 052')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
print()

# 053 슬라이싱을 사용해서 짝수만 출력하라.
print('# 053')
print(nums[1::2])
print()

# 054 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
print('# 054')
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
print()

# 055
print('# 055')
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])
print()

# 056
print('# 056')
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest[0], interest[1], interest[2],
      interest[3], interest[4])
print(' '.join(interest))
print()

# 057
print('# 057')
print(interest[0], interest[1], interest[2],
      interest[3], interest[4], sep='/')
print('/'.join(interest))
print()

# 058 join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
print('# 058')
print('\n'.join(interest))
print()

# 059
print('# 059')
string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)
print()

# 060
print('# 060')
string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
interest = string.split('/')
print(interest)

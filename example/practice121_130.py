# 파이썬 문제 풀이 121 ~ 130

# 121
for i in ['가', '나', '다', '라']:
    print(i)
print()

# 122
for i in ['사과', '귤', '수박']:
    print(i)
print()

# 123
for i in ['사과', '귤', '수박']:
    print(i)
    print('--')
print()

# 124
for i in ['사과', '귤', '수박']:
    print(i)
print('--')
print()

# 125
menu = ["김밥", "라면", "튀김"]

for i in menu:
    print('오늘의 메뉴 :', i)
print()

# 126
portfolio = ["SK하이닉스", "삼성전자", "LG전자"]

for i in portfolio:
    print(i, '보유중')
print()

# 127
pets = ['dog', 'cat', 'parrot', 'squirrel', 'goldfish']

for i in pets:
    print(i, len(i))
print()

# 128
prices = [100, 200, 300]

for i in prices:
    print(i + 10)
print()

# 129
prices = ["129,300", "1,000", "2,300"]

for i in prices:
    result = int(i.replace(',', ''))
    print(result)
print()

# 130
menu = ["면라", "밥김", "김튀"]

for i in menu:
    print(i[::-1])

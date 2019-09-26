# 파이썬 문제 풀이 071 ~ 080

# 071 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
print('# 071')
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, a, b = scores
*valid_score, _, _ = scores
print(valid_score)
print()

# 072 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
print('# 72')
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(a, b, valid_score)
print()

# 073 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
print('# 073')
a, *valid_score, b = scores
print(a, valid_score, b)
print()

# 074 temp 이름의 비어있는 딕셔너리를 만들라.
print('# 074')
temp = {}
print(temp, type(temp))
print()

# 075 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
print('# 075')
icecream = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
print(icecream)
print()

# 076 075 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
print('# 076')
icecream.update(죠스바=1200, 월드콘=1500)
print(icecream)
print()

# 077 메로나 가격을 출력하라.
print('# 077')
print(icecream.get('메로나'))
print(icecream['메로나'])
print()

# 078 메로나의 가격을 1300으로 수정하라.
print('# 078')
icecream.update(메로나=1300)
print(icecream)
print()

# 079 메로나를 삭제하라.
print('# 079')
del icecream['메로나']
print(icecream)
print()

# 080
# 없는 key 값을 호출해서

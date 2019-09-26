# 파이썬 연습 문제 풀이 061 ~ 070

# 061 다음 코드의 결과 예측
print('# 061')
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0
interest_1[0] = 'Naver'
# interest_0의 값도 바뀐다.
print(interest_0)
print()

# 062 다음 코드의 결과 예측
print('# 062')
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0[:2]
interest_1[0] = 'Naver'
# interest_0의 값에는 영향을 미치지 않는다.
print(interest_0)
print()

# 063 my_variable 이름의 비어있는 튜플을 만들라.
print('# 063')
my_variable = ()
print(my_variable, type(my_variable))
print()

# 064 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# t = (1, 2, 3)
# t[0] = 'a'
print('# 064')
print('# 튜플은 수정이 불가능하다.')
print()

# 065 숫자 1 이 저장된 튜플을 생성하라.
print('# 065')
t = (1,)
print(t, type(t))
print()

# 066 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
print('# 066')
t = 1, 2, 3, 4
print('t는 튜플이다.')
print(t, type(t))
print()

# 067 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
print('# 067')
t = ('a', 'b', 'c')
t1 = ('A', 'b', 'c')
t = t1
print(t)
print()

# 068 다음 튜플을 리스트로 변환하라.
print('# 068')
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest)
print()

# 069 다음 리스트를 튜플로 변경하라.
print('# 069')
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest)
print()

# 070 아래 코드의 실행 결과를 예측하라
print('# 070')
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a + b + c)
# 결과는 6 / a, b, c에 언팩킹한다.

# Chapter 03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
'''
딕셔너리 자료형의 특징
1. 순서가 없다.
2. 키는 중복을 허용하지 않는다.
3. 수정이 가능하다.
4. 삭제가 가능하다.
'''

# 선언
a = {'name': 'goodsoul', 'phone': '01011112222', 'birth': '800612'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
)

print('a :', type(a), a)
print('b :', type(b), b)
print('c :', type(c), c)
print('d :', type(d), d)
print('e :', type(e), e)
print('f :', type(f), f)

# 출력
print('\n- 출력 -')
print('a :', a['name'])  # 키가 존재하지 않으면 에러발생
# get을 사용할 때 키가 존재하지 않으면 None으로 처리된다. 때문에 get 함수로 가져오는게 보다 안전하다.
print('a :', a.get('name1'))
print('b :', b[0])
print('b :', b.get(0))
print('f :', f.get('City'))
print('f :', f.get('Age'))


# 딕셔너리 추가
print('\n- 딕셔너리 추가 -')
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3]
print('a :', a)

# 딕셔너리 길이(키의 갯수)
print('\n- 딕셔너리 길이(키의 갯수) -')
print('len(a) :', len(a))
print('len(b) :', len(c))
print('len(c) :', len(c))
print('len(d) :', len(d))

# 딕셔너리 함수 : dict_keys, dict_values, dict_items --> 반복문
print('\n- 딕셔너리 함수 keys() -')
print('a key :', a.keys())
print('b key :', b.keys())
print('c key :', c.keys())
print('d key :', d.keys())
print('a :', list(a.keys()))
print('b :', list(b.keys()))

print('\n- 딕셔너리 함수 values() -')
print('a values :', a.values())
print('b values :', b.values())
print('c values :', c.values())
print('a :', list(a.values()))
print('b :', list(b.values()))

print('\n- 딕셔너리 함수 items() -')
print('a.items() :', a.items())
print('b.items() :', b.items())
print('c.items()', c.items())

print(list(a.items()))
print(list(b.items()))
print()

print('a :', a.pop('name'))
print('a :', a)

print('c :', c.pop('arr'))
print('c :', c)
print()

print('f :', f.popitem())
print('f :', f)
print('f :', f.popitem())
print('f :', f)
print('f :', f.popitem())
print('f :', f)
print('f :', f.popitem())
print('f :', f)
print('f :', f.popitem())
print('f :', f)
print()

print('a :', a)
print('a birth in :', 'birth' in a)
print('a birth2 in :', 'birth2' in a)

# 수정
print('\n- 수정 & 추가 -')
a['test'] = 'test_dict'
print('a :', a)

a['address'] = 'Daejeon'
print('a :', a)

a.update(birth='910904')
print('a :', a)

temp = {'birth': '800612'}
a.update(temp)
print('a :', a)

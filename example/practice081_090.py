# 파이썬 문제풀이 081 ~ 090

# 081 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
print('# 081')
inventory = {
    '메로나': [300, 20],
    '비비빅': [400, 3],
    '죠스바': [250, 100]
}
print(inventory)
print()

# 082 inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
print('# 082')
print(inventory['메로나'][0], '원')
print()

# 083 inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
print('# 083')
print(inventory['메로나'][1], '개')
print()

# 084 inventory 딕셔너리에 아래 데이터를 추가하라.
print('# 084')
inventory.update(월드콘=[500, 7])
print(inventory)
print()

# 085 다음의 딕셔너리에서 key 값으로만 구성된 리스트를 생성하라.
print('# 085')
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream_list = list(icecream.keys())
print(icecream_list)
print()

# 086 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
print('# 086')
icecream_values = list(icecream.values())
print(icecream_values)
print()

# 087 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
print('# 087')
print(sum(icecream.values()))
print()

# 088 new_product 딕셔너리를 087번의 icecream 딕셔너리에 추가하라.
print('# 088')
new_product = {'팥빙수': 2700, '아맛나': 1000}
icecream.update(new_product)
print(icecream)
print()

# 089 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
print('# 089')
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)
# result = {
#     keys[0]: vals[0],
#     keys[1]: vals[1],
#     keys[2]: vals[2]
# }
result = dict(zip(keys, vals))
print(result)
print()

# 090 date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
print('# 090')
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = {
#     date[0]: close_price[0],
#     date[1]: close_price[1],
#     date[2]: close_price[2],
#     date[3]: close_price[3],
#     date[4]: close_price[4],

# }
close_table = dict(zip(date, close_price))
print(close_table)

# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묵어주는 역할을 하는 함수 이다.

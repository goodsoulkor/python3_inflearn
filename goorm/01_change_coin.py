# 알고리즘 히어로즈 셀프레벨테스트 1차
# https://level.goorm.io/exam/49912/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%96%B4%EB%A1%9C%EC%A6%88-%EC%85%80%ED%94%84%EB%A0%88%EB%B2%A8%ED%85%8C%EC%8A%A4%ED%8A%B8-1%EC%B0%A8/quiz/1

user_money = int(input())
change = 1000 - user_money
coin = [500, 100, 50, 10]

for i in coin:
    if change > i:
        print(change // i, end=' ')
        change %= i
    else:
        print(0, end=' ')

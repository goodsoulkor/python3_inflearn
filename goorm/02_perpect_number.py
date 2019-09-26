# 알고리즘 히어로즈 셀프레벨테스트 2차
# 범위 안의 완전수를 찾아라
# https://level.goorm.io/exam/49912/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%96%B4%EB%A1%9C%EC%A6%88-%EC%85%80%ED%94%84%EB%A0%88%EB%B2%A8%ED%85%8C%EC%8A%A4%ED%8A%B8-1%EC%B0%A8/quiz/2

number = input().split()
start = int(number[0])
end = int(number[1])

for i in range(start, end + 1):
    sum = 0
    for v in range(1, i):
        if i % v == 0:
            sum += v
    if sum == i:
        print(i, end=' ')

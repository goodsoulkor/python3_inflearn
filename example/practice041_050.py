# 041
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

# 042
print(movie_rank)
movie_rank.append('배트맨')
print(movie_rank)
print()

# 043 "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)
print()

# 044 '럭키'를 삭제하라.
movie_rank.remove('럭키')
# del movie_rank[3]
print(movie_rank)
print()

# 045 '스플릿' 과 '배트맨'을 를 삭제하라.
del movie_rank[2:]
print(movie_rank)
print()

# 046 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)
print()

# 047 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
print('min:', min(nums))
print('max:', max(nums))
print()

# 048 다음 리스트의 합을 출력하라.
nums = [1, 2, 3, 4, 5]
print(sum(nums))
print()

# 049 다음 리스트에 저장된 데이터의 개수를 화면에 구하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자",
        "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))
print()

# 050 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)

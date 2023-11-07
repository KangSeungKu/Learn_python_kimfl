food = ["피자", "햄버거", ["감자튀김", "김치"], 100, "삼겹살"]

print(type(food))       # <class 'list'>
print(len(food))        # 5
print(food[0])          # 피자
print(food[-1])         # 삼겹살
print(food[0:2])        # ['피자', '햄버거']
print(type(food[4]))    # <class 'str'>
print(type(food[3]))    # <class 'int'>
print(food[2])          # ['감자튀김', '김치']
print(food[2][0])       # 감자튀김


# 리스트 합치기
food2 = [100, "김치", "삼겹살"]
food3 = ["햄버거", "감자튀김"]

food4 = food2 + food3
food5 = food2 * 3

print(food4)    # [100, '김치', '삼겹살', '햄버거', '감자튀김']
print(food5)    # [100, '김치', '삼겹살', 100, '김치', '삼겹살', 100, '김치', '삼겹살']


food6 = ["김치", "삼겹살"]
food6.append("피자")

print(food6)    # ['김치', '삼겹살', '피자']

# 요소 중간 추가
food6.insert(1, "햄버거")
print(food6)    # ['김치', '햄버거', '삼겹살', '피자']

# 요소 삭제
food6.remove("김치")
print(food6)    # ['햄버거', '삼겹살', '피자']

# 요소 삭제
# 한꺼번에 삭제되는 것이 아닌 맨 앞의 인덱스의 요소를 삭제하게 됨.
food7 = ["김치", "삼겹살", "김치", "김치"]
food7.remove("김치")
print(food7)    # ['삼겹살', '김치', '김치']

# 개수
print(food7.count("김치"))      # 2

# 인덱스
print(food7.index("삼겹살"))    # 0
print(food7.index("김치"))      # 1


# 정렬
food8 = ["김치", "삼겹살", "김치", "포도"]
food9 = ["g", "a", "T", "p"]

food8.sort()
food9.sort()

print(food8)    # ['김치', '김치', '삼겹살', '포도']
print(food9)    # ['T', 'a', 'g', 'p']

# 정렬
food9.sort(reverse=True)
print(food9)    # ['p', 'g', 'a', 'T']

# 리스트 수정
food9[0] = "피자"
print(food9)    # ['피자', 'g', 'a', 'T']

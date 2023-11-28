food1 = ("피자", "햄버거", "치킨", "라면", "된장찌개")
food2 = ["피자", "햄버거", "치킨", "라면", "된장찌개"]

print(type(food1))  # <class 'tuple'>
print(type(food2))  # <class 'list'>

print(food1[0:3])   # ('피자', '햄버거', '치킨')

food3 = ("피자", "햄버거", "치킨")
food4 = ("라면", "된장찌개")

# 더하기 가능
print(food3 + food4)    # ('피자', '햄버거', '치킨', '라면', '된장찌개')

# 길이 측정 가능
print(len(food1))   # 5

# 곱하기 가능
print(food3 * 3)    # ('피자', '햄버거', '치킨', '피자', '햄버거', '치킨', '피자', '햄버거', '치킨')

# 큰 차이
food2[0] = "김치"
print(food2)

food1[0] = "김치"
# 튜플은 값을 변경할 수 없음.
print(food1)
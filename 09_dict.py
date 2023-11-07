# {"key": "value"}
user = {"name": "초코", "job": "웹프로그래머", "email": "choco@naver.com"}

print(user["name"]) # 초코
print(user["job"])  # 웹프로그래머

# 요소 추가
user["age"] = 30
print(user)     # {'name': '초코', 'job': '웹프로그래머', 'email': 'choco@naver.com', 'age': 30}

# 요소 삭제
del user["name"]
print(user)     # {'job': '웹프로그래머', 'email': 'choco@naver.com', 'age': 30}

# 요소 수정
user["age"] = 31
print(user)     # {'job': '웹프로그래머', 'email': 'choco@naver.com', 'age': 31}

keys_list = user.keys()
print(keys_list)        # dict_keys(['job', 'email', 'age'])
print(type(keys_list))  # <class 'dict_keys'>

keys_list = list(keys_list)
print(keys_list)        # ['job', 'email', 'age']
print(type(keys_list))  # <class 'list'>

# 값 리스트
value_list = user.values()
print(value_list)       # dict_values(['웹프로그래머', 'choco@naver.com', 31])
print(type(value_list)) # <class 'dict_values'>

# 키, 값 모든 리스트
item_list = user.items()
print(item_list)       # dict_values(['웹프로그래머', 'choco@naver.com', 31])
print(type(item_list)) # <class 'dict_values'>

# 반복문에 사용할 경우에는 별도의 형변환을 하지 않아도 무관
# append나 list로 사용하고 싶을 때는 형변환 필요
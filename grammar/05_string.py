name = "승구"
job = "웹프로그래머"
age = 30

# 일반적이지만 사용이 용이하지 않음.
print("안녕하세요. 내 이름은 " + name + "입니다." + "직업은 " + job + "입니다." + "나이는 " + str(age) + "입니다.")

# 포맷팅을 이용한 방법
print("안녕하세요. 내 이름은 %s입니다. 직업은 %s입니다. 나이는 %s입니다." %(name, job, age))

# format함수를 사용하는 경우
print("안녕하세요. 내 이름은 {0}입니다. 직업은 {1}입니다. 나이는 {2}입니다.".format(name, job, age))

# f string 포맷팅 (3.6v 이상부터 사용가능)
print(f"안녕하세요. 내 이름은 {name}입니다. 직업은 {job}입니다. 나이는 {age}입니다.")
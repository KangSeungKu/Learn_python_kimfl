user_data = {"name" : "초코", "age" : "30", "email" : "choco@gmail.com"}

# 방법 1
for data in user_data:
    print(f"{data} : {user_data[data]}")

# 방법 2
for data in user_data.items():
    print(f"{data[0]} : {data[1]}")
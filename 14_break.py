count = 1

while True:
    count += 1
    if count == 5:
        print(f"좀 쉬어야겠다...")
        continue

    print(f"{count}바퀴째")
    if count > 10 :
        break

print("달리기를 마쳤습니다.")
"""만약 오늘 == 월요일:
    출근한다.
만약 오늘 == 일요일:
    더 잔다."""

today = "수요일"

if today == "월요일":
    print("출근해야지.")
elif today == "일요일":
    print("오늘은 쉬는날~!")
else:
    print("무슨요일이지?")
    

state1 = True
state2 = False

if state1 and state2:
    print("참")
else:
    print("거짓")
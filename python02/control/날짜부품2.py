# 날짜와 시간을 알려주는 부품 사용.
import datetime

now = datetime.datetime.now()
print("오늘은 ",  now)
print("-----------------------")

# 오늘은 학원을 가는 날일까요??. 판단.
요일 = '월화수목금토일'[now.weekday()]
print("오늘은 ", 요일, "요일입니다.")

if 요일 == '토' or 요일 == '일' : 
    print("오늘은 학원에 가는 날입니다.")
else :
    print("오늘은 학교에 가는 날입니다.")
    
















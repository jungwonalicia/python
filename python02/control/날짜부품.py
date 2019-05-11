# 날짜와 시간을 알려주는 부품 사용.
import datetime
import time

now = datetime.datetime.now()
print(now)
time.sleep(2)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.weekday()) #요일
print('월화수목금토일'[now.weekday()]) #요일









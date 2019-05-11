# 조건 => 날짜
# 날짜입력: 어제
# 어제는 금요일이었어요.
# 
# 날짜입력: 오늘
# 오늘은 토요일이예요.
# 
# 날짜입력: 내일
# 내일은 일요일이예요.
from _ast import In

def  날짜판별(data):
    if data == '어제':
        print('어제는 금요일이었어요.')
    elif data == '오늘':
        print('오늘은 토요일이예요.')
    else:
        print('내일은 일요일이예요.')
        

data = input("날짜 입력>> ")
날짜판별(data)
        













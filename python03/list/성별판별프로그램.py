# 주민번호를 입력하세요.
# 880115-1037515, 990115-2078144
# 880115-3037515, 990115-4078144

number = input("주민번호 입력>> ")
data = number[7]

if data == '3' or data == '1':
    print('남자입니다.')
elif data == '4'or data == '2':
    print('여자입니다.')
else:
    print('알 수 없습니다.')
    
    











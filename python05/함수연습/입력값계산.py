# 입력값1: 300
# 입력값2: 100
# 연산자 : +
# 
# 입력값1: 300
# 입력값2: 100
# 연산자 : -
# 
# 세 개의 입력값을 이용해서
# 결과 출력하는 함수를 만들어보세요.
# 
# 함수명: 계산(x, y, z)

def 계산(x, y, z):
    if z == '+':
        print(x + y)
    elif z == '-':
        print(x - y)

x = int(input("입력값1: "))
y = int(input("입력값2: "))
z = input("연산자: ")

계산(x, y, z)







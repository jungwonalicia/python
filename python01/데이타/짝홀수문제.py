# 짝수, 홀수 판별 문제는 나누기를 가지고 함.
# 입력값을 2로 나누어서 나머지가 0이면 짝수, 아니면  홀수

data = int(input("숫자 입력: "))
data2 = data % 2 #data2 = 나머지

if data2 == 0:
    print("짝수")
else:
    print("홀수")
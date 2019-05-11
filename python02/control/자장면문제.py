# 자장면 가격은 고정, 변수에 넣어줌.
price = 4500

# 인원수를 입력--> 계산을 위해서 int()정수로 바꾸어줌.
person = int(input("인원수 입력: "))

# 변수에 들어간 데이타 타입을 알고 싶으면 type()
print(type(price))
print(type(person))

# 총금액을 계산
total = price * person

# 총금액에서 2000원 할인
내야할금액 = total - 2000

# 내야할 금액을 출력
print("내가 내야할 금액은 ", 내야할금액, "원 입니다.")






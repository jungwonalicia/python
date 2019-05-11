data = range(0, 5, 1)
print(data)

음식 = ['감자', '고구마', '양파', '피자', '아이스크림']
#리스트의 위치값을 이용해서 값을 가지고 올 때는 index(위치값)사용
print(음식[0]) #첫번째 값
print(음식[4]) #다섯번째 값

print(len(음식))

#index을 이용해서 한번에 출력(반복문)
def food_print(): #함수(function)
    for i in range(0, 5, 1):
        print(음식[i])

음식[2] = "햄버거"
print(음식[2])

food_print()












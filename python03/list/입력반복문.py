# 3번 입력을 받아서
# 콜라, 사이다, 주스를 리스트에 넣어서 출력

음료 = []

#반복문을 통해서 여러번 입력받음-->리스트에 저장
for count in range(0, 3, 1):
    food = input("마시고 싶은 음료를 입력>> ")
    음료.append(food)

for imsi in 음료:
    print(imsi)


    
food = []

for count in range(0, 3, 1):
    data = input("음식 종류 입력: ")
    food.append(data)

def food_print():
    for f in food:
        print(f, end = " ")
    print()

food_print()

food[0] = '라면'
food[1] = '스파게티'
food[2] = '불고기'

food_print()






     

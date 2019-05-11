# 반복문 문제
# -----------
# range(시작값, 끝나는값+1, 증감값)
# 1. 숫자를 1부터 10까지 출력
for x in range(1, 11, 1):
    print(x, end = " ")
print()

# 2. 숫자를 5부터 1씩 작아지면서 출력
for x in range(5, 0, -1) :
    print(x, end = " ")
print()

# 3. 숫자를 1부터 20사이의 값 중 홀수만 출력
for x in range(1, 21, 2):
    print(x, end = " ")
print()

for x in range(1, 21):
    if x % 2 != 0:
        print(x, end = " ")
print()
   
# 4. 숫자를 1부터 20사이의 값 중 3의 배수만 출력
for x in range(0, 21, 3):
    if x != 0:
        print(x, end = " ")
print()

# 5. 숫자를 1부터 100사이의 값 중 5의 배수 개수 출력
count = 0
for x in range(0, 101, 5):
    if x != 0:
        print(x, end = " ")
        count = count + 1
print()
print("전체 5의 배수의 개수는 ", count, "개")
        
    










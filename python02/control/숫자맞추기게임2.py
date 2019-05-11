import random

target = random.randrange(100)
count = 0 #count의 시작값은 0부터 시작.

while True:
    count = count + 1
    data = int(input("당신이 생각한 숫자를 입력 : "))
    
    if(data == target) :
        print("정답입니다.")
        print("정답 시도 횟수는 ", count)
        break
    else:
        print("정답이 아닙니다.")
        if data > target :
            print("너무 큽니다.") 
        else:
            print("너무 작습니다.") 
            
    
        
        
        
        
        
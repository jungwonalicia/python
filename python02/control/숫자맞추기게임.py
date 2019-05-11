target = 55

while True:
    data = int(input("당신이 생각한 숫자를 입력 : "))
    
    if(data == target) :
        print("정답입니다.")
        break
    else:
        print("정답이 아닙니다.")
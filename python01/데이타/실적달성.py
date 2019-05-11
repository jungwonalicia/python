target = int(input("실적을 입력하세요.."))

if target >= 1000 :
    print("실적 달성")
    print("당신의 보너스는 " , int(target * 0.2))
else:
    print("실적 미달성")
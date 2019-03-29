# 모든 입력 데이터 타입은 string.
# int <-- string (타입변환, 형변환, casting)
data1 = int(input("실적을 입력하세요..>> "))
if data1 >= 1000:
    print("실적달성")
    bonus = (data1 - 1000) * 0.1
    print("당신의 보너스는 " , bonus)
else:
    print("실적 미달성")
    print("다음 기회에...")
    
print("프로그램 종료")
     

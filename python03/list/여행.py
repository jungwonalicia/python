# 1. 여행가고싶은곳 세곳을 리스트로 넣는다.
여행 = ['강릉', '속초', '안면도']

# 2. 전체 프린트
for 지역 in 여행:
    print(지역)
    
print()

#함수를 만들 때는 def(definiton:정의, 만듦)
def 음식프린트():
    for 위치값 in range(0, 3, 1):
        print(여행[위치값])

# 3. 두번째 여행가고 싶은곳의 항목을 제주도로 변경
여행[1] = '제주도'

# 4. 변경된 내용 프린트
# 이미 만들어놓은 함수를 사용(호출한다. call)
음식프린트()






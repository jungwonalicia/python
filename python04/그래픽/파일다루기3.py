
#10번 입력받아서 파일에 저장
def input10():
    name = input('만들고 싶은 파일이름: ')
    file3 = open(name + '.txt', 'w')
    for count in range(0, 10):
        data = input("저장 데이터 입력>> ")
        file3.write(data + "\n")
    print(name + '파일을 생성했습니다.')

#만들어놓은 함수를 사용: 함수명()
#함수를 사용하는 것을 함수를 호출한다.(call, 콜)        
input10()


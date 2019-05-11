영화 = ['생일', '어스', '돈', '헬보이', '파이브피트']

#쓸 수만 있는 movie.txt와의 stream(강물, 통로) 생성
#stream은 한 방향으로만 흐른다.
#읽기용 스트림 또는 쓰기용 스트림을 따로 만들어주어야 한다.
file7 = open('movie.txt', 'w')

# 컨트롤+/ => 해당 자동 주석
# print(영화[0]) #리스트에서 첫번째 값을 의미
# print(영화[1]) #리스트에서 두번째 값을 의미

#리스트 반복문 이용해서 출력
for index in range(0, 5): #0,1,2,3,4
    print(영화[index])

#리스트 반복문 이용해서 파일에 저장
for index in range(0, 5):
    file7.write(영화[index] + '\n')

file7.close() #쓰기 모드로 연결되었던 스트림이을 닫음.(사라짐)

#저장한 파일 읽어오기
print('-----저장한 파일 읽어오기')
file8 = open('movie.txt', 'r')
for index in range(0, 5):
    data = file8.read()
    print(data)
file8.close()
    







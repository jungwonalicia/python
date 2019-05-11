# 채팅을 프로그램을 만들기 위해서 필요한 것.
# 1. 전화기 역할을 하는 socket이 필요.
# 2. 네트워크 프로그램이기 때문에 ip가 필요.
# 2. ip가 동일하기 때문에 A, B를 구분해줄 필요.(port)
# 전송방식 TCP와 UDP 중에서 UDP => SOCK_DGRAM
# 초간단채팅A는 수신용.(받는 쪽)

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind(('192.168.0.5', 6007))

print('수신용 소켓 생성 완료!! ')
print('데이터 받기를 기다리는 중...보내주세요..')

while True:
    data, ip = sock.recvfrom(1024)
    print("수신된 데이터>> ", data.decode('utf-8'))
    
    
    
    
    
    
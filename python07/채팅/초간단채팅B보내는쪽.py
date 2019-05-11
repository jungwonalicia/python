# 초간단채팅B는 송신용.(보내는 쪽)

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

print('송신용 소켓 생성 완료!! ')

while True:
    data = input('데이터 입력>> ')
    sock.sendto(data.encode('utf-8'), ('192.168.0.5', 6007))
#     print("송신된 데이터>> ", data)

















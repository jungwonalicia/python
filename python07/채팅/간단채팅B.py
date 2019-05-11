import socket

#소켓은 받는 쪽, 보내는 쪽 소캣을 각각 만들어야 한다.
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(('192.168.0.5', 4000))

print('-------------------------------')
print('---------  간단 채팅 B  ----------')
print('-------------------------------')

while True:
    # 채팅 보내는 부분
    data2 = input('간단 채팅 B>> ')
    sock1.sendto(data2.encode('utf-8'), ('192.168.0.5', 3000))
    
    # 채팅 받는 부분
    data, addr = sock2.recvfrom(1024)
    print('간단 채팅 A>> ', data.decode('utf-8'))
    











 
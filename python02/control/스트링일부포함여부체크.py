email = "hera@naver.com"

if email.endswith('.com'):
    print('닷컴회사군요.')
elif email.endswith('.net'):
    print('닷넷회사군요.')
else:
    print('기타 회사군요.')

if email.startswith('he'):
    print('he로 시작하는 군요.')
else:
    print('he로 시작하지 않는 군요.')
    
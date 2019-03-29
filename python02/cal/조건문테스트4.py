user = "root" #변수명은 대문자로 쓰지 않습니다.
pw = "1234"

iUser = input("user: ")
iPw = input("pw: ")

if iUser == user and iPw == pw:
    print("로그인 OK")
else:
    print("로그인 NOT")
    


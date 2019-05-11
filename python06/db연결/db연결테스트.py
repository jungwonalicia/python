import pymysql as sql

def db(id, pw, name, tel):
    #1. db(shoes) 연결
    #    db명, id(root), pw(1234)
    con = sql.connect(host='localhost', 
                user='root',
                password='1234',
                db='shoes'
                )
    print('1. DB연결 성공!!!')
    print(con)
    
    #2. 데이터 전송을 위한 통로를 만든다.(cursor 커서)
    cur = con.cursor()
    print('2. DB연결 통로 만들기 성공!!!')
    
    #3. 데이터 전송, 실행
    data = "insert into member values ('"+ id +"','" + pw + "','" + name + "','" + tel + "')"
    print('전송할 데이터 SQL문: ', data)
    cur.execute(data)
    print('3.데이터 전송 성공!!!')
    
    con.commit()

#### 회원정보를 입력받아서 DB에 전송, 실행
print('회원가입 정보를 입력해주세요.')
print('---------------------')
id2 = input("id입력>> ")
pw2 = input("pw입력>> ")
name2 = input("name입력>> ")
tel2 = input("tel입력>> ")
print('--------------------')
db(id2, pw2, name2, tel2)











import pymysql as sql
from tkinter import *

def db():
    id2 = id.get()
    pw2 = pw.get()
    name2 = name.get()
    tel2 = tel.get()
    
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
    data = "insert into member values ('"+ id2 +"','" + pw2 + "','" + name2 + "','" + tel2 + "')"
    print('전송할 데이터 SQL문: ', data)
    cur.execute(data)
    print('3.데이터 전송 성공!!!')
    
    con.commit()

#### 회원정보를 입력받아서 DB에 전송, 실행
w = Tk()
w.geometry('500x550')
w.title('나의 회원가입 화면')
w.configure(bg = 'white')

#이미지는 혼자 w라는 프레임에 올리지 못함.
#라벨이나 버튼을 먼저 만들어서 그곳에 끼워넣어야 함.
icon = PhotoImage(file='naver.png')
img = Label(w, image=icon)
img.pack()

l1 = Label(w, text='아이디 입력', font = ('궁서', 30), bg='white', fg='blue')
l1.pack()
id = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
id.pack()
l2 = Label(w, text='패스워드 입력', font = ('궁서', 30), bg='white', fg='blue')
l2.pack()
pw = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
pw.pack()
l3 = Label(w, text='이름 입력', font = ('궁서', 30), bg='white', fg='blue')
l3.pack()
name = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
name.pack()
l4 = Label(w, text='전화번호 입력', 
           font = ('궁서', 30), bg='white', fg='blue')
l4.pack()

tel = Entry(w, font=('궁서', 30), bg='yellow', fg='red')
tel.pack()

button = Button(w, text='회원가입처리', 
           font = ('궁서', 30), bg='pink', fg='blue',
           command = db)
button.pack()

w.mainloop()











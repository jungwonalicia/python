from tkinter import * #생략함
import pymysql as mysql #닉네임을 사용

def db처리():
    # 1. DB연결(어떤 db에 연결할지, db이름, user, password)
    con = mysql.connect(  host='localhost',
                        user = 'root',
                        password = '1234',
                        db = 'lim'
                    )
    print('1. DB연결 성공..!!! ')
    print(con)
    
    # 2. 연결통로 만들기
    cur = con.cursor()
    print('2. DB연결 통로 만들기 성공..!!! ')
    
    # 입력한 값 가지고 오는 부분.
    day = day2.get()
    title = title2.get()
    content = content2.get()
    etc = etc2.get()
    
    # 3. SQL만들기
    sql = "insert into diary values ('" + day + "','" + title + "','" + content + "','" + etc + "')"
    print('만들어진  sql문: ', sql)
    print('3. SQL문 만들기 성공!!!')
    
    # 4. SQL문을 mySQL에 전달
    cur.execute(sql)
    print('4. SQL문 mySQL에 전달 성공!!!')
    
    con.commit()

w = Tk()
w.geometry('500x700')
w.title('나의 일기장')
img = PhotoImage(file ='diary.png')
top = Label(w, image = img)
top.pack()
day1 = Label(w,  #날짜
             text = '날짜', 
             font = ('궁서', 20),
             bg = 'white', #라벨의 배경색
             fg = 'blue' #글자색
             )
day1.pack()
day2 = Entry(w, 
             font = ('궁서', 20),
             bg = 'yellow', #입력의 배경색
             fg = 'red' #글자색
             )
day2.pack()
title1 = Label(w, 
             text = '제목', 
             font = ('궁서', 20),
             bg = 'white', #라벨의 배경색
             fg = 'blue' #글자색
             )
title1.pack()
title2 = Entry(w, 
             font = ('궁서', 20),
             bg = 'yellow', #입력의 배경색
             fg = 'red' #글자색
             )
title2.pack()

content1 = Label(w, 
             text = '내용', 
             font = ('궁서', 20),
             bg = 'white', #라벨의 배경색
             fg = 'blue' #글자색
             )
content1.pack()
content2 = Entry(w, 
             font = ('궁서', 20),
             bg = 'yellow', #입력의 배경색
             fg = 'red' #글자색
             )
content2.pack()
etc1 = Label(w, 
             text = '기타', 
             font = ('궁서', 20),
             bg = 'white', #라벨의 배경색
             fg = 'blue' #글자색
             )
etc1.pack()
etc2 = Entry(w, 
             font = ('궁서', 20),
             bg = 'yellow', #입력의 배경색
             fg = 'red' #글자색
             )
etc2.pack()
button = Button(w, text = '일기장 DB에 저장', 
                bg = 'lime', fg = 'blue',
                font = ('궁서', 30),
                command = db처리 
                #버튼에 함수를 연결할 때는 함수명만 씀!!!
                )
button.pack()


w.mainloop()




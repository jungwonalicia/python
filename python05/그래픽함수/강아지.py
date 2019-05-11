from tkinter import *

def 강아지버튼처리():
    x = e1.get();
    print("강아지 버튼을 눌렀군요...")
    print("강아지 이름은 ", x)
    
def 버튼처리():
    print("버튼을 눌렀군요...")

w = Tk()
img = PhotoImage(file='dog.PNG')

b2 = Button(w,
            image = img,
            command = 강아지버튼처리
            )
b2.pack()

e1 = Entry(w, #텍스트 입력용
           font=('궁서', 30),
           bg = 'lime',
           fg = 'red'
           )
e1.pack()










b = Button(w, 
           text='나는 버튼입니다.',
           font=('맑은 고딕', 30),
           bg='yellow', #backgroud: 배경색
           fg='blue' , #foreground: 글자색
           command=버튼처리
           )
b.pack()


w.mainloop()


